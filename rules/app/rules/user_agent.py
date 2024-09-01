from .base import Rule
from ..models import UserAgent


class UserAgentRule(Rule):
    rule_type = "user_agent"
    model = UserAgent
