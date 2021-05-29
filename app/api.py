from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, ValidationError, stricturl

from . import schemas
from .whois import whois

router = APIRouter()


class Model(BaseModel):
    url: stricturl(strip_whitespace=False, allowed_schemes={"http"})  # noqa: F821


def validate_hostname(hostname: str) -> bool:
    url = f"http://{hostname}"
    Model(url=url)
    return True


@router.get("/{hostname}", response_model=schemas.ParsedWhoisResult)
async def query_whois(hostname: str) -> schemas.ParsedWhoisResult:
    try:
        validate_hostname(hostname)
    except ValidationError:
        raise HTTPException(
            status_code=400,
            detail=f"{hostname} is not a valid input. An IP address or a domain is allowed as an input.",
        )

    return await whois(hostname)
