from odoo import fields, api, models, _


class exam_type(models.Model):
    _name = 'ray.school.examtype'
    _description = 'examtype'

    name = fields.Char(string="Grade Name", required=True)
    desc = fields.Char(string="Description", required=True)