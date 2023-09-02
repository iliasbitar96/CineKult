from odoo import models, fields


class Movie(models.Model):
    _name = 'movie'
    _description = 'movies'

    name = fields.Char('Movie')
    votes = fields.Many2one('vote')
    cast_ids = fields.Many2many('cast.member')
    genre = fields.Selection(
        [('horror', 'Horror'), ('thriller', 'Thriller'), ('animation', 'Animation'), ('drame', 'Drame')])
    duration = fields.Selection([('1h00', '1h00'), ('1h30', '1h30'), ('2h00', '2h00'), ('2h30', '2h30'), ('3h', '3h+')])
    description = fields.Text('Description')
    production = fields.Many2one('production', 'Production')
    creator_id = fields.Many2one('res.user')

    def search_movie(self, choice, post):
        if choice == 'actor':
            return self.search(['|', ('cast_ids.firstname', 'ilike', post.get('actor-search')),
                                ('cast_ids.lastname', 'ilike', post.get('actor-search'))])
        if choice == 'director':
            return self.search(['|', ('cast_ids.firstname', 'ilike', post.get('director-search')),
                                ('cast_ids.lastname', 'ilike', post.get('director-search'))])
        if choice == 'category':
            return self.search([('genre', 'ilike', post.get('category-select'))])
