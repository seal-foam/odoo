# -*- coding: utf-8 -*-
{
    'name': "Drasi | drs_mrp",

    'summary': """
        MRP customizations.
    """,

    'description': """
        This module add customizations to MRP workflow.
    """,

    'author': "Drasi Consulting",
    'website': "https://www.drasi.odoo.com",

    'category': 'MRP',
    'version': '16.0.1.0.0',

    'depends': ['mrp'],

    'data': [
        'views/mrp_production_report.xml',
        'views/mrp_production_views.xml',
    ],
}
