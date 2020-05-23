from odoo import fields, api, models, _
from odoo.exceptions import ValidationError


class exam_result(models.Model):
    _name = 'ray.school.exam.result'
    _description = 'exam.result'

    exam_id = fields.Many2one('ray.school.exam', string="Exam name", required=True)
    student_id = fields.Many2one('ray.school.student', string="Student name", required=True)
    course_id = fields.Many2one('ray.school.student', string="Course name", required=True)
    mark = fields.Float(string="mark")

    @api.constrains('mark')
    def check_mark(self):
        if self.mark > 20:
            raise ValidationError(_("mark must be less than 20"))
