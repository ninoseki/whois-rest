import httpx
import pytest

from app import create_app


@pytest.fixture
async def client():
    app = create_app()

    async with httpx.AsyncClient(
        app=app,
        base_url="http://testserver",
    ) as client_:
        yield client_
