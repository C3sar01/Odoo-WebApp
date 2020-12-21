# -*- coding: utf-8 -*-
{

    'name': "Inventario",

    'summary': """
        Módulo en odoo""",

    'description': """
        Aplicación que permite administrar el inventario de una empresa de limpieza
    """,

    'author': "César Soto",
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
         'views/view_poliza.xml',
        # 'views/templates.xml',
    ],
    

}