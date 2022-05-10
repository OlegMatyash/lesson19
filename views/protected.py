from flask_restx import Namespace, Resource

from service.auth import AuthService
from utils import auth_required, admin_access_required

protected_ns = Namespace('protected')


@protected_ns.route('/users')
class UsersView(Resource):

    @auth_required
    def get(self):
        return {}, 200


@protected_ns.route('/admin')
class AdminView(Resource):

    @admin_access_required
    def get(self):
        return {}, 200
