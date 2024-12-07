# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api
from odoo.exceptions import ValidationError


class LibraryLocation(models.Model):
    _name = "library.location"
    _rec_name = "book_id"
    Date_location = fields.Date('the rental date')
    Date_retour = fields.Date('the return date')
    book_id = fields.Many2one('library.book')
    customer_ids = fields.Many2many('library.customer')

    @api.constrains('Date_retour')
    def _check_date_end(self):
        for location in self:
            if location.Date_retour < location.Date_location:
                raise ValidationError("The return date cannot be set in the past")