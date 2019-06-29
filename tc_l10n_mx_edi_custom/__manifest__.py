# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'EDI for Mexico Custom',
    'version': '1.0',
    'category': 'Account',
    'depends': [
        'l10n_mx_edi',
    ],
    'data': [
        "views/l10n_mx_edi_report_invoice.xml",
    ],
    'installable': True,
    'auto_install': False,
}
