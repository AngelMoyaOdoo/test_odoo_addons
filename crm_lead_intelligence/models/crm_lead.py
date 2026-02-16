from odoo import models, fields

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    competitor_id = fields.Many2one('crm.lead.competitor', string='Main Competitor', tracking=True)
    urgency_level = fields.Selection([
        ('0', 'Low'),
        ('1', 'Medium'),
        ('2', 'High'),
        ('3', 'Critical'),
    ], string='Urgency Level', default='1', tracking=True)
    estimated_budget = fields.Monetary(string='Estimated Budget', currency_field='company_currency', tracking=True)
    product_fit_score = fields.Integer(string='Product Fit Score', default=0, help="Qualitative score from 1 to 5")
