from flask_restx import Namespace, Resource, fields
from app.services import facade

api = Namespace('users', description='User operations')

user_model = api.model('User', {
    'first_name': fields.String(required=True, description='First name'),
    'last_name': fields.String(required=True, description='Last name'),
    'email': fields.String(required=True, description='Email')
})

@api.route('/')
class UserList(Resource):
    @api.expect(user_model, validate=True)
    @api.response(201, 'User successfully created')
    @api.response(400, 'Email already registered or invalid data')
    def post(self):
        data = api.payload
        if facade.get_user_by_email(data['email']):
            return {'error': 'Email already registered'}, 400
        u = facade.create_user(data)
        return {
            'id': u.id, 'first_name': u.first_name,
            'last_name': u.last_name, 'email': u.email
        }, 201

    @api.response(200, 'List retrieved')
    def get(self):
        users = facade.list_users()
        return [
            {'id': u.id, 'first_name': u.first_name, 'last_name': u.last_name, 'email': u.email}
            for u in users
        ], 200

@api.route('/<string:user_id>')
class UserResource(Resource):
    @api.expect(user_model, validate=True)
    @api.response(200, 'User updated')
    @api.response(404, 'User not found')
    def put(self, user_id):
        """Update user details by ID"""
        data = api.payload
        updated_user = facade.update_user(user_id, data)
        if not updated_user:
            return {'error': 'User not found'}, 404
        return {
            'id': updated_user.id,
            'first_name': updated_user.first_name,
            'last_name': updated_user.last_name,
            'email': updated_user.email
        }, 200

    @api.expect(user_model, validate=True)
    @api.response(200, 'User updated')
    @api.response(404, 'User not found')
    def put(self, user_id):
        data = api.payload
        u = facade.update_user(user_id, data)
        if not u:
            return {'error': 'User not found'}, 404
        return {'id': u.id, 'first_name': u.first_name, 'last_name': u.last_name, 'email': u.email}, 200
