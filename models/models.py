# -*- coding: utf-8 -*-

from odoo import models, fields, api


class school(models.Model):
    _name = 'school.school'

    name = fields.Char(string='school name')
    adresse = fields.Char(string='school adresse')

