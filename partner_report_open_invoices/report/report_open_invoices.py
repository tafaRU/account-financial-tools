# -*- coding: utf-8 -*-
# --------------------------------------------------------------------------
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2016-Today Serpent Consulting Services PVT. LTD.
#    (<http://www.serpentcs.com>)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>
#
# ---------------------------------------------------------------------------

import time

from openerp.report import report_sxw
from openerp.osv import osv


class report_open_invoices_parser(report_sxw.rml_parse):

    def __init__(self, cr, uid, name, context):
        super(report_open_invoices_parser, self).__init__(
            cr, uid, name, context=context)
        ids = context.get('active_ids')
        partner_obj = self.pool['res.partner']
        docs = partner_obj.browse(cr, uid, ids, context)

        addresses = self.pool['res.partner']._address_display(
            cr, uid, ids, None, None)
        self.localcontext.update({
            'docs': docs,
            'time': time,
            'message': self._message,
            'getLines': self._lines_get,
            'addresses': addresses,
        })
        self.context = context

    def _lines_get(self, partner):
        invoice_obj = self.pool['account.invoice']
        invoices_rec = invoice_obj.search(self.cr, self.uid, [('partner_id', '=', partner.id), (
            'account_id', '=', partner.property_account_receivable.id), ('state', '=', 'open')])
        move_lines = []
        for invoices in invoices_rec:
            for invoice_data in invoice_obj.browse(self.cr, self.uid, invoices):
                for move_line_data in invoice_data.move_id.line_id:
                    if move_line_data.date_maturity:
                        move_lines.append(move_line_data)
        return move_lines

    def _message(self, obj, company):
        company_pool = self.pool['res.company']
        message = company_pool.browse(self.cr, self.uid, company.id, {
                                      'lang': obj.lang}).open_invoices_msg
        return message.split('\n')


class report_open_invoices(osv.AbstractModel):
    _name = 'report.partner_report_open_invoices.report_open_invoices'
    _inherit = 'report.abstract_report'
    _template = 'partner_report_open_invoices.report_open_invoices'
    _wrapped_report_class = report_open_invoices_parser

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
