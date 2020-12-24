# -*- coding: utf-8 -*-
{
    'name': "compra",

    'summary': """
        Proyecto desarrollo web""",

    'description': """
        Sistema que permite realizar compras  y emitir órdenes para la reposición del inventario, 
        además de permitir mostrar la cantidad a comprar, el costo y el nombre de cada producto.
    """,

    'author': "Utalca",
    'website': "http://www.utalca.cl",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Purchase',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
         'security/ir.model.access.csv',
         'views/view_purchase.xml',
        #'views/templates.xml',
    ],
    # only loaded in demonstration mode
  
    
}