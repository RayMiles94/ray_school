from odoo import fields, api, models, _


class course(models.Model):
    _name = 'ray.school.course'
    _description = 'course'

    name = fields.Char()