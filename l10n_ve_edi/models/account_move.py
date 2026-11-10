# -*- coding: utf-8 -*-
##############################################################################
# Author: Mastercore Sinapsys Global®
# Copyright: 2019-Present.
# License OPL-1 (Odoo Proprietary License v1.0)
# See https://www.odoo.com/documentation/master/legal/licenses.html
#
#
##############################################################################
from odoo import api, models


class AccountMove(models.Model):
    _inherit = 'account.move'

    @api.depends('journal_id', 'journal_id.l10n_ve_seniat_ws')
    def _compute_l10n_ve_vat_book_emission(self):
        super()._compute_l10n_ve_vat_book_emission()
        for move in self:
            if move._get_default_l10n_ve_vat_book_emission() == 'digital':
                move.l10n_ve_vat_book_emission = 'digital'

    def _get_default_l10n_ve_vat_book_emission(self):
        emission = super()._get_default_l10n_ve_vat_book_emission()
        if emission != 'fiscal' and self.move_type in ('out_invoice', 'out_refund') and (
            self.journal_id.type == 'sale' and self.journal_id.l10n_ve_seniat_ws
        ):
            return 'digital'
        return emission
