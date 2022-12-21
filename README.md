# Welcome to the Quickie on Flask, REST API, Swagger UI, DB Connection

## Starter App
- Please open `1_starter` folder and run `start_server.py` to start the server.
- Let's see what is there inside that file.

[`./1_starter/start_server.py`](./1_starter/start_server.py)
```python
from project import app

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
```

- What is this `project` and `app`
- `project` is the custom module which is created and we have `app` variable in it's  `__init__.py`.

[`./1_starter/project/__init__.py`](./1_starter/project/__init__.py)
```python
from flask import Flask

# Creating flask app instance.
app = Flask(__name__)

# Creatng new endpoint to say "Hello, World!"
@app.route("/")
def hello_world():
    return "Hello, World!"
```

## Reference link
- [Flask Documentation](https://flask.palletsprojects.com/en/2.2.x/)
- [Flask SQL-Alchemy](https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/)
- [RestX Documentation](https://flask-restx.readthedocs.io/en/latest/installation.html)