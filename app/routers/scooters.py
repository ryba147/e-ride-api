import uuid
from typing import Optional, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from app.crud.crud_scooter import scooter_crud
from app.deps import get_db
from app.schemas.scooter import (
    ScooterUpdateSchema,
    ScooterResponse,
    ScooterCreateSchema,
)

router = APIRouter(
    prefix="/scooters",
    tags=["Scooters"],
)


@router.get("/", response_model=List[ScooterResponse])
def list_scooters(limit: Optional[int] = 100, db: Session = Depends(get_db)):
    scooters = scooter_crud.get_list(db, limit=limit)
    return scooters


@router.post("/", response_model=ScooterResponse)
def create_scooter(scooter_data: ScooterCreateSchema, db: Session = Depends(get_db)):
    new_scooter = scooter_crud.create(db, scooter_data)
    return new_scooter


# @router.post("/assign_scooter", response_model=ScooterResponse)
# def assign_scooter_to_user(data: AssignScooterToUser, db: Session = Depends(get_db)):
#     scooter = scooter_crud.get_by_id(db, data.scooter_id)
#     if not scooter:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail=f"Scooter with id {data.scooter_id} not found.",
#         )
#     user = user_crud.get_by_id(db, data.user_id)
#     if not user:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail=f"User with id {data.user_id} not found.",
#         )
#     return assigned_scooter


@router.get("/{scooter_id}", response_model=ScooterResponse)
def get_scooter(scooter_id: uuid.UUID, db: Session = Depends(get_db)):
    scooter = scooter_crud.get_by_id(db, scooter_id)
    if not scooter:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Scooter with id {scooter_id} not found.",
        )
    return scooter


@router.patch("/{scooter_id}", response_model=ScooterResponse)
def update_scooter(
    scooter_id: uuid.UUID,
    scooter_data: ScooterUpdateSchema,
    db: Session = Depends(get_db),
):
    scooter = scooter_crud.get_by_id(db, scooter_id)
    if not scooter:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Scooter with id {scooter_id} not found.",
        )
    updated_scooter = scooter_crud.update(db, scooter, scooter_data)
    return updated_scooter


@router.delete("/{scooter_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_scooter(scooter_id: uuid.UUID, db: Session = Depends(get_db)):
    scooter = scooter_crud.get_by_id(db, scooter_id)
    if not scooter:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Scooter with id {scooter_id} not found.",
        )
    scooter_crud.delete(db, scooter_id)
