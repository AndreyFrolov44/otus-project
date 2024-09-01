from typing import ClassVar

from pydantic import BaseModel


class Rule:
    rule_type: ClassVar[str]
    model: ClassVar[type[BaseModel]]

    def __init__(self, context: dict) -> None:
        self.context = context

    def validate(self):
        self.model.model_validate(self.context)
