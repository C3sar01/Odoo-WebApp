# -*- coding: utf-8 -*-

from odoo import models, fields, api

#Modelo de la clase boleta

class Boleta(models.Model):
     _name = 'venta.boleta'

     cliente= fields.Char(string="Nombre del cliente", required=True)
     fecha= fields.Date()
     
     direccion= fields.Char(string="Dirección", required=True)
     vendedor= fields.Char (string="Vendedor", required=True)
 
     detalle_boleta_ids = fields.One2many(
         'venta.detalle_boleta', 'boleta_id', string="Detalle de la venta")

#Modelo de la clase detalle_boleta

class DetalleBoleta(models.Model):
    _name = 'venta.detalle_boleta'

    producto_id= fields.Many2one('inventario.producto', String="Producto")
    cantidad = fields.Integer(default=1)
    precio_unitario = fields.Integer()
    descuento= fields.Integer(default=0)
    sub_total = fields.Integer(String="Sub Total", compute="_sub_total")
    total = fields.Integer(String="Sub Total", compute="_total")
    boleta_id= fields.Many2one('venta.boleta', String="Boleta")

    @api.one
    def _sub_total(self):
        self.sub_total = (self.cantidad*self.precio_unitario)

    @api.one
    def _total(self):
        self.total = (self.sub_total - ((self.descuento/100) * self.sub_total))   