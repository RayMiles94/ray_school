from odoo import fields, api, models, _


class partent(models.Model):
    _name = 'ray.school.partent'
    _description = 'partent'

    name = fields.Char()