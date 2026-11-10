# -*- coding: utf-8 -*-
##############################################################################
# Author: Mastercore Sinapsys Global®
# Copyright: 2019-Present.
# License OPL-1 (Odoo Proprietary License v1.0)
# See https://www.odoo.com/documentation/master/legal/licenses.html
#
#
##############################################################################
{
    'name': 'Facturación electrónica Venezuela',
    'summary': 'Identificación de facturas digitales por diario.',
    'description': """
Configura diarios de ventas para asignar la modalidad Factura digital a sus
facturas y notas de crédito. No realiza conexiones con servicios web externos.
    """,
    'version': '18.0.1.0.0',
    'category': 'Accounting/Localizations',
    'countries': ['ve'],
    'author': 'Mastercore Sinapsys Global',
    'website': 'https://sinapsys.global',
    'license': 'OPL-1',
    'depends': ['account_accountant', 'l10n_ve_vat_ledger'],
    'data': ['views/account_journal_views.xml'],
    'installable': True,
    'auto_install': False,
    'application': False,
}
