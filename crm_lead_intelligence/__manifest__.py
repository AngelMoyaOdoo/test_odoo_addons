{
    'name': 'CRM Lead Intelligence',
    'version': '19.0.1.0.0',
    'summary': 'Add competitor tracking, urgency, and qualitative scoring to leads.',
    'description': """
        This module extends CRM Leads with new fields for strategic intelligence:
        - Competitor tracking (Many2one to crm.lead.competitor).
        - Urgency level (Low, Medium, High, Critical).
        - Estimated Budget (different from Expected Revenue).
        - Product Fit Score (1-5 stars).
    """,
    'author': 'OdooDevBot',
    'website': 'https://github.com/OdooDevBot/test_odoo_addons',
    'category': 'Sales/CRM',
    'depends': ['crm'],
    'data': [
        'security/ir.model.access.csv',
        'views/crm_competitor_views.xml',
        'views/crm_lead_views.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'AGPL-3',
}
