from app.crud.base import CRUDBase
from app.models.role import Role
from app.schemas.role import RoleCreateSchema, RoleUpdate


class CRUDRole(CRUDBase[Role, RoleCreateSchema, RoleUpdate]):
    pass


role_crud = CRUDRole(Role)
