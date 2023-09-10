from odoo import models, fields, api


class Movie(models.Model):
    _name = 'movie'
    _description = 'movies'

    name = fields.Char('Movie')
    vote_ids = fields.One2many('vote', 'movie_id')
    cast_ids = fields.Many2many('cast.member', string="Actors", domain="[('member_type', '=', 'actor')]")
    genre = fields.Selection(
        [('action', 'Action'), ('animation', 'Animation'), ('aventure', 'Aventure'), ('comédie', 'Comédie'),
         ('drame', 'Drame'), ('fantastique', 'Fantastique'), ('guerre', 'Guerre'), ('historique', 'Historique'),
         ('horreur', 'Horreur'), ('policier', 'Policier'), ('romance', 'Romance'),
         ('science_fiction', 'Science fiction'), ('thriller', 'Thriller'), ('western', 'Western')])
    duration = fields.Selection([('n1', '-1h00'), ('1h00', '1h00'), ('1h30', '1h30'), ('2h00', '2h00'),
                                 ('2h30', '2h30'), ('3h', '3h'), ('p3h', '+3h')])
    description = fields.Text('Description')
    production = fields.Many2one('production', 'Production')
    creator_id = fields.Many2one('res.user')
    year = fields.Integer('Year')
    director = fields.Many2one('cast.member', domain="[('member_type', '=', 'director')]")
    total_votes = fields.Integer('Votes', compute='compute_total_votes')

    @api.depends('vote_ids')
    def compute_total_votes(self):
        for record in self:
            vote_ids = record.vote_ids
            record.total_votes = len(vote_ids.filtered(lambda x: x.vote_type == True)) - \
                                 len(vote_ids.filtered(lambda x: x.vote_type == False))

    def search_movie(self, choice, post):
        if choice == 'actor':
            return self.search(['|', ('cast_ids.firstname', 'ilike', post.get('actor-search')),
                                ('cast_ids.lastname', 'ilike', post.get('actor-search'))])
        if choice == 'director':
            return self.search(['|', ('cast_ids.firstname', 'ilike', post.get('director-search')),
                                ('cast_ids.lastname', 'ilike', post.get('director-search'))])
        if choice == 'category':
            return self.search([('genre', 'ilike', post.get('category-select'))])
