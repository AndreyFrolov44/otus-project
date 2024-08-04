from fastapi import APIRouter, Depends, Request
from dependency_injector.wiring import inject, Provide

from .di import Container
from .redirect import RedirectService
from .models import Rule, Url

router = APIRouter()


@router.post("/redirect", response_model=Url)
@inject
def redirect(
    rules: list[Rule],
    request: Request,
    redirect_service: RedirectService = Depends(Provide[Container.redirect_service]),
):
    return Url.model_validate({"url": redirect_service.redirect(rules, request)})
