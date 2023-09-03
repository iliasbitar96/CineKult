from werkzeug.utils import redirect

from odoo.http import Controller, request, route, Response
from odoo.tools import json


class Main(Controller):
    @route('/', type='http', auth="public")
    def my_page(self, movies=False):
        Movies = request.env['movie']
        products = Movies.sudo().search([])
        movie_list = []
        for product in products:
            movie_list.append(
                {
                    'id': product.id,
                    'name': product.name,
                }
            )
        return request.render('cm_cast.main_page', {'movies': movie_list})

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
