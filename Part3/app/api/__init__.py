from .v1 import places
from flask_restx import Api
from api.v1.places import api as places_ns
from api.v1.reviews import api as reviews_ns

api = Api(
    title='HBnB API',
    version='1.0',
    description='HBnB API Documentation'
)

api.add_namespace(places_ns, path='/api/v1/places')
api.add_namespace(reviews_ns, path='/api/v1/reviews')
