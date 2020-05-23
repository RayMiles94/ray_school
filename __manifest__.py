# -*- coding: utf-8 -*-
{
    'name': "Ray School",
    'summary': """
    Odoo School application     
    """,
    'description': """
        Odoo School application
    """,
    'author': "RayMiles94",
    'website': "https://github.com/RayMiles94/ray_school",
    'category': 'School',
    'version': '1.0',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/attendance.xml',
        'views/classroom.xml',
        'views/course.xml',
        'views/exam.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'auto_install':False,
    'application':True,
    'css': [],
    'sequence':10
}