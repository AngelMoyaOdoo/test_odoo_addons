# -*- coding: utf-8 -*-
{
    'name': 'Account Analytic Product Category',
    'version': '19.0.1.0.0',
    'category': 'Accounting',
    'summary': 'Add product category grouping in analytic accounting reports',
    'description': """
Account Analytic Product Category
=================================
This module adds the ability to group by product category in analytic accounting reports.

Features:
---------
* Adds related field product_categ_id to analytic lines
* Enables grouping by product category in pivot and graph views
* Adds search filters for product category
    """,
    'author': 'OdooDevBot',
    'website': '',
    'license': 'LGPL-3',
    'depends': [
        'account',
        'account_analytic_online',
        'product',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/account_analytic_line_views.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
