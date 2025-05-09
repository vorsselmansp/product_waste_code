# -*- coding: utf-8 -*-
{
    'name': "product_waste_code",
    'version': '0.1',
    'category': 'Equeens',
    'summary': "App to manage European Waste Codes for ptoducts",
    'description': """
Long description of module's purpose
    """,
    'website': "https://www.attiesatelier.be",
    'author': "Atti's Atelier",

    # A EWC list can be found here https://wikiwaste.org.uk/index.php/Category:EWC_Codes
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'application': True,
    'installable': True,

    # any module necessary for this one to work correctly
    'depends': ['base','web'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/data.xml',
        'views/views.xml',
        'views/myview.xml',
        'views/templates.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'product_waste_code/static/src/**/*',
        ],
    },
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'license': 'LGPL-3',
}

