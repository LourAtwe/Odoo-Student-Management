
{
    'name': 'Student Management',
    'version': '1.0',
    'category': 'Education',
    'summary': 'Student Management System',
    'author': 'Lour',

    'depends': ['base'],

    'data': [
        'security/ir.access.csv',
        'views/student_views.xml',
        'views/student_actions.xml',
        'views/student_menus.xml',
    ],

    'installable': True,
    'application': True,
}
