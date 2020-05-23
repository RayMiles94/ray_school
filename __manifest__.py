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
        'views/classroom_student.xml',
        'views/course.xml',
        'views/exam.xml',
        'views/exam_result.xml',
        'views/exam_type.xml',
        'views/partent.xml',
        'views/student.xml',
        'views/teacher.xml',
        'views/grade.xml',
        'views/menu.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'auto_install':False,
    'application':True,
    'css': [],
    'sequence':10
}