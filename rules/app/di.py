from dependency_injector import containers, providers

from .redirect import RedirectService
from .rules.service import RulesService


class Container(containers.DeclarativeContainer):
    redirect_service = providers.Factory(RedirectService)
    rules_service = providers.Singleton(RulesService)
