{
    'name': "Classic Movies",
    "summary": "All the cast logic",
    'version': '1.0',
    'depends': [],
    'installable': True,
    'data': [
        'security/ir.model.access.csv',
        'views/movie.xml',
        'views/cast_members.xml',
        'static/xml/main_page.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'cm_cast/static/css/main_page.css',
        ],
    },
}
