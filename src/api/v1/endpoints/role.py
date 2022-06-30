from flask import Blueprint

role_blueprint = Blueprint('role_blueprint', __name__)


@role_blueprint.route('/', methods=['get', 'post'])
def get():
    return {'name': 'Hello'}

