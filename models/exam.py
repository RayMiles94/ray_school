from odoo import fields, api, models, _


class exam(models.Model):
    _name = 'ray.school.exam'
    _description = 'exam'

    name = fields.Char()