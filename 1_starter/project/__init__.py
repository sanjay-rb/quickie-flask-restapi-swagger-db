from flask import Flask

# Creating flask app instance.
app = Flask(__name__)

# Creatng new endpoint to say "Hello, World!"
@app.route("/")
def hello_world():
    return "Hello, World!"