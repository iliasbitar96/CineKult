from odoo import models, fields, api


class Movie(models.Model):
    _name = 'movie'
    _description = 'movies'

    name = fields.Char('Movie')
    vote_id = fields.Many2one('vote')
    total_votes = fields.Integer(related="vote_id.total_votes", store=True)
    cast_ids = fields.Many2many('cast.member', domain="[('member_type', '=', 'actor')]")
    genre = fields.Selection(
        [('horror', 'Horror'), ('thriller', 'Thriller'), ('animation', 'Animation'), ('drame', 'Drame')])
    duration = fields.Selection([('1h00', '1h00'), ('1h30', '1h30'), ('2h00', '2h00'), ('2h30', '2h30'), ('3h', '3h+')])
    description = fields.Text('Description')
    production = fields.Many2one('production', 'Production')
    creator_id = fields.Many2one('res.user')
    year = fields.Integer('Year')
    director = fields.Many2one('cast.member', domain="[('member_type', '=', 'director')]")
    total_votes = fields.Integer('Votes', compute='compute_total_votes')

    @api.depends('vote_id', 'vote_id.vote_type')
    def compute_total_votes(self):
        Vote = self.env['vote']
        for record in self:
            movie_votes = Vote.sudo().search([('movie_id', '=', record.id)])
            record.total_votes = len(movie_votes.filtered(lambda x: x.vote_type == True)) \
                    - len(movie_votes.filtered(lambda x: x.vote_type == False))

    def search_movie(self, choice, post):
        if choice == 'actor':
            return self.search(['|', ('cast_ids.firstname', 'ilike', post.get('actor-search')),
                                ('cast_ids.lastname', 'ilike', post.get('actor-search'))])
        if choice == 'director':
            return self.search(['|', ('cast_ids.firstname', 'ilike', post.get('director-search')),
                                ('cast_ids.lastname', 'ilike', post.get('director-search'))])
        if choice == 'category':
            return self.search([('genre', 'ilike', post.get('category-select'))])
