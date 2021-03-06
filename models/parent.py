from odoo import fields, api, models, _
from odoo.exceptions import ValidationError

class partent(models.Model):
    _name = 'ray.school.parent'
    _description = 'partent'

    name = fields.Char(string="Name", requried=True)
    email = fields.Char(string="Email", required=True)
    phone = fields.Char(string="Phone", required=True)
    mobile = fields.Char(string="Mobile", required=True)
    join_date = fields.Date(string="Joind Date", required=True)
    Status = fields.Boolean(string="Status", required=True)
    contact_id = fields.Many2one('res.partner', string="Contact profile")

    @api.constrains('name')
    def check_name(self):
        if len(self.name) > 45:
            raise ValidationError(_('name must be less than 45 chars'))

    @api.constrains('email')
    def check_name(self):
        if len(self.email) > 45:
            raise ValidationError(_('email must be less than 45 chars'))

    @api.constrains('phone')
    def check_name(self):
        if len(self.phone) > 45:
            raise ValidationError(_('phone must be less than 45 chars'))

    @api.constrains('mobile')
    def check_name(self):
        if len(self.mobile) > 45:
            raise ValidationError(_('mobile must be less than 45 chars'))