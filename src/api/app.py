from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from src.api.routes import document_routes
from src.config.config import settings


def create_app() -> FastAPI:
    app = FastAPI(title=settings.APP_TITLE)

    app.include_router(
        document_routes.router,
        prefix="/api/v1",
        tags=["documents"]
    )

    return app


app = create_app()
