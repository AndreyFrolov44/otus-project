from .base import Rule


class RulesService:
    def __init__(self) -> None:
        self._rules: list[Rule] = []

    def add_rule(self, rule: Rule):
        self._rules.append(rule)

    def get_rule(self, rule_type: str) -> Rule:
        for r in self._rules:
            if r.rule_type == rule_type:
                return r
        raise TypeError
