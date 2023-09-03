from odoo import models, fields


class Vote(models.Model):
    _name = 'vote'
    _description = 'up and down votes for the movies'

    up_votes = fields.Integer('Up votes')
    down_votes = fields.Integer('Down votes')
    movie_id = fields.Many2one('movie')
    voter = fields.Many2one('res.partner')
