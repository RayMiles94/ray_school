from odoo import fields, api, models, _
from  odoo.exceptions import ValidationError

class garde(models.Model):
    _name = 'ray.school.grade'
    _description = 'Grade'

    name = fields.Char(string="Grade Name", required=True)
    desc = fields.Char(string="Description", required=True)


    @api.constrains('name')
    def check_name(self):
        if(len(self.name)>45):
            raise ValidationError(_('name must less than 50 chars'))

    @api.constrains('desc')
    def check_name(self):
        if (len(self.desc) > 45):
            raise ValidationError(_('desc must less than 50 chars'))