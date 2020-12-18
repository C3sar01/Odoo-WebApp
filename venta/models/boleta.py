# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Boleta(models.Model):
     _name = 'venta.boleta'

     fecha= fields.Date()
     subtotal= fields.Integer(default=0)
     descuento = fields.Float(default=0)
     total= fields.Float(default=0)

     detalle_boleta_ids = fields.One2many(
         'venta.detalle_boleta', 'boleta_id', string="Detalle de la venta")

class DetalleBoleta(models.Model):
    _name = 'venta.detalle_boleta'
    cantidad = fields.Integer(default=1)
    precio = fields.Integer()
    sub_total = fields.Integer(String="Sub Total", compute="sub_total")
    descuento= fields.Integer(default=0)
    total = fields.Integer(string="Total", compute="total_detalle_boleta")
    boleta_id= fields.Many2one('venta.boleta', String="Boleta")
    
    @api.one
    def _sub_total(self):
        self.sub_total = (self.cantidad*self.precio)

    @api.one
    def _total(self):
        self.total = (self.sub_total - ((self.descuento/100) * self.sub_total))   