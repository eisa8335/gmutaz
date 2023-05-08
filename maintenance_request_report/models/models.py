from odoo import models, fields, api


class MaintenanceWorkItem(models.AbstractModel):
    _name = 'report.maintenance_request_report.request_report'
    _description = "Maintenance Request Report"

    @api.model
    def _get_report_values(self, docids, data=None):
        record = self.env['maintenance.request'].browse(docids)
        return {
            'doc_ids': docids,
            'doc_model': 'maintenance.request',
            'docs': record,
            'data': data
        }
