from odoo import fields, api, models, _
from odoo.exceptions import ValidationError


class course(models.Model):
    _name = 'ray.school.course'
    _description = 'course'

    name = fields.Char(string='course name', required=True)
    desc = fields.Char(string='Description', required=True)
    course = fields.Binary(string="Course")
    grade_id = fields.Many2one('ray.school.grade', string="Grade", required=True)

    @api.constrains('name')
    def check_name(self):
        if len(self.name)>45:
            raise ValidationError(_('name must be less than 45'))

    @api.constrains('desc')
    def check_name(self):
        if len(self.desc) > 45:
            raise ValidationError(_('descrption must be less than 45'))