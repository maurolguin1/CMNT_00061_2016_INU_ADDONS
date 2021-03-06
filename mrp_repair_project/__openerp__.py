# -*- coding: utf-8 -*-
# (c) 2014 Daniel Campos <danielcampos@avanzosc.es>
# (c) 2015 Pedro M. Baeza - Serv. Tecnol. Avanzados
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

{
    "name": "MRP Repair Project Link",
    "summary": "Link repair with projects",
    "version": "8.0.1.2.0",
    "depends": [
        "mrp_analytic",
        "project",
        "project_timesheet",
        "mrp_project",
    ],
    'license': 'AGPL-3',
    "images": [],
    "author": "OdooMRP team,"
              "AvanzOSC,"
              "Serv. Tecnol. Avanzados - Pedro M. Baeza,"
              "Antiun Ingeniería S.L.,"
              "Odoo Community Association (OCA)",
    "category": "Manufacturing",
    'data': [
        "views/mrp_repair_view.xml",
        "views/project_task_view.xml",
    ],
    'installable': True,
    'auto_install': False,
}
