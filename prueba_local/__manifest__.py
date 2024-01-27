# -*- coding: utf-8 -*-
{
    'name': 'Prueba Local',
    'description': """ Modulo de Prueba """,
    'version': '1.0.0',
    'category': 'Account',
    'author': "Ismael Castillo - ismaonline2000@gmail.com",
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/res_partner.xml',
        'views/prueba.xml'
    ],
    'application': True,
    'installable': True,
    'auto_install': False
}