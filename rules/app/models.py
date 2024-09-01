from datetime import datetime
from pydantic import BaseModel


class BaseRedirect(BaseModel):
    rule_type: str


class CreateRedirect(BaseRedirect):
    url: str
    context: dict


class Redirect(CreateRedirect):
    token: str


class Date(BaseModel):
    start: datetime | None
    end: datetime | None


class UserAgent(BaseModel):
    agent: str
