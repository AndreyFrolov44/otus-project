from fastapi.requests import Request
from dependency_injector.wiring import inject, Provide

from .models import Rule
from .rules.service import RulesService


class RedirectService:
    @inject
    def redirect(
        self,
        rules: list[Rule],
        request: Request,
        rules_service: RulesService = Provide["rules_service"],
    ):
        for r in rules:
            rule = rules_service.get_rule(r.rule_type)(r.context, r.url, request)
            if rule.match():
                return rule.get_target_url()
