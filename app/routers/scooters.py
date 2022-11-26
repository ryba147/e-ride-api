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


@router.patch("/{scooter_id}", response_model=ScooterResponse)
def update_scooter(
    scooter_id: uuid.UUID, scooter_data: ScooterUpdateSchema, db: Session = Depends(get_db)
):
    scooter = scooter_crud.get_by_id(db, scooter_id)
    if not scooter:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"scooter with id {scooter_id} not found.",
        )
    updated_scooter = scooter_crud.update(db, scooter, scooter_data)
    return updated_scooter


@router.delete("/{scooter_id}", status_code=status.HTTP_204_NO_CONTENT)
def update_scooter(scooter_id: uuid.UUID, db: Session = Depends(get_db)):
    scooter = scooter_crud.get_by_id(db, scooter_id)
    if not scooter:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"scooter with id {scooter_id} not found.",
        )
    scooter_crud.delete(db, scooter_id)
