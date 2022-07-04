from models import Role
from schemas import RoleIn, RoleUpdate
from repo import BaseRepo

roles_repo = BaseRepo[Role, RoleIn, RoleUpdate](Role)