from odoo import fields, api, models, _
from odoo.exceptions import ValidationError

YEAR = [
    ('2010','2010'),
    ('2011','2011'),
    ('2012','2012'),
    ('2013','2013'),
    ('2014','2014'),
    ('2015','2015'),
    ('2016','2016'),
    ('2017','2017'),
    ('2018','2018'),
    ('2019','2019'),
    ('2020','2020'),
    ('2021','2021'),
    ('2022','2022'),
    ('2023','2023'),
    ('2024','2024'),
    ('2025','2025'),
]


class classroom(models.Model):
    _name = 'ray.school.classroom'
    _description = 'ClassRoom'

    name= fields.Char('')
    year = fields.Selection(string="Year", selection=YEAR, required=True)
    grade_id = fields.Many2one('ray.school.grade', string="Grade")
    section = fields.Selection(selection=[('MATH', 'math'), ('PHY', 'phy'), ('science', 'science'), ('computer', 'computer')], default='math', required=True)
    status = fields.Boolean(string="Status")
    remarks = fields.Text(string="Remark", required=True)
    teacher_ids = fields.One2many('ray.school.teacher', 'class_id', required=True)
    students_ids = fields.One2many('ray.school.student', 'class_id', required=True)

    @api.model
    def create(self, values):
        values['name'] = 'CLASS/' + str(len(self.search([])))
        return super(classroom, self).create(values)
