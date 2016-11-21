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

from openerp import fields, models


class ResCompany(models.Model):
    _inherit = "res.company"

    open_invoices_msg = fields.Text('Open Invoices Message', translate=True,
                                    default='''Dear Sir / Madam,

From our accounting records it appears that some payments on your account
is still open. Please check the details attached. If payment should already
have been paid, please do not consider this. 
If not, I pray you stand for the amount indicated below. If there are
any questions or requests about it, please do not hesitate to contact us.
Thank you in advance for your cooperation.
Best Regards,''')
