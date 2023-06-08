# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api


class LibraryBook(models.Model):
    _name = "library.book"
    _rec_name = 'Title'

    Title = fields.Char('Title')

    Editors = fields.Char('Editors')

    ISBN = fields.Integer('ISBN')

    customer_ids = fields.Many2many('library.customer')
    author_ids = fields.Many2many('library.author')
    location_ids = fields.One2many('library.location', 'book_id')

    @api.model
    def Date_selection(self):
      Date = 1900 # replace 1900 with your a start year
      Date_list = []
      while Date != 2030: # replace 2030 with your end year
        Date_list.append((str(Date), str(Date)))
        Date += 1
      return Date_list

    Date = fields.Selection(
    Date_selection,
    string="Date",
    default="2019", # as a default value it would be 2019
)