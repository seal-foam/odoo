# -*- coding: utf-8 -*-
"""
@author: Oscar González M. <oggonzalezm96@gmail.com>
@Date: 20/02/24
@project sealandfoam
@name: maintenance_request_extended
"""
from odoo import api, fields, models


class MaintenanceRequestExtended(models.Model):
    _inherit = 'maintenance.request'

    maintenance_type = fields.Selection(
        selection_add=[('predictive', "Predictivo")]
    )