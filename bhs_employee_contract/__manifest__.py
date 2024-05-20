# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Employee Contract Notification',
    'version': '1.0',
    'category': 'HR',
    'sequence': 335,
    'summary': "Distinguish contract is gross or net and warn employees whose contracts are about to expire.",
    'description': """
        A product of Bac Ha Software allows to distinguish contract is gross or net
        and warn employees whose contracts are about to expire.
    """,
    'website': 'https://bachasoftware.com',
    'depends': ['hr_contract', 'hr_holidays'],
    'data': [
        'views/hr_contract_history_views.xml',
        'views/hr_leave_views_dashboard.xml',
        'views/hr_leave_views_kanban.xml',
    ],
    'images': ['static/description/banner.gif'],
    'installable': True,
    'auto_install': False,
    'application': True,
    'assets': {
    },
    'license': 'LGPL-3'
}
