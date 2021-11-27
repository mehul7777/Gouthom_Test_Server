# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Goutham Project',
    'version': '1.0',
    'author': 'Mehul Darji',
    'category': 'Project',
    'summary': 'Goutham Project',
    'description': "For Test Server",
    'website': 'https://www.odoo.com',
    'depends': [
        'base', 'product'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/Inherit_Template_view.xml',
        'wizard/Products_Import_view.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
