from pydantic import BaseModel


class Url(BaseModel):
    url: str


class Rule(BaseModel):
    rule_type: str
    url: str
    context: dict
