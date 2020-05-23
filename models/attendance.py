from odoo import fields, api, models, _
from odoo.exceptions import ValidationError


class attendance(models.Model):
    _name = 'ray.school.attendance'
    _description = 'attendance'

    student_id = fields.Many2one('ray.school.student', string="Student", required=True)
    status = fields.Boolean(string="Status", required=True)
    remark = fields.Text(string="Remark")