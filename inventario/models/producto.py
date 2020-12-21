# -*- coding: utf-8 -*-

from odoo import models, fields, api

#Modelo de los productos

class Producto(models.Model):
    _name = 'inventario.producto'

    name = fields.Char(string="Nombre", required=True)
    duration = fields.Integer(string="Cantidad", required=True)
    price = fields.Monetary('Precio', 'currency_id')
    currency_id = fields.Many2one('res.currency')
    date_contract = fields.Date(string = "Fecha de llegada")
    active = fields.Boolean('Disponibilidad', default=True)

    categorias_id = fields.Many2one('inventario.categoria_producto', string="Categoría")

#Modelo de las categorias de productos

class CategoriaProducto(models.Model):
    _name = 'inventario.categoria_producto'
    name = fields.Char(string="Nombre", required=True)
    poliza_ids = fields.One2many(
        'inventario.producto',
        'categorias_id',
        string = 'Productos')

    total_productos = fields.Integer(string = "Total Productos", compute =  "_total_productos")

    
    @api.one
    def _total_productos(self):
        self.total_productos = len(self.poliza_ids)

