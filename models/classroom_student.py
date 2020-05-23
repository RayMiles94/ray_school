from odoo import fields, api, models, _


class classroom_student(models.Model):
    _name = 'ray.school.classroomstudent'
    _description = 'classroom student'

    name = fields.Char()