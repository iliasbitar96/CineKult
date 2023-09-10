from werkzeug.utils import redirect

from odoo.http import Controller, request, route, Response
from odoo.tools import json


class Main(Controller):
    @route('/', type='http', auth="public", cors='*')
    def my_page(self, movies=False):
        return redirect('http://localhost:3000/')

    @route('/cm_cast/search_movies', type='http', auth='public', methods=['POST', 'GET'], cors="*")
    def search_movies(self, **post):
        headers_json = {'Content-Type': 'application/json'}
        name = post.get('search')
        Movie = request.env['movie']
        movies = Movie.sudo().search([])
        if name:
            for movie in movies:
                if movie.description:
                    if name in movie.description:
                        Movie += movie
            movie_name_search = Movie.sudo().search(['|', '|', '|', ('name', 'ilike', name), ('genre', 'ilike', name),
                                                     ('cast_ids.lastname', 'ilike', name),
                                                     ('cast_ids.firstname', 'ilike', name)])
            filtered_movies = movie_name_search + Movie
        else:
            filtered_movies = movies
        movie_list = []
        for movie in filtered_movies:
            movie_list.append(
                {
                    'id': movie.id,
                    'name': movie.name,
                    'votes': movie.total_votes,
                    'year': movie.year,
                    'director': ','.join(movie.director.mapped('name')),
                    'actors': ', '.join(movie.cast_ids.mapped('name'))
                }
            )
        return Response(json.dumps(movie_list), headers=headers_json)

    @route('/cm_cast/search_selection', type='http', auth='public', methods=['POST'])
    def save_product(self, **post):
        choice = post.get('choice-select')
        Movie = request.env['movie']
        movies = Movie.search_movie(choice, post)
        return request.render('cm_cast.main_page', {'movies': movies})

    @route('/cm_cast/set_vote', type='http', auth='public', methods=['POST'], cors='*', csrf=False)
    def set_vote(self, **post):
        headers_json = {'Content-Type': 'application/json'}
        movie_id = request.env['movie'].sudo().browse(int(post.get('id')))
        Vote = request.env['vote']
        user_vote = Vote.sudo().search([('movie_id', '=', movie_id.id), ('user_id', '=', request.env.user.id)], limit=1)
        vote_type = post.get('up_vote') == '1'
        if user_vote:
            user_vote.update({
                'vote_type': vote_type,
            })
        else:
            Vote.sudo().create({
                'movie_id': movie_id.id,
                'user_id': request.env.user.id,
                'vote_type': post.get('up_vote') == '1',
            })
        return Response(json.dumps({'vote': movie_id.total_votes}), headers=headers_json)

    @route('/cm_cast/filter_movies', type='http', auth='public', methods=['POST'], cors='*', csrf=False)
    def filter_movie(self, **post):
        print(post)
