
from odoo import models, fields


class Student(models.Model):
    _name = 'student.student'
    _description = 'Student'

    name = fields.Char(string='Student Name', required=True)
    student_id = fields.Char(string='Student ID')
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')
    age = fields.Integer(string='Age')

    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
    ], string='Gender')

    active = fields.Boolean(default=True)
    image = fields.Image(string='Student Photo')
    status = fields.Selection([
        ('draft', 'New'),
        ('enrolled', 'Enrolled'),
        ('graduated', 'Graduated'),
    ], string='Status', default='draft')

    rating = fields.Selection([
        ('0', 'Poor'),
        ('1', 'Average'),
        ('2', 'Good'),
        ('3', 'Very Good'),
        ('4', 'Excellent'),
        ('5', 'Outstanding'),
    ], string='Rating', default='0')