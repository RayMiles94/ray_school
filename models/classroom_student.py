from odoo import fields, api, models, _
from odoo.exceptions import ValidationError


class classroom_student(models.Model):
    _name = 'ray.school.classroomstudent'
    _description = 'classroom student'

    classromm_id = fields.Many2one('ray.school.classroom', string="Classroom", required=True)
    student_id = fields.Many2one('ray.school.student', string="Students", required=True)