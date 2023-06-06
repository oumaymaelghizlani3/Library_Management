# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models




class LibraryCustomer(models.Model):
    _name = "library.customer"

    _rec_name = 'l_name'
    f_name = fields.Char('first name')
    l_name = fields.Char('last name')
    aadress = fields.Text('adress')
    phone = fields.Char('phone')
    email = fields.Text()
    book_ids = fields.Many2many('library.book')
    location_ids = fields.Many2many('library.location')





