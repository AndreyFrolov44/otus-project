from abc import abstractmethod
from typing import ClassVar
from fastapi.requests import Request


class Rule:
    rule_type: ClassVar[str]

    def __init__(self, context: dict, url: str, request: Request) -> None:
        self.context = context
        self.url = url
        self.request = request

    @abstractmethod
    def match(self):
        """Проверяет подходит ли правило"""

    def get_target_url(self):
        return self.url
