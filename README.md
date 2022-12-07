# Welcome to the Quickie on Flask, REST API, Swagger UI, DB Connection

## Run setup.bat file for windows
- Open cmd in repo folder
- Run `setup.bat`

## Starter App
- Open `starter_app` folder, run `app.py` file 

[starter_app\app.py](starter_app\app.py)

```python
# Importing flask modules to start with
from flask import Flask

# Creating new flask app
app = Flask(__name__)

# Creating a basic GET endpoint for
# Endpoint : http://localhost:5000/
@app.route('/')
def index():
    return {'data':'Hello World!'}

# Main code to start the server
if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)
```

## Simple Rest API App
- Open `simple_restapi_app` folder, run `app.py` file 

[simple_restapi_app\app.py](simple_restapi_app\app.py)

```python
# Importing requried modules
from flask import Flask, jsonify, request
from datetime import datetime
import urllib.request

# Creating new flask app
app = Flask(__name__)

# Creating empty linky dict for store the links
linky = {}

# Creating 2 check which will validate and verify the data
def checkLink(link, error):
    try:
        if not str(urllib.request.urlopen(link).getcode()).startswith('20'):
            error.append("ERROR: Link given is not valid")    
    except Exception as e:
        error.append("ERROR: Link given is not valid")
    return error

def checkId(id, error):
    if id not in linky:
        error.append("ERROR: Link ID given is not valid")
    return error

# Let's start with our CRUD app logic

# Create operation CRUD, ie : C -> CRUD
# Endpoint : http://localhost:5000/createlink  
# To create a new link dict and add that to our linky dict
@app.route('/createlink', methods=['POST'])
def createlink():
    data = request.get_json()
    error = []
    id = str(round(datetime.now().timestamp()))
    link = data['link']
    error = checkLink(link=link, error=error)
    if len(error) == 0:
        linky[id] = {'id' : id, 'link' : link}
        return jsonify({'data' : 'link added with id {}'.format(id), 'error' : []}), 200
    else:
        return jsonify({'data' : [], 'error' : error}), 404

# Read operation CRUD, ie : R -> CRUD
# Endpoint : http://localhost:5000/readlink (or) http://localhost:5000/
# To read & return all links in linky dict
@app.route('/', methods=['GET'])
@app.route('/readlink', methods=['GET'])
def readlink():
    return jsonify({'data' : linky, 'error' : []}), 200

# Update operation CRUD, ie : U -> CRUD
# Endpoint : http://localhost:5000/updatelink 
# To update a link in linky dict using link's id
@app.route('/updatelink', methods=['PUT'])
def updatelink():
    data = request.get_json()
    error = []
    id = data['id']
    link = data['link']

    error = checkId(id, error)
    error = checkLink(link, error)

    if len(error) == 0:
        linky[id] = {'id' : id, 'link' : link}
        return jsonify({'data' : 'link updated on id {}'.format(id), 'error' : []}), 200
    else:
        return jsonify({'data' : [], 'error' : error}), 404

# Delete operation CRUD, ie : D -> CRUD
# Endpoint : http://localhost:5000/deletelink 
# To delete a link in linky dict using link's id
@app.route('/deletelink', methods=['DELETE'])
def deletelink():
    data = request.get_json()
    error = []
    id = data['id']

    error = checkId(id, error)

    if len(error) == 0:
        del linky[data['id']]
        return jsonify({'data' : 'link with id {} deleted'.format(data['id']), 'error' : []}), 200
    else:
        return jsonify({'data' : [], 'error' : error}), 404

# Main template code to start the server
if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)
```



## Reference link
- [Flask Documentation](https://flask.palletsprojects.com/en/2.2.x/)
- [RestX Documentation](https://flask-restx.readthedocs.io/en/latest/installation.html)
