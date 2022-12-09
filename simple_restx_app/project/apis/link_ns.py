from flask_restx import Namespace, Resource, fields, reqparse
from flask import request
from datetime import datetime
import urllib.request

links_ns = Namespace('link', description='All links related operations')


linky = []

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

link_api_model_in = links_ns.model(
    "LinkAPIModelIn",
    {
        "link": fields.String(required=True, description="Link that you link to store"),
        "title": fields.String(required=True, description="Title you like to give for link"),
    },
)

link_api_model_out = links_ns.model(
    "LinkAPIModelOut",
    {
        "id" : fields.Integer(),
        "link" : fields.String(),
        "title" : fields.String(),
        "created" : fields.DateTime(),
        "updated" : fields.DateTime()
    },
)

@links_ns.route('/')
class LinkRoute(Resource):
    @links_ns.expect(link_api_model_in)
    def post(self):
        link_api_parser = reqparse.RequestParser()
        link_api_parser.add_argument('link', required=True)
        link_api_parser.add_argument('title', required=True)
        data = link_api_parser.parse_args()
        error = []
        id = str(round(datetime.now().timestamp()))
        link = data.get('link')
        title = data.get('title')
        error = checkLink(link=link, error=error)
        if len(error) == 0:
            linky.append({'id' : id, 'link' : link, 'title':title, 'created' : datetime.now(), 'updated' : datetime.now()})
            return {'data' : 'link added with id {}'.format(id), 'error' : []}, 200
        else:
            return {'data' : [], 'error' : error}, 404
    
    @links_ns.marshal_with(link_api_model_out)
    def get(self):
        return linky
    
    # @links_ns.expect(link_api_model)
    # def put(self):
    #     link_api_parser = reqparse.RequestParser()
    #     link_api_parser.add_argument('id', required=True, type=int)
    #     link_api_parser.add_argument('link', required=True, type=str)
    #     link_api_parser.add_argument('title', required=True, type=str)
    #     data = link_api_parser.parse_args()
    #     error = []
    #     id = data.get('id')
    #     link = data.get('link')
    #     title = data.get('title')

    #     error = checkId(id, error)
    #     error = checkLink(link, error)

    #     if len(error) == 0:
    #         linky[id] = {'id' : id, 'link' : link}
    #         return {'data' : 'link updated on id {}'.format(id), 'error' : []}, 200
    #     else:
    #         return {'data' : [], 'error' : error}, 404