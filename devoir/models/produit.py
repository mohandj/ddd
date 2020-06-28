# coding: utf-8

from odoo import fields, models

class ProductTemplate(models.Model):
    _inherit = 'product.template'


    marque_id = fields.Many2one('modéle.devoir2', string="marques associer aux produit")

