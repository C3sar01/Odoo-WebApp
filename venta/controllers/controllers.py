# -*- coding: utf-8 -*-
from odoo import http

# class Venta(http.Controller):
#     @http.route('/venta/venta/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/venta/venta/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('venta.listing', {
#             'root': '/venta/venta',
#             'objects': http.request.env['venta.venta'].search([]),
#         })

#     @http.route('/venta/venta/objects/<model("venta.venta"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('venta.object', {
#             'object': obj
#         })