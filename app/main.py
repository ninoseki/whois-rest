from fastapi import FastAPI
from fastapi.middleware.gzip import GZipMiddleware

from . import api, index, settings


def create_app() -> FastAPI:
    app = FastAPI(
        debug=settings.DEBUG,
        title=settings.PROJECT_NAME,
    )
    # add middleware
    app.add_middleware(GZipMiddleware, minimum_size=1000)

    # add routes
    app.include_router(index.router)
    app.include_router(api.router, prefix="/api/v1")

    return app
