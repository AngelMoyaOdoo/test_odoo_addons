# -*- coding: utf-8 -*-
from odoo import models, fields, api


class AccountAnalyticLine(models.Model):
    _inherit = 'account.analytic.line'

    product_categ_id = fields.Many2one(
        comodel_name='product.category',
        string='Product Category',
        related='product_id.categ_id',
        store=True,
        readonly=True,
        help='Product category from the related product',
    )
