from .base import Rule
from ..models import Date

class DateRule(Rule):
    rule_type = "date"
    model = Date

