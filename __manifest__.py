# -*- coding: utf-8 -*-
{
    'name': "school",
    'summary': """
    Odoo School application     
    """,
    'description': """
        Odoo School application
    """,
    'author': "raouf",
    'website': "http://www.raouf.com",
    'category': 'School',
    'version': '1.0',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'auto_install':False,
    'application':True,
    'css': [],
    'sequence':10
}