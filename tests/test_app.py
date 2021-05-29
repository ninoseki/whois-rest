import httpx
import pytest


@pytest.mark.parametrize(
    "hostname",
    ["example.com", "8.8.8.8"],
)
@pytest.mark.asyncio
async def test_valid_input(client: httpx.AsyncClient, hostname: str):
    res = await client.get(f"/api/v1/{hostname}")
    assert res.status_code == 200


@pytest.mark.parametrize(
    "hostname",
    ["echo", "cat"],
)
@pytest.mark.asyncio
async def test_invalid_input(client: httpx.AsyncClient, hostname: str):
    res = await client.get(f"/api/v1/{hostname}")
    assert res.status_code == 400


@pytest.mark.asyncio
async def test_index(client: httpx.AsyncClient):
    res = await client.get("/", allow_redirects=False)
    assert res.status_code == 307
