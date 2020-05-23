from odoo import fields, api, models, _


class garde(models.Model):
    _name = 'ray.school.grade'
    _description = 'Grade'

    name = fields.Char()