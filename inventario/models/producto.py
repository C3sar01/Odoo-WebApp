# -*- coding: utf-8 -*-

from odoo import models, fields, api

#Modelo de los productos

class Producto(models.Model):
    _name = 'inventario.producto'

    name = fields.Char(string="Nombre", required=True)
    #duration = fields.Integer(string="Cantidad", required=True)
    

    #calculo_stock = fields.Integer(string = "Stock", compute =  "_calculo_stock")
    
    price = fields.Monetary('Precio', 'currency_id')
    currency_id = fields.Many2one('res.currency')
    date_contract = fields.Date(string = "Fecha de llegada")
    existencia = fields.Integer(compute='_calculo_stock')
    active = fields.Boolean('Disponibilidad', default=True)
    categorias_id = fields.Many2one('inventario.categoria_producto', string="Categoría")

    @api.one
    def _calculo_stock(self):
        compras = self.env['compra.detalle'].search([('producto_id','=', self.id)])
        total_compra = 0
        for compra in compras:
           total_compra += compra.cantidad
        
        
        ventas = self.env['venta.detalle_boleta'].search([('producto_id','=', self.id)])
        total_venta = 0
        for venta in ventas:
            total_venta += venta.cantidad
        
        self.existencia = total_compra - total_venta

        

#Modelo de las categorias de productos

class CategoriaProducto(models.Model):
    _name = 'inventario.categoria_producto'
    name = fields.Char(string="Nombre", required=True)
    producto_ids = fields.One2many(
        'inventario.producto',
        'categorias_id',
        string = 'Productos')

    total_productos = fields.Integer(string = "Total Productos", compute =  "_total_productos")

    
    @api.one
    def _total_productos(self):
        self.total_productos = len(self.producto_ids)
