# -*- coding: utf-8 -*-

from odoo import models, fields, api
class purchase(models.Model):
    _name = 'compra.purchase'
    name = fields.Char(string = "Nombre", required=True)
    duration = fields.Integer(string="Plazo", required=True)
    cost = fields.Float(string="Costo")
    date = fields.Date("Fecha")