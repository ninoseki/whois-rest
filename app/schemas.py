from datetime import datetime
from typing import List, Optional

from humps import camelize
from pydantic import BaseModel


class APIModel(BaseModel):
    class Config:
        alias_generator = camelize
        allow_population_by_field_name = True


class ParsedWhoisResult(APIModel):
    hostname: str
    raw: str
    status: List[str]
    name_servers: List[str]

    created: Optional[datetime] = None
    updated: Optional[datetime] = None
    expires: Optional[datetime] = None
    registrar: Optional[str] = None
    registrant_name: Optional[str] = None
    registrant_organization: Optional[str] = None
    registrant_address: Optional[str] = None
    registrant_city: Optional[str] = None
    registrant_state: Optional[str] = None
    registrant_zipcode: Optional[str] = None
    registrant_country: Optional[str] = None
    dnssec: Optional[str] = None
