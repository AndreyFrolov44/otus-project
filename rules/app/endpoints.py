from fastapi import APIRouter, Depends, status
from fastapi.responses import RedirectResponse
from dependency_injector.wiring import inject, Provide

from .di import Container
from .redirect import RedirectService
from .models import CreateRedirect, Redirect

router = APIRouter()


@router.post("/rule", response_model=Redirect)
@inject
def create_rule(
    create_redirect: CreateRedirect,
    redirect_service: RedirectService = Depends(Provide[Container.redirect_service]),
):
    redirect = redirect_service.create(create_redirect)

    return redirect


@router.get("/redirect/{token}")
@inject
def redirect(
    token: str,
    redirect_service: RedirectService = Depends(Provide[Container.redirect_service]),
):
    url = redirect_service.redirect(token)
    return RedirectResponse(url, status_code=status.HTTP_302_FOUND)
