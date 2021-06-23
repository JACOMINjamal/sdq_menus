# -*- coding: utf-8 -*-
{
    'name': "All in One Reports Menus",

    'summary': """
     Adds All In One sale,Purchase,P.O.S Analyses""",

    'description': """
        All In One sale,Purchase,P.O.S Analyses
    """,

    'author': "Mohamed Sadiq",


    # Categories can be used to filter modules in modules listing
    # for the full list
    'category': 'Project Management',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale', 'purchase', 'point_of_sale', 'account'],

    # always loaded
    'data': [
        'views/sale.xml',
        'views/stock_menu.xml',
        'views/purchase_menu.xml',
        'views/pos_reports_menu.xml',
        'views/facturation.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
}