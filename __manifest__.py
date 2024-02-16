
{
    'name': 'Bus Travel App',
    'version': '1.0.0.0.0',
    'author': 'Álvaro Roldán',
    'maintainer': 'Álvaro Roldán',
    'website': 'www.google.es',
    'license': 'AGPL-3',
    'category': 'Administration',
    'summary': 'Application oriented to the administration of a Bus agency service',
    'depends': ['base'],
    'security':[
            'security/ir.model.access.csv',
            'security/driver_security.xml',
            'security/travel_security.xml',
            'security/traveller_security.xml',
            'security/vehicle_security.xml',
            ],
    'data':[
        'views/driver_view.xml',
        'views/travel_view.xml',
        'views/traveller_view.xml',
        'views/vehicle_view.xml',
        ],
    'application' : True,
    'instalable' : True,
    'auto_install' : False,
    'images' : [
        'static/description/icon.png'
    ]               
}
