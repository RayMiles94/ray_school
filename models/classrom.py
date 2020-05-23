from odoo import fields, api, models, _


class classroom(models.Model):
    _name = 'ray.school.classroom'
    _description = 'ClassRoom'

    name = fields.Char()
