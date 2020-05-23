from odoo import fields, api, models, _


class attendance(models.Model):
    _name = 'ray.school.attendance'
    _description = 'attendance'

    name = fields.Char()