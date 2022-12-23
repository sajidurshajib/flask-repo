from flask import Flask, jsonify, request
from api.v1 import routes

app = Flask(__name__)
app.register_blueprint(routes.routes)


@app.route("/", methods=["GET", "POST"])
def index():
    # print(request.args.get('code'))
    return jsonify(msg='Welcome to flask-repo')


if __name__ == "__main__":
    app.run(debug=True, port="8000")
