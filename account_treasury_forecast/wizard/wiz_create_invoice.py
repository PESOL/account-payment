# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

import odoo.addons.decimal_precision as dp
from odoo import models, fields, api


class WizCreateInvoice(models.TransientModel):
    _name = 'wiz.create.invoice'
    _description = 'Wizard to create invoices'

    partner_id = fields.Many2one("res.partner", string="Partner")
    journal_id = fields.Many2one("account.journal", string="Journal",
                                 domain=[("type", "=", "purchase")])
    description = fields.Char(string="Description")
    amount = fields.Float(string="Amount",
                          digits_compute=dp.get_precision('Account'))
    line_id = fields.Many2one("account.treasury.forecast.line.template",
                              string="Payment")

    @api.one
    def button_create_inv(self):
        invoice_obj = self.env['account.invoice']
        res_inv = invoice_obj.onchange_partner_id('in_invoice',
                                                  self.partner_id.id)
        values = res_inv['value']
        values['name'] = ('Treasury: ' + self.description + '/ Amount: ' +
                          str(self.amount))
        values['reference'] = ('Treasury: ' + self.description + '/ Amount: ' +
                               str(self.amount))
        values['partner_id'] = self.partner_id.id
        values['journal_id'] = self.journal_id.id
        values['type'] = 'in_invoice'
        invoice_id = invoice_obj.create(values)
        self.line_id.write({'invoice_id': invoice_id.id, 'paid': 1,
                            'journal_id': self.journal_id.id,
                            'partner_id': self.partner_id.id,
                            'amount': self.amount})
        return {'type': 'ir.actions.act_window_close'}
