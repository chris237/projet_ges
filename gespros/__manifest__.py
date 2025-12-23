# -*- coding: utf-8 -*-
{
    'name': 'Gestion Operations',
    'version': '1.0.0',
    'category': 'Perso',
    'summary': 'Module',
    'description': """
        Module 
    """,
    'author': 'Christian Ferdinand fotie201@gmail.com',
    'website': 'https://',
    'depends': ['base', 'account', 'hr_expense', 'mail', 'fleet'],
    'data': [
        'security/security_rules.xml',
        'security/ir.model.access.csv',
        'report/project_expense_report.xml',
        'views/projet.xml',
        'views/account_move.xml',
        'views/cate_expense.xml',
        'views/menus.xml',
    ],
    'images': [
        'static/description/brains.png',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
