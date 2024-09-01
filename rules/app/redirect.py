import uuid
import requests

from dependency_injector.wiring import inject, Provide
from pydantic import ValidationError
from fastapi import HTTPException, status

from .rules.service import RulesService
from .models import CreateRedirect, Redirect
from .db import DB


class RedirectService:
    def redirect(self, token: str):
        rules = DB.get(token)
        if not rules:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="token not exist"
            )

        return requests.post(f"http://localhost:8001/redirect/{token}", json=rules)

    @inject
    def create(
        self,
        redirect: CreateRedirect,
        rules_service: RulesService = Provide["rules_service"],
    ):
        rule_type = redirect.rule_type
        rule = rules_service.get_rule(rule_type)(redirect.context)
        try:
            rule.validate()
        except ValidationError:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail="Unknown format",
            )

        token = str(uuid.uuid4())
        DB[token] = redirect.model_dump()
        return Redirect.model_validate(redirect.model_dump() | {"token": token})
