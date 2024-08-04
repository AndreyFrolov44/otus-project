from datetime import datetime
from .base import Rule


class DateRule(Rule):
    rule_type = "date"

    def match(self) -> bool:
        current_date = datetime.now()

        return (
            datetime.strptime(self.context["start"], "%Y-%m-%d %H:%M:%S.%f")
            <= current_date
            <= datetime.strptime(self.context["end"], "%Y-%m-%d %H:%M:%S.%f")
        )
