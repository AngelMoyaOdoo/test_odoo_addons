{
    'name': 'Project Task Urgency',
    'version': '19.0.1.0.0',
    'summary': 'Add urgency levels to tasks',
    'description': """
        This module adds an Urgency field to Project Tasks.
        - Levels: Low, Medium, High, Critical
        - Critical tasks are highlighted in red in list view.
    """,
    'author': 'OdooDevBot',
    'website': 'https://github.com/OdooDevBot/test_odoo_addons',
    'category': 'Project',
    'depends': ['project'],
    'data': [
        'views/project_task_views.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'AGPL-3',
}
