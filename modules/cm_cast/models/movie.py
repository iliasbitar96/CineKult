from odoo import models, fields


class Movie(models.Model):
    _name = 'movie'
    _description = 'movies'

    name = fields.Char('Movie')
    votes = fields.Many2one('vote')
    cast_ids = fields.Many2many('cast.member')
    genre = fields.Selection([('horror', 'Horror'), ('thriller', 'Thriller'), ('animation', 'Animation'), ('drame', 'Drame')])
    duration = fields.Selection([('1h00', '1h00'), ('1h30', '1h30'), ('2h00', '2h00'), ('2h30', '2h30'), ('3h', '3h+')])
    description = fields.Text('Description')
    creator_id = fields.Many2one('res.user')
