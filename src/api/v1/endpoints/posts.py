from turtle import title
from flask import Blueprint, jsonify, request
from schemas import PostIn, PostOut


posts_blueprint = Blueprint('posts_blueprint', __name__, url_prefix='/posts')


@posts_blueprint.route('/', methods=['GET', 'POST'])
def all_posts():
    if request.method == 'GET':
        return jsonify(msg="All posts"), 200
    if request.method == 'POST':
        post = PostIn(**request.json)
        post_out = PostOut(title=post.title, body=post.body)
        return jsonify(title=post_out.title, body=post_out.body), 200
