# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api


class LibraryAuthor(models.Model):
    _name = "library.author"
    _rec_name = 'l_name'
    f_name = fields.Char('first name')
    l_name = fields.Char('last name')
    book_ids = fields.Many2many('library.book')

    @api.model
    def year_selection(self):
       year = 1900 # replace 2000 with your a start year
       year_list = []
       while year != 2030: # replace 2030 with your end year
         year_list.append((str(year), str(year)))
         year += 1
       return year_list

    year = fields.Selection(
    year_selection,
    string="Year",
    default="2019", # as a default value it would be 2019
)