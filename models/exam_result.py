from odoo import fields, api, models, _


class exam_result(models.Model):
    _name = 'ray.school.exam.result'
    _description = 'exam.result'

    name = fields.Char()