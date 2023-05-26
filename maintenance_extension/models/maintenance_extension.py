# -*- coding: utf-8 -*-
from odoo import fields, models, api, _
from odoo.exceptions import UserError, ValidationError
import math
from random import randint
from datetime import date
import logging
_logger = logging.getLogger('odoo')


class PartnerInherit(models.Model):
    _inherit = 'res.partner'

    contact_line_ids = fields.One2many('contact.address.line', 'partner_id')


class MaintenanceRequestInherit(models.Model):
    _inherit = 'maintenance.request'

    reference = fields.Char(string="Record Id", copy=False)
    signature = fields.Char(string='Signature')
    installation_base_id = fields.Many2one('equipments.installation.base', string="Installation Base", tracking=True)
    location_id = fields.Many2one('stock.location', string="Location", tracking=True,
                                  domain="[('usage', '=', 'internal')]")
    stock_id = fields.Many2one('stock.picking', string="Picking", tracking=True)
    used_line_ids = fields.One2many('part.used.line', 'maintenance_id', string="Equipment")
    picking_count = fields.Integer(compute='_compute_stock_count')
    duration = fields.Float(related='installation_base_id.maintenance_duration', readonly=False, store=True)
    edit_state = fields.Selection([
        ('open', 'Open'),
        ('locked', 'Locked')
    ], string='Edit Status', tracking=True, default='open')

    @api.model
    def create(self, vals):
        vals['reference'] = self.env['ir.sequence'].next_by_code('maintenance.request.sequence') or _('New')
        res = super().create(vals)
        if res.installation_base_id:
            res.installation_base_id.request_ids = [(4, res.id)]
        return res

    def lock_request(self):
        if not self.stock_id:
            self.create_delivery_order()
        self.edit_state = 'locked'

    def create_delivery_order(self):
        picking_type = self.env['stock.picking.type'].search(
            [('code', '=', 'outgoing'), ('company_id', '=', self.company_id.id)], limit=1)
        dest_location = self.env['stock.location'].search([('name', '=', 'Customers')], limit=1)

        stock_picking = self.env['stock.picking'].create({
            'scheduled_date': self.request_date,
            'company_id': self.company_id.id,
            'location_id': self.location_id.id,
            'picking_type_id': picking_type.id,
        })
        for line in self.used_line_ids:
            self.env['stock.move'].create({
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
    _description = 'Installation Base'
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
    maintenance_request_days = fields.Integer(help="Schedule No of Days to auto generate Work Requests.")
    maintenance_duration = fields.Float(help="Maintenance Duration in hours.", tracking=True)
    classification_id = fields.Many2one('maintenance.equipment.category', string="Classification", ondelete='restrict',
                                        tracking=True)
    part_line_ids = fields.One2many('spare.part.line', 'equipment_id', ondelete='restrict', tracking=True)
    request_ids = fields.Many2many('maintenance.request', string="Work Items", tracking=True,
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
    contract = fields.Binary()
    contract_start_date = fields.Date(string='Contract Start Date', tracking=True)
    contract_period = fields.Char(string='Contract Period', tracking=True)
    state = fields.Selection([('draft', 'Draft'), ('confirm', 'Confirm')], 'State', default='draft', tracking=True)

    def _default_color(self):
        return randint(1, 11)

    color = fields.Integer('Color', default=_default_color)

    @api.model
    def _generate_auto_work_request(self):
        installation_base_objects = self.search([])
        for record in installation_base_objects:
            scheduled_days = record.maintenance_request_days
            work_request_pool = self.env['maintenance.request']
            latest_record = work_request_pool.search([('installation_base_id', '=', record.id)], order='create_date desc', limit=1)
            if not latest_record.create_date:
                continue
            days_delta = (date.today() - latest_record.create_date.date()).days
            if days_delta > scheduled_days:
                stage = self.env['maintenance.stage'].search([], limit=1, order='id asc')
                obj = work_request_pool.create({
                    'name': f"PPM - {record.name}",
                    'maintenance_type': 'preventive',
                    'request_date': fields.Date.today(),
                    'employee_id': latest_record.employee_id.id,
                    'installation_base_id': record.id,
                    'duration': record.maintenance_duration,
                    'stage_id': stage.id
                })
                installation_base_parts = record.part_line_ids
                for part in installation_base_parts:
                    self.env['part.used.line'].create({
                        'part_id': part.part_id.id,
                        'qty': part.qty,
                        'maintenance_id': obj.id
                    })

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
                if delta.days > 0:
                    rec.equipment_age = delta.days / 365
                else:
                    rec.equipment_age = 0

    @api.depends('delivery_date', 'percentage_depreciation', 'price')
    def _compute_depreciation(self):
        for rec in self:
            if rec.delivery_date and rec.percentage_depreciation:
                delta_date = fields.Date.today() - rec.delivery_date
                value_depreciation = math.floor(delta_date.days / 365) * (
                        rec.price * (rec.percentage_depreciation / 100))
                if value_depreciation > 0:
                    rec.value_depreciation = value_depreciation
                else:
                    rec.value_depreciation = 0
            else:
                rec.value_depreciation = 0
            rec.current_value = rec.price - rec.value_depreciation if rec.value_depreciation else rec.price

    @api.depends('request_ids', 'request_ids.used_line_ids')
    def _compute_operational_cost(self):
        for rec in self:
            if rec.request_ids:
                rec.no_of_item = len(rec.request_ids)
                total_cost_for_operations = 0
                for work_item in rec.request_ids:
                    if not work_item.employee_id:
                        raise UserError(
                            f"No Employee Specified with Work Item {work_item.name}. We need an employee to get their hourly rate for Operational Cost.")
                    if not work_item.duration:
                        raise ValidationError(
                            f"Please specify Maintenance Duration for {work_item.name}.")
                    cost_for_parts = 0
                    if work_item.used_line_ids:
                        for part_line in work_item.used_line_ids:
                            cost_for_parts += part_line.part_id.lst_price * part_line.qty
                    total_cost_for_operations += work_item.duration * work_item.employee_id.hourly_rate + cost_for_parts
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
            'view_mode': 'kanban,tree,form',
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
    _description = 'Contact Address'

    phone = fields.Char()
    mobile = fields.Char()
    email = fields.Char()
    website = fields.Char()
    address = fields.Char()
    partner_id = fields.Many2one('res.partner')


class SparePartLine(models.Model):
    _name = 'spare.part.line'
    _description = 'Spare Part Installation Base'

    part_id = fields.Many2one('product.product', string='Part', domain=[('part_state', '=', 'confirm')])
    qty_available = fields.Float(related='part_id.qty_available', store=True, string='Quantity Available')
    qty = fields.Float()
    equipment_id = fields.Many2one('equipments.installation.base')


class SpareUsedLine(models.Model):
    _name = 'part.used.line'
    _description = 'Spare Part Maintenance Request'

    part_id = fields.Many2one('product.product', string='Part', domain=[('part_state', '=', 'confirm')])
    qty_available = fields.Float(related='part_id.qty_available', store=True, string='Quantity Available')
    qty = fields.Float()
    maintenance_id = fields.Many2one('maintenance.request')


class ProductProductExt(models.Model):
    _inherit = 'product.product'

    part_id = fields.Char(readonly=True)
    model = fields.Char(string='Model Number', tracking=True)
    manufacturer = fields.Char(string='Manufacturer', tracking=True)
    supplier_id = fields.Many2one('res.partner', string="Supplier", tracking=True)
    dimensions = fields.Char(tracking=True)
    compatibility = fields.Many2one('equipments.installation.base', tracking=True)
    condition = fields.Selection([('new', 'New'), ('used', 'Used'), ('refurbished', 'Refurbished')], 'Condition',
                                 default='new', tracking=True)
    warranty = fields.Date(tracking=True)
    is_part = fields.Boolean()
    part_state = fields.Selection([('draft', 'Draft'), ('confirm', 'Confirm')], 'State', default='draft', tracking=True)

    def action_draft(self):
        self.part_state = "draft"

    def action_confirm(self):
        self.part_state = "confirm"

    @api.model
    def create(self, vals):
        vals['part_id'] = self.env['ir.sequence'].next_by_code('part.detail.sequence') or _('New')
        res = super().create(vals)
        return res


class EquipmentCategoryExt(models.Model):
    _inherit = 'maintenance.equipment.category'

    installation_base_count = fields.Integer(compute='_compute_installation_base_count')

    def show_equipments(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Equipments',
            'res_model': 'equipments.installation.base',
            'view_mode': 'kanban,tree,form',
            'view_type': 'form',
            'view_id': False,
            'domain': [('classification_id', '=', self.id)],
        }

    def _compute_installation_base_count(self):
        for rec in self:
            rec.installation_base_count = self.env['equipments.installation.base'].search_count(
                [('classification_id', '=', self.id if self.id else 0)])
