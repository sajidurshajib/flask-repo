from flask import Blueprint, jsonify

posts_blueprint = Blueprint('posts_blueprint', __name__, url_prefix='/posts')


@posts_blueprint.route('/', methods=['GET', 'POST'])
def all_posts():
    return jsonify(msg="All posts"), 200
