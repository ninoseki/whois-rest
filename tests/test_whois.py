import pytest

from app import schemas
from app.whois import whois


@pytest.mark.parametrize(
    "hostname",
    ["example.com", "8.8.8.8"],
)
@pytest.mark.asyncio
async def test_whois(hostname: str):
    res = await whois(hostname)
    assert isinstance(res, schemas.ParsedWhoisResult)
    assert res.raw != ""
