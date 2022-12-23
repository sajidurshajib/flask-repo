from flask import Flask, jsonify, request
from api.v1 import routes

app = Flask(__name__)
app.register_blueprint(routes.routes)


@app.route("/", methods=["GET", "POST"])
def index():
    # print(request.args.get('code'))
    if request.method == "GET":
        return jsonify(msg="GET Response"), 200
    if request.method == "POST":
        return jsonify(msg="POST Response"), 201


@app.route("/<int:id>", methods=["PATCH", "DELETE"])
def single(id: int):
    if request.method == "PATCH":
        return jsonify(msg="Patch response", id=id), 202
    if request.method == "DELETE":
        return jsonify(msg="Remove Response", id=id), 200


if __name__ == "__main__":
    app.run(debug=True, port="8000")
