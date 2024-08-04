from dependency_injector.wiring import Provide

from .di import Container
from .rules.service import RulesService
from .rules import DateRule, UserAgentRule

rules_service: RulesService = Provide[Container.rules_service]

container = Container()
container.wire(
    modules=[".endpoints", ".main", ".redirect", __name__], packages=[".rules"]
)

rules_service.add_rule(DateRule)
rules_service.add_rule(UserAgentRule)
