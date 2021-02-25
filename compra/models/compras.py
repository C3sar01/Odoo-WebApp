# -*- coding: utf-8 -*-

from odoo import models, fields, api
class Compra(models.Model):
    _name = 'compra.compras'
    fecha_compra= fields.Date()
    detalle_compra_ids = fields.One2many(
         'compra.detalle', 'compras_id', string="Detalle de la compra")


class DetalleCompra(models.Model):
    _name = 'compra.detalle'

    producto_id= fields.Many2one('inventario.producto', String="Producto")
    cantidad = fields.Integer(default=1)
    precio_unitario = fields.Integer()
    descuento= fields.Integer(default=0)
    sub_total = fields.Integer(String="Sub Total", compute="_sub_total")
    total = fields.Integer(String="Sub Total", compute="_total")
    compras_id= fields.Many2one('compra.compras', String="Numero de factura")

    @api.one
    def _sub_total(self):
        self.sub_total = (self.cantidad*self.precio_unitario)

    @api.one
    def _total(self):
        self.total = (self.sub_total - ((self.descuento/100) * self.sub_total)) 