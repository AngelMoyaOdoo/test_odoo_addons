from odoo import models, fields

class ProjectTask(models.Model):
    _inherit = 'project.task'

    urgency = fields.Selection([
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ('critical', 'Critical'),
    ], string='Urgency', default='medium', required=True, tracking=True)
