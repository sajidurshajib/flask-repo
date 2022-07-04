from models import Role
from schemas import RoleIn, RoleUpdate
from repo import roles_repo
from services import BaseService


roles_service = BaseService[Role, RoleIn, RoleUpdate](Role, roles_repo)