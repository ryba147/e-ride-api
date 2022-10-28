from fastapi import FastAPI

from app.routers import health, users, roles

app = FastAPI()

app.include_router(health.router)
app.include_router(users.router)
app.include_router(roles.router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, port=8000)
