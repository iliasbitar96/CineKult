from odoo import models, fields


class Production(models.Model):
    _name = 'production'
    _description = 'The production companies'

    name = fields.Char('Production')
