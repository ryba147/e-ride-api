from fastapi import APIRouter, HTTPException, status

router = APIRouter(
    prefix="/health",
    tags=["Health"],
)


@router.get("/")
async def health():
    return {"health": "ok"}
