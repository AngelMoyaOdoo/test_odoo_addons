from odoo import models, fields

class CrmLeadCompetitor(models.Model):
    _name = 'crm.lead.competitor'
    _description = 'CRM Lead Competitor'
    _order = 'name'

    name = fields.Char(string='Competitor Name', required=True, translate=True)
    website = fields.Char(string='Website')
    active = fields.Boolean(default=True)
