from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return {"data": "Welcome to Quike on Flask, REST API, Swagger UI, DB Connection"}