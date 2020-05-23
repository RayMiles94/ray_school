from odoo import fields, api, models, _


class teacher(models.Model):
    _name = 'ray.school.teacher'
    _description = 'teacher'

    name = fields.Char()