{
    'name': 'task_1912',
    'version': '15.0.1.0.1',
    'category': 'task eCommerce',
    'summary': 'task eCommerce',
    'sequence': 1,
    'description': """
This module contains all the common features of eCommerce.
    """,
    'depends': ['sale_management','stock','website_sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/res_config_settings_views.xml',
        'views/shop_inherit_views.xml',
        'views/sale_order_inherit_views.xml',
        'views/preferred_time_views.xml',
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,

    'license': 'LGPL-3',
'assets': {
        'web.assets_frontend': [
            'task_1912/static/src/js/set_time.js',
        ]
    }
}
