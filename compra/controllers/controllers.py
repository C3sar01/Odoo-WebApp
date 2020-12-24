# -*- coding: utf-8 -*-
from odoo import http

# class Compra(http.Controller):
#     @http.route('/compra/compra/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/compra/compra/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('compra.listing', {
#             'root': '/compra/compra',
#             'objects': http.request.env['compra.compra'].search([]),
#         })

#     @http.route('/compra/compra/objects/<model("compra.compra"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('compra.object', {
#             'object': obj
#         })