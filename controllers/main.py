# -*- coding: utf-8 -*-
# create resful api for school application
from odoo import http
from odoo import api, models, fields, _
from odoo.http import content_disposition, dispatch_rpc, request, \
    serialize_exception as _serialize_exception, Response
from odoo.exceptions import AccessError, UserError, AccessDenied
import json


class rayschool_api(http.Controller):

    @http.route("/students", type='http', auth="none")
    def getstudents(self, **kw):
        students = request.env['ray.school.student'].search([])
        print(students)
        reponse = []
        for student in students:
            reponse.append(student.name)
        #reponse = json.dumps({ reponse:  reponse  })
        return json.dumps({ "ok" :"ok"  })