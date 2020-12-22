# -*- coding: utf-8 -*-
{
    'name': "inventario",

    'summary': """
        Módulo de odoo""",

    'description': """
        Módulo que permite la gestión de inventario de la empresa Pegasus
    """,

    'author': "César Soto Rojas",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Inventary',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/view_producto.xml',
        #'views/templates.xml',
    ],
    
}