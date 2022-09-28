from typing import Optional, List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.crud.crud_roles import role_crud
from app.deps import get_db
from app.schemas.role import RoleBase

router = APIRouter(
    prefix="/roles",
    tags=["Roles"],
)


@router.get("/", response_model=List[RoleBase])
def list_roles(limit: Optional[int] = 100, db: Session = Depends(get_db)):
    roles = role_crud.get_list(db, limit=limit)
    return roles
