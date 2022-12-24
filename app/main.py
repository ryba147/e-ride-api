import time

from fastapi import FastAPI
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.requests import Request
from starlette.responses import Response

from app.routers import (
    health,
    users,
    scooters,
)

app = FastAPI()

app.include_router(health.router)
app.include_router(users.router)
app.include_router(scooters.router)


# class MyMiddleware(BaseHTTPMiddleware):
#     async def dispatch(
#         self, request: Request, call_next: RequestResponseEndpoint
#     ) -> Response:
#         start_time = time.time()
#         response = await call_next(request)
#         process_time = time.time() - start_time
#         response.headers["X-Process-Time"] = str(process_time)
#         return response
#
# app.add_middleware(MyMiddleware)
#
# @app.get("/t")
# async def t():
#     return {}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, port=8000)
