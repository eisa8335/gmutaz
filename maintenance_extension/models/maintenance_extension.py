# -*- coding: utf-8 -*-
from odoo import fields, models, api, _
from odoo.exceptions import UserError, ValidationError
import math


class PartnerInherit(models.Model):
    _inherit = 'res.partner'

    contact_line_ids = fields.One2many('contact.address.line', 'partner_id')


class MaintenanceRequestInherit(models.Model):
    _inherit = 'maintenance.request'

    signature = fields.Char(string='Signature')
    installation_base_id = fields.Many2one('equipments.installation.base', string="Equipment", tracking=True)
    location_id = fields.Many2one('stock.location', string="Location", tracking=True,domain="[('usage', '=', 'internal')]")
    stock_id = fields.Many2one('stock.picking', string="Picking", tracking=True)
    used_line_ids = fields.One2many('part.used.line', 'maintenance_id', string="Equipment")
    picking_count = fields.Integer(compute='_compute_stock_count')

    @api.model
    def create(self, vals):
        res = super().create(vals)
        if res.installation_base_id:
            res.installation_base_id.request_ids = [(4, res.id)]
        return res

    def create_delivery_order(self):
        picking_type = self.env['stock.picking.type'].search([('code', '=', 'outgoing'),('company_id', '=', self.company_id.id)],limit=1)
        dest_location = self.env['stock.location'].search([('name', '=', 'Customers')],limit=1)
            
            
        stock_picking = self.env['stock.picking'].create({
            # 'partner_id': self.partner_id.id,
            'scheduled_date': self.request_date,
            # 'move_type': self.picking_policy,
            'company_id': self.company_id.id,
            'location_id': self.location_id.id,
            # 'group_id': self.procurement_group_id.id,
            'picking_type_id': picking_type.id,
        })
        for line in self.used_line_ids:
            stock_move = self.env['stock.move'].create({
                'product_id': line.part_id.id,
                'product_uom': line.part_id.uom_id.id,
                'product_uom_qty': line.qty,
                'description_picking': line.part_id.name,
                'name': line.part_id.name,
                'company_id': self.company_id.id,
                'picking_id': stock_picking.id,
                'location_id': self.location_id.id,
                'location_dest_id': dest_location.id
                })
        self.stock_id = stock_picking.id

    def write(self, vals):

        if 'installation_base_id' in vals:
            previous_installation_base_id = self.installation_base_id
            super().write(vals)
            if previous_installation_base_id != self.installation_base_id:
                previous_installation_base_id.request_ids = [(3, self.id)]
            self.installation_base_id.request_ids = [(4, self.id)]
            return
        return super().write(vals)

    def show_picking(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Stock',
            'res_model': 'stock.picking',
            'view_mode': 'tree,form',
            'view_type': 'form',
            'view_id': False,
            'domain': [('id', '=', self.stock_id.id)],
        }

    def _compute_stock_count(self):
        for rec in self:
            if rec.stock_id:
                rec.picking_count = 1
            else:
                rec.picking_count = 0

    def print_report(self):
        return self.env.ref('maintenance_request_report.maintenance_request_report').report_action(self)

    @api.constrains('duration')
    def _check_duration(self):
        for rec in self:
            if rec.duration <= 0:
                raise ValidationError('Please specify Duration Time for this Maintenance Request.')

    @api.constrains('used_line_ids')
    def _check_duplicate_parts(self):
        for rec in self:
            part_ids = rec.used_line_ids.mapped('part_id.id')
            if len(set(part_ids)) != len(part_ids):
                raise ValidationError('Please Remove Duplicate Spare Parts.')

    @api.onchange('installation_base_id')
    def get_parts(self):
        if self.used_line_ids:
            for line in self.used_line_ids:
                line.unlink()
        self.category_id = self.installation_base_id.classification_id.id
        installation_base_parts = self.installation_base_id.part_line_ids
        for part in installation_base_parts:
            self.env['part.used.line'].create({
                'part_id': part.part_id.id,
                'qty': part.qty,
                'maintenance_id': self.id
            })


class EquipmentsInstallationBase(models.Model):
    _name = 'equipments.installation.base'
    _inherit = ["mail.thread", "mail.activity.mixin"]

    record_id = fields.Char(string='Record Id', readonly=True, default='New', tracking=True)
    active = fields.Boolean(default=True)
    name = fields.Char(tracking=True)
    model = fields.Char(tracking=True)
    currency_id = fields.Many2one('res.currency', string="Currency",
                                  default=lambda self: self.env.company.currency_id)
    floor = fields.Char(tracking=True)
    room = fields.Char(tracking=True)
    note = fields.Text(string='Notes', tracking=True)
    serial_number = fields.Char(string='Serial Number', tracking=True)
    batch = fields.Char(tracking=True)
    delivery_date = fields.Date(string='Delivery Date', tracking=True)
    procurement_id = fields.Char(string='Procurement ID', tracking=True)
    image = fields.Binary()
    warranty_start_date = fields.Date(string='Warranty Start Date', tracking=True)
    warranty_period = fields.Char(string='Warrenty Period', tracking=True)
    price = fields.Monetary(string='Price', currency_field='currency_id', tracking=True)
    classification_id = fields.Many2one('maintenance.equipment.category', string="Classification", ondelete='restrict',
                                        tracking=True)
    part_line_ids = fields.One2many('spare.part.line', 'equipment_id', ondelete='restrict', tracking=True)
    request_ids = fields.Many2many('maintenance.request', string="Work Items", ondelete='restrict', tracking=True,
                                   readonly=True)
    supplier_id = fields.Many2one('res.partner', string="Supplier", ondelete='restrict', tracking=True)
    equipment_age = fields.Float(string='Equipment Age', compute='_get_age', store=True, tracking=True)
    operational_cost = fields.Float(string='Operational Cost', compute='_compute_operational_cost', store=True,
                                    tracking=True)
    percentage_depreciation = fields.Integer(string='Percentage Of Depreciation', tracking=True)
    value_depreciation = fields.Float(string='Value Depreciation', compute='_compute_depreciation', store=True,
                                      tracking=True)
    current_value = fields.Float(string='Current Value', compute='_compute_depreciation', store=True, tracking=True)
    no_of_item = fields.Float(string='Number Of Maintenance Work Items', compute='_get_operational_cost', store=True,
                              tracking=True)
    state = fields.Selection([('draft', 'Draft'), ('confirm', 'Confirm')], 'State', default='draft', tracking=True)

    @api.constrains('price')
    def _check_price(self):
        for rec in self:
            if rec.price < 100:
                raise ValidationError('Price must be greater then or equal to 100.')

    @api.model
    def create(self, vals):
        vals['record_id'] = self.env['ir.sequence'].next_by_code('equipments.installation.sequence') or _('New')
        res = super().create(vals)
        return res

    @api.depends('delivery_date')
    def _get_age(self):
        for rec in self:
            if not rec.delivery_date:
                rec.equipment_age = 0
            else:
                delta = fields.Date.today() - rec.delivery_date
                rec.equipment_age = delta.days / 365

    @api.depends('delivery_date', 'percentage_depreciation', 'price')
    def _compute_depreciation(self):
        for rec in self:
            if rec.delivery_date and rec.percentage_depreciation:
                delta_date = fields.Date.today() - rec.delivery_date
                value_depreciation = math.floor(delta_date.days / 365) * (
                        rec.price * (rec.percentage_depreciation / 100))
                if value_depreciation:
                    rec.value_depreciation = value_depreciation
                else:
                    rec.value_depreciation = 0
            else:
                rec.value_depreciation = 0
            rec.current_value = rec.price - rec.value_depreciation if rec.value_depreciation else rec.price

    @api.depends('request_ids')
    def _compute_operational_cost(self):
        for rec in self:
            if rec.request_ids:
                for request in rec.request_ids:
                    request.installation_base_id = rec.id
                rec.no_of_item = len(rec.request_ids)
                total_cost_for_operations = 0
                for work_item in rec.request_ids:
                    if not work_item.employee_id:
                        raise UserError(
                            f"No Employee Specified with Work Item {work_item.name}. We need an employee to get their hourly rate for Operational Cost.")
                    if not work_item.duration:
                        raise ValidationError(
                            f"Please specify Maintenance Duration for {work_item.name}.")
                    total_cost_for_operations += work_item.duration * work_item.employee_id.hourly_rate
                rec.operational_cost = total_cost_for_operations
            else:
                rec.no_of_item = 0
                rec.operational_cost = 0

    def set_to_draft(self):
        self.state = "draft"

    def set_to_confirm(self):
        self.state = "confirm"


class HrEmployeeExtension(models.Model):
    _inherit = 'hr.employee'

    working_hours = fields.Float(string='Working Hours', tracking=True)
    hourly_rate = fields.Float(string='Hourly Rate', tracking=True)
    installation_base_count = fields.Integer(compute='_compute_equipment_count')

    def show_equipments(self):
        request_objs = self.env['maintenance.request'].search([('employee_id', '=', self.id)])
        equipment_ids = list(set(request_objs.mapped('installation_base_id.id')))
        return {
            'type': 'ir.actions.act_window',
            'name': 'Equipments',
            'res_model': 'equipments.installation.base',
            'view_mode': 'tree,form',
            'view_type': 'form',
            'view_id': False,
            'domain': [('id', 'in', equipment_ids)],
        }

    def _compute_equipment_count(self):
        for rec in self:
            requests = self.env['maintenance.request'].search([('employee_id', '=', rec.id)])
            rec.installation_base_count = len(set(requests.mapped('installation_base_id.id')))

    @api.constrains('hourly_rate')
    def _check_hourly_rate(self):
        for rec in self:
            if rec.hourly_rate <= 0:
                raise ValidationError('Please specify Hourly Rate.')


class ContactAddress(models.Model):
    _name = 'contact.address.line'

    phone = fields.Char()
    mobile = fields.Char()
    email = fields.Char()
    website = fields.Char()
    address = fields.Char()
    partner_id = fields.Many2one('res.partner')


class SparePartLine(models.Model):
    _name = 'spare.part.line'

    part_id = fields.Many2one('product.product', string='Part')
    qty = fields.Float()
    equipment_id = fields.Many2one('equipments.installation.base')


class SpareUsedLine(models.Model):
    _name = 'part.used.line'

    part_id = fields.Many2one('product.product', string='Part')
    qty = fields.Float()
    maintenance_id = fields.Many2one('maintenance.request')


class ProductProductExt(models.Model):
    _inherit = 'product.product'

    part_id = fields.Char(readonly=True)
    image = fields.Binary()
    model = fields.Char(string='Model Number', tracking=True)
    manufacturer = fields.Char(string='Manufacturer', tracking=True)
    supplier_id = fields.Many2one('res.partner', string="Supplier", tracking=True)
    dimensions = fields.Char(tracking=True)
    compatibility = fields.Many2one('equipments.installation.base', tracking=True)
    condition = fields.Selection([('new', 'New'), ('used', 'Used'), ('refurbished', 'Refurbished')], 'Condition',
                                 default='new', tracking=True)
    warranty = fields.Date(tracking=True)
    is_part = fields.Boolean()

    @api.model
    def create(self, vals):
        vals['part_id'] = self.env['ir.sequence'].next_by_code('part.detail.sequence') or _('New')
        res = super().create(vals)
        return res


class EquipmentCategoryExt(models.Model):
    _inherit = 'maintenance.equipment.category'

    installation_base_count = fields.Integer(compute='_compute_equipment_count')

    def show_equipments(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Equipments',
            'res_model': 'equipments.installation.base',
            'view_mode': 'tree,form',
            'view_type': 'form',
            'view_id': False,
            'domain': [('classification_id', '=', self.id)],
        }

    def _compute_equipment_count(self):
        for rec in self:
            rec.installation_base_count = self.env['equipments.installation.base'].search_count(
                [('classification_id', '=', self.id)])
