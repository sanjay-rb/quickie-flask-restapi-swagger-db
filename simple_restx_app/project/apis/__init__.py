from flask_restx import Api

from project.apis.link_ns import links_ns

api = Api(
    title='Linky',
    version='1.0',
    description='An api framework for store link with users',
    doc='/doc'
)

api.add_namespace(links_ns)