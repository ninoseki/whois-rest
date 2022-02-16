from datetime import datetime
from typing import Optional, Union

from humps import camelize
from pydantic import BaseModel


class APIModel(BaseModel):
    class Config:
        alias_generator = camelize
        allow_population_by_field_name = True


class Contact(APIModel):
    organization: Optional[str] = None
    email: Optional[str] = None
    name: Optional[str] = None
    telephone: Optional[str] = None


class Abuse(APIModel):
    email: Optional[str] = None
    telephone: Optional[str] = None


class WhoisRecord(APIModel):
    raw_text: str

    tech: Contact
    admin: Contact
    registrant: Contact

    statuses: list[str]
    name_servers: list[str]

    domain: Optional[str] = None

    expires_at: Optional[Union[datetime, str]] = None
    registered_at: Optional[Union[datetime, str]] = None
    updated_at: Optional[Union[datetime, str]] = None
