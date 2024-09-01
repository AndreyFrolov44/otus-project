from .base import Rule


class UserAgentRule(Rule):
    rule_type = "user_agent"

    def match(self):
        return self.request.headers.get("user-agent") == self.context["agent"]
