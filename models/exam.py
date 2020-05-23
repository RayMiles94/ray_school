from odoo import fields, api, models, _
from odoo.exceptions import ValidationError

class exam(models.Model):
    _name = 'ray.school.exam'
    _description = 'exam'

    name = fields.Char(string="Exam Name", required=True)
    start_date = fields.Date(string="Date", required=True)
    exam_type = fields.Many2one('ray.school.examtype', string="Exam type")

    @api.constrains('name')
    def check_name(self):
        if len(self.name) > 45:
            raise ValidationError(_('name must less than 50 chars'))