from odoo import models, fields


class Vote(models.Model):
    _name = 'vote'
    _description = 'up and down votes for the movies'

    vote_type = fields.Boolean('vote')
    movie_id = fields.Many2one('movie')
    user_id = fields.Many2one('res.partner')
