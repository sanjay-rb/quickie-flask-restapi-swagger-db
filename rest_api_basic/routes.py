from rest_api_basic import app
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