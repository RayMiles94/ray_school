# -*- coding: utf-8 -*-
{
    'name': "school",
    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",
    'description': """
        Long description of module's purpose
    """,
    'author': "raouf",
    'website': "http://www.raouf.com",
    'category': 'Uncategorized',
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