from fastapi import FastAPI

from .routers import health, users

app = FastAPI()

app.include_router(health.router)
app.include_router(users.router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, port=8000)
