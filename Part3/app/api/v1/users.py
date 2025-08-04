from flask_restx import Namespace, Resource, fields
from app.services import facade

api = Namespace('users', description='User operations')

user_model = api.model('User', {
    'first_name': fields.String(required=True, description='First name'),
    'last_name': fields.String(required=True, description='Last name'),
    'email': fields.String(required=True, description='Email')
})

@users_ns.route('/')
class UserList(Resource):
    @users_ns.expect(user_model)
    def post(self):
        data = request.get_json()

        if not data.get("password"):
            return {"error": "Password is required"}, 400

        user = User(
            first_name=data.get("first_name"),
            last_name=data.get("last_name"),
            email=data.get("email"),
            password=data.get("password")
        )

        user_repo.save(user) 
        return {
            "id": user.id,
            "message": "User registered successfully"
        }, 20

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

@users_ns.route('/<string:user_id>')
class UserDetail(Resource):
    def get(self, user_id):
        user = user_repo.get(user_id)
        if not user:
            return {"error": "User not found"}, 404
        return user.to_dict(), 200
