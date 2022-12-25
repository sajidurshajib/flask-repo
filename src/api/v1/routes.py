from api.v1.endpoints import users, posts
from flask import Blueprint

routes = Blueprint('routes', __name__, url_prefix='/')


routes.register_blueprint(users.users_blueprint)
routes.register_blueprint(posts.posts_blueprint)
