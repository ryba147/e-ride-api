from app.crud.base import CRUDBase
from app.models.role import Role
from app.schemas.role import RoleCreateSchema, RoleUpdateSchema


class CRUDRole(CRUDBase[Role, RoleCreateSchema, RoleUpdateSchema]):
    pass


role_crud = CRUDRole(Role)
