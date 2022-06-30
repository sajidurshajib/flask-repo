from api.v1.endpoints import role_blueprint

def register_blueprint_v1(app):
    app.register_blueprint(role_blueprint, url_prefix='/role')