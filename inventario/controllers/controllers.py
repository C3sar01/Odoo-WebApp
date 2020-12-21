# -*- coding: utf-8 -*-
from odoo import http


# class Seguros(http.Controller):
#     @http.route('/seguros/seguros/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/seguros/seguros/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('seguros.listing', {
#             'root': '/seguros/seguros',
#             'objects': http.request.env['seguros.seguros'].search([]),
#         })

#     @http.route('/seguros/seguros/objects/<model("seguros.seguros"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('seguros.object', {

#             'object': obj
#         })