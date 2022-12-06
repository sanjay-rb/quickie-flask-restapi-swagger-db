from app import api
from flask_restx import Resource

@api.route('/index')
class Index(Resource):
    def get(self):
        return {"data": "Welcome to Quike on Flask, REST API, Swagger UI, DB Connection"}    