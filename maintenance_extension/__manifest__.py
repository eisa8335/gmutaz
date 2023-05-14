# -*- coding: utf-8 -*-
{
    'name': "Maintenance Extension",
    'version': "16.0.1",
    'author': 'Eisa Ahmed',
    'website': 'https://www.fiverr.com/users/eisaahmed63',
    'description': """This module will add custom Equipment information and Extend the functionality of Maintenance Work Items.""",
    'summary': 'This module will add custom Equipment information and Extend the functionality of Maintenance Work Items.',
    'category': 'Customizations',
    'maintainer': 'Eisa Ahmed',
    'depends': ['base', 'product', 'maintenance', 'contacts', 'hr','maintenance_request_report', 'stock'],
    'data': [
        'security/ir.model.access.csv',
        'data/data.xml',
        'data/ir_cron_data.xml',
        'views/maintenance_extension.xml',
        'views/equipment_view.xml',
        'views/part_view.xml',
    ],
    'license': 'AGPL-3',
    'application': True
}
