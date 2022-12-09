import urllib.request
from project import app
from flask import request, jsonify

from datetime import datetime

from project.models import User, Link


# Creating link is validate or not.
def checkLink(link, error):
    try:
        if not str(urllib.request.urlopen(link).getcode()).startswith('20'):
            error.append("ERROR: Link given is not valid")    
    except Exception as e:
        error.append("ERROR: Link given is not valid")
    return error

# Creating a basic GET endpoint for
# Endpoint : http://localhost:5000/
@app.route('/')
def index():
    Link().create_db()
    return {'data':'Hello World!'}

# Create operation CRUD, ie : C -> CRUD
# Endpoint : http://localhost:5000/createuser
# To create a new user 
@app.route('/createuser', methods=['POST'])
def createuser():
    data = request.get_json()
    error = []
    name = data.get('name')
    try:
        user = User(name=name, created=datetime.now(), updated=datetime.now())
        user.add()
    except Exception as err:
        error.append(str(err))
    
    if len(error) == 0:
        return jsonify({'data' : 'user added with id {}'.format(user.id), 'error' : []}), 200
    else:
        return jsonify({'data' : [], 'error' : error}), 404

# Delete operation CRUD, ie : D -> CRUD
# Endpoint : http://localhost:5000/deleteuser 
# To delete a new user 
@app.route('/deleteuser', methods=['DELETE'])
def deleteuser():
    data = request.get_json()
    error = []
    id = data.get('id')
    try:
        user = User.query.filter(User.id == id).first()
        user.delete()
    except Exception as err:
        error.append(str(err))
    
    if len(error) == 0:
        return jsonify({'data' : 'user deleted with id {}'.format(id), 'error' : []}), 200
    else:
        return jsonify({'data' : [], 'error' : error}), 404


# Read operation CRUD, ie : R -> CRUD
# Endpoint : http://localhost:5000/userlink
# To read & return all links of user
@app.route('/userlink', methods=['GET'])
def userlink():
    data = request.get_json()
    error = []
    linky = []
    user_id = data.get('user_id')

    try:
        # For single user -> multiple link can be there
        # MANY to MANY
        links = User.query.filter(User.id == user_id).first().links
        linky = [l.json() for l in links]
    except Exception as err:
        error.append(str(err))

    if len(error) == 0:
        return jsonify({'data' : linky, 'error' : []}), 200
    else:
        return jsonify({'data' : [], 'error' : error}), 404


# Read operation CRUD, ie : R -> CRUD
# Endpoint : http://localhost:5000/linkuser
# To read & return all users having a link
@app.route('/linkuser', methods=['GET'])
def linkuser():
    data = request.get_json()
    error = []
    users = []
    link_id = data.get('link_id')

    try:
        # For single link -> multiple user can be there
        # MANY to MANY
        creators = Link.query.filter(Link.id == link_id).first().creators
        users = [c.json() for c in creators]
    except Exception as err:
        error.append(str(err))

    if len(error) == 0:
        return jsonify({'data' : users, 'error' : []}), 200
    else:
        return jsonify({'data' : [], 'error' : error}), 404


# Create operation CRUD, ie : C -> CRUD
# Endpoint : http://localhost:5000/createlink  
# To create a new link 
@app.route('/createlink', methods=['POST'])
def createlink():
    data = request.get_json()
    error = []
    id = str(round(datetime.now().timestamp()))
    title = data.get('title')
    new_link = data.get('link')
    user_id = data.get('user_id')

    error = checkLink(new_link, error)

    try:
        user = User.query.filter(User.id == user_id).first() # getting user
        try:
            link = Link.query.filter(Link.link == new_link).first() # getting link if exists
            if not link:
                raise Exception("Link not found") # if not exists, raise Exception
        except Exception as e:
            link = Link(id=id, title=title, link=new_link, created=datetime.now(), updated=datetime.now()) # creating new link 
        user.links.append(link) # just adding this link to user
        user.update() # and updating the user for db.commit() & done
    except Exception as err:
        if "NOT NULL constraint failed: link.user_id" in str(err):
            error.append("ERROR : Please provide valid 'user_id' while creating link")
        else:
            error.append(str(err))
    
    if len(error) == 0:
        return jsonify({'data' : 'link added with id {}'.format(id), 'error' : []}), 200
    else:
        return jsonify({'data' : [], 'error' : error}), 404

# Read operation CRUD, ie : R -> CRUD
# Endpoint : http://localhost:5000/readlink (or) http://localhost:5000/
# To read & return all links
@app.route('/', methods=['GET'])
@app.route('/readlink', methods=['GET'])
def readlink():
    error = []
    linky = []

    try:
        links = Link.query.all() # we get as model obj
        linky = [l.json() for l in links] # running new loop for change obj to json :(, but we can find solution for this in upcoming modules
    except Exception as err:
        error.append(str(err))

    if len(error) == 0:
        return jsonify({'data' : linky, 'error' : []}), 200
    else:
        return jsonify({'data' : [], 'error' : error}), 404

# Read operation CRUD, ie : R -> CRUD
# Endpoint : http://localhost:5000/readlink (or) http://localhost:5000/
# To read & return one link
@app.route('/<int:id>', methods=['GET'])
@app.route('/readlink/<int:id>', methods=['GET'])
def readSinglelink(id):
    error = []
    linky = []

    try:
        link = Link.query.filter(Link.id == id).first()
        linky.append(link.json())
    except Exception as err:
        if "'NoneType' object has no attribute" in str(err):
            error.append("ERROR : There is not link created with id {}".format(id))
        else:
            error.append(str(err))

    if len(error) == 0:
        return jsonify({'data' : linky, 'error' : []}), 200
    else:
        return jsonify({'data' : [], 'error' : error}), 404


# Update operation CRUD, ie : U -> CRUD
# Endpoint : http://localhost:5000/updatelink 
# To update a link 
@app.route('/updatelink', methods=['PUT'])
def updatelink():
    data = request.get_json()
    error = []
    id = data.get('id')
    new_link = data.get('link')
    new_title = data.get('title')

    try:
        link = Link.query.filter(Link.id == id).first()
        if new_link:
            error = checkLink(new_link, error)
            link.link = new_link
        if new_title:
            link.title = new_title
        link.update()
    except Exception as err:
        if "'NoneType' object has no attribute" in str(err):
            error.append("ERROR : There is not link created with id {}".format(id))
        else:
            error.append(str(err))

    if len(error) == 0:
        return jsonify({'data' : 'link updated on id {}'.format(id), 'error' : []}), 200
    else:
        return jsonify({'data' : [], 'error' : error}), 404

# Delete operation CRUD, ie : D -> CRUD
# Endpoint : http://localhost:5000/deletelink 
# To delete a link
@app.route('/deletelink', methods=['DELETE'])
def deletelink():
    data = request.get_json()
    error = []
    id = data.get('id')

    try:
        link = Link.query.filter(Link.id  == id).first()
        link.delete()
    except Exception as err:
        if "'NoneType' object has no attribute" in str(err):
            error.append("ERROR : There is not link created with id {}".format(id))
        else:
            error.append(str(err))

    if len(error) == 0:
        return jsonify({'data' : 'link with id {} deleted'.format(id), 'error' : []}), 200
    else:
        return jsonify({'data' : [], 'error' : error}), 404