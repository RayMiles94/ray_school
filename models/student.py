from odoo import fields, api, models, _


class student(models.Model):
    _name = 'ray.school.student'
    _description = 'student'

    name = fields.Char()