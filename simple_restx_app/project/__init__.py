from flask import Flask, Blueprint
from project.apis import api

app = Flask(__name__)

api_bp = Blueprint("API", __name__, url_prefix='/api')
api.init_app(api_bp)
app.register_blueprint(api_bp)

