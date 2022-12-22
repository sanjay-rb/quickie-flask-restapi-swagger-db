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

## Let's create simple REST api only using Flask
- We are going to create a CRUD API for simple `Link` storage app.
- We can store any link in this app.
- Please open `2_simple_rest_api` folder and run `start_server.py` to start the server.
- If you see our `project` folder this time we have `routes.py`. What is inside that?

[`./2_simple_rest_api/project/routes.py`](./2_simple_rest_api/project/routes.py)
```python
from project import app
from flask import jsonify, request
from datetime import datetime

# An empty dictionary to store our links
links = {}

# Read operation in CRUD, ie : R -> CRUD
# Endpoint : http://localhost:5000/link (GET)
# To read & return all links in links dictionary
@app.route('/link', methods=['GET'])
@app.route('/link/', methods=['GET'])
def getAllLink():
    return jsonify(links)

# Create operation in CRUD, ie : C -> CRUD
# Endpoint : http://localhost:5000/link (POST)
# To create or add new link to our links dictionary
@app.route('/link', methods=['POST'])
@app.route('/link/', methods=['POST'])
def addLink():
    data = request.get_json()
    uid = datetime.now().strftime("%Y%M%d%H%M%S%f")
    links[uid] = data
    return jsonify({"message" : "Link added succesfully with id {}".format(uid)})

# Update operation in CRUD, ie : U -> CRUD
# Endpoint : http://localhost:5000/link/20221222221211518239 (PUT)
# To update single link using link's id
@app.route('/link/<string:id>', methods=['PUT'])
def updateLink(id):
    data = request.get_json()
    links[id] = data
    return jsonify({"message" : "Link updated succesfully on id {}".format(id)})

# Delete operation in CRUD, ie : D -> CRUD
# Endpoint : http://localhost:5000/link/20221222221211518239 (DELETE)
# To delete single link using link's id
@app.route('/link/<string:id>', methods=['DELETE'])
def deleteLink(id):
    del links[id]
    return jsonify({"message" : "Link deleted succesfully on id {}".format(id)})
```

- We have create our REST API's but we didn't add them to our flask app
- Let's add it to our `__init__.py` file

[`./2_simple_rest_api/project/__init__.py`](./2_simple_rest_api/project/__init__.py)
```python
# ... some code ...

from project import routes
```

## Reference link
- [Flask Documentation](https://flask.palletsprojects.com/en/2.2.x/)
- [Flask SQL-Alchemy](https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/)
- [RestX Documentation](https://flask-restx.readthedocs.io/en/latest/installation.html)