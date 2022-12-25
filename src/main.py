from flask import Flask, jsonify, request
from api.v1 import routes
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/flaskrepo'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.register_blueprint(routes.routes)


db = SQLAlchemy()


@app.route("/", methods=["GET", "POST"])
def index():
    # print(request.args.get('code')
    if request.method == 'GET':
        return jsonify(msg='Welcome to flask-repo'), 200


if __name__ == "__main__":
    app.run(debug=True, port="8000")
