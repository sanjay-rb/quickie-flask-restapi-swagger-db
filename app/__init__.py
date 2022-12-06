from flask import Flask, Blueprint
from flask_restx import Api

api_bp = Blueprint('API', __name__, url_prefix='/api')

app = Flask(__name__)
api = Api(api_bp, doc='/doc')

app.register_blueprint(api_bp)

from app.routes import index