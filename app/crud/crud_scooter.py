from app.crud.base import CRUDBase
from app.models.scooter import Scooter
from app.schemas.scooter import ScooterCreateSchema, ScooterUpdateSchema


class CRUDScooter(CRUDBase[Scooter, ScooterCreateSchema, ScooterUpdateSchema]):
    pass


scooter_crud = CRUDScooter(Scooter)
