from flask import Flask
from api.v1.register_blueprint import register_blueprint_v1

app = Flask(__name__)


@app.route('/', methods=['get'])
def index():
    return {'msg':'Hello Flask'}


register_blueprint_v1(app)

if __name__ == "__main__":
    app.run(use_reloader=True, debug=True)