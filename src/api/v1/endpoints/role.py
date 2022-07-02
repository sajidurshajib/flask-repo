from flask import Blueprint
from flask_pydantic import validate
from schemas import RoleIn, RoleOut, RoleUpdate, RoleQuery


role_blueprint = Blueprint('role_blueprint', __name__)


@role_blueprint.route('/', methods=['get'])
@validate()
def get_role():
    return RoleOut(name='Hello')


@role_blueprint.route('/', methods=['post'])
@validate()
def create_role(body: RoleIn):
    return RoleOut(name=body.name)
    

@role_blueprint.route('/', methods=['patch'])
@validate()
def update_role(body:RoleUpdate, query:RoleQuery):
    print(query)
    return RoleOut(name=body.name)
