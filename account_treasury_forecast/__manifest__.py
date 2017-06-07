# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    'name': 'Account Treasury Forecast',
    'version': '10.0.1.0.0',
    'category': 'Accounting',
    'author': 'Odoo Community Association (OCA), '
              'AvanzOSC, '
              'Serv. Tecnol. Avanzados - Pedro M. Baeza, ',
    'website': 'http://www.odoomrp.com',
    'license': 'AGPL-3',
    'depends': [
        'account',
        'purchase',
    ],
    'data': [
        'security/ir.model.access.csv',
        'wizard/wiz_create_invoice_view.xml',
        'views/account_treasury_forecast_view.xml',
        'views/account_treasury_forecast_template_view.xml',
    ],
    'installable': True,
}
