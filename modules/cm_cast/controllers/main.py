from werkzeug.utils import redirect

from odoo.http import Controller, request, route, Response


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


    @route('/cm_cast/search_movies', type='http', auth='public', methods=['POST'])
    def save_product(self, **post):
        name = post.get('search')
        Movie = request.env['movie']
        movies = Movie.search([])
        for movie in movies:
            if movie.description:
                if name in movie.description:
                    Movie += movie
        movie_name_search = Movie.search(['|', '|', '|', ('name', 'ilike', name), ('genre', 'ilike', name),
                                                         ('cast_ids.lastname', 'ilike', name),
                                                         ('cast_ids.firstname', 'ilike', name)])
        filtered_movies = movie_name_search + Movie
        return request.render('cm_cast.main_page', {'movies': filtered_movies})
