from flask import Blueprint, jsonify


users_blueprint = Blueprint('users_blueprint',  __name__, url_prefix='/users')


@users_blueprint.route('/', methods=['GET'])
def all_users():
    return jsonify(msg='All users'), 200


@users_blueprint.get('/<int:id>')
def single_user(id: int):
    return jsonify(msg=f'Single user {id}')
