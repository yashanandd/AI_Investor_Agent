from fastapi import FastAPI

from app.routes.analyze import router

app = FastAPI(
    title="AI Investment Research Agent"
)

app.include_router(router)