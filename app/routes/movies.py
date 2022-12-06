from datetime import datetime
from app import api
from flask import request
from flask_restx import Resource, fields

from app.models.movie_model import MovieModel

movies = [
    MovieModel(id=datetime.now().strftime('%Y%m%d%H%M%S%f'), name='Master', date='2021-01-13', hit=True)
]

get_output_model = api.model(
    'Get Movie', 
    {
        'name': fields.String(),
        'date': fields.Date(),
    }
)

post_input_model = api.model(
    'Post Movie', 
    {
        'name': fields.String(),
        'date': fields.Date(),
        'hit': fields.Boolean(),
    }
)

@api.route('/movies')
class Movies(Resource):

    @api.marshal_with(get_output_model, envelope="data")
    def get(self):
        return movies

    @api.expect(post_input_model)
    def post(self):
        data = request.get_json()
        new_movie = MovieModel(id=datetime.now().strftime('%Y%m%d%H%M%S%f'), name=data['name'], date=data['date'], hit=data['hit'])
        movies.append(new_movie)
        return {
            "data" : "{} Movie added to our database".format(new_movie),
            "error" : ""
        }