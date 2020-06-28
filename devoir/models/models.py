# -*- coding: utf-8 -*-

 from odoo import models, fields, api


class devoir(models.Model):
    _name = 'modéle.devoir2'
    _rec_name = 'titre'
    """ methode pour recupérer le nombre de produit d'une marque  """

    def get_produit_count(self):
        count = self.env['devoir.produit'].search_count([('marque_id', '=', self.id)])
        self.produit_count = count

    """ les champs  """
    name = fields.Char(string="Nom")
    code = fields.Integer(string="code" )
    produit_count = fields.Integer(string='count', compute='get_produit_count')

