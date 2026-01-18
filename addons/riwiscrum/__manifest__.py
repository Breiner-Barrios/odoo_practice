{
    'name': 'Riwiscrum',
    'version': '18.0.1.0.0',
    'category': 'Uncategorized',
    'summary': 'Modulo creado para Odoo 18',
    'description': 'Descripcion de riwiscrum',
    'author': 'Breiner',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',

        'sequences/ir_sequence_data.xml',
        'views/riwiscrum_views.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}