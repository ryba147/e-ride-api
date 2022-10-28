import uuid
from typing import Optional, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from app.crud.crud_roles import role_crud
from app.deps import get_db
from app.schemas.role import RoleUpdateSchema, RoleResponse, RoleCreateSchema

router = APIRouter(
    prefix="/roles",
    tags=["Roles"],
)


@router.get("/", response_model=List[RoleResponse])
def list_roles(limit: Optional[int] = 100, db: Session = Depends(get_db)):
    roles = role_crud.get_list(db, limit=limit)
    return roles


@router.post("/", response_model=RoleResponse)
def create_role(role_data: RoleCreateSchema, db: Session = Depends(get_db)):
    # role = get_role_by_code(db, role_data.code)
    # if role: raise HTTP_400_BAD_REQUEST
    new_role = role_crud.create(db, role_data)
    return new_role


@router.patch("/{role_id}", response_model=RoleResponse)
def update_role(
    role_id: uuid.UUID, role_data: RoleUpdateSchema, db: Session = Depends(get_db)
):
    role = role_crud.get_by_id(db, role_id)
    if not role:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Role with id {role_id} not found.",
        )
    updated_role = role_crud.update(db, role, role_data)
    return updated_role


@router.delete("/{role_id}", status_code=status.HTTP_204_NO_CONTENT)
def update_role(role_id: uuid.UUID, db: Session = Depends(get_db)):
    role = role_crud.get_by_id(db, role_id)
    if not role:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Role with id {role_id} not found.",
        )
    role_crud.delete(db, role_id)
    return
