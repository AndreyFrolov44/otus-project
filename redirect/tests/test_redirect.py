from datetime import datetime, timedelta
from fastapi import status
from fastapi.testclient import TestClient
from fastapi.requests import Request
from starlette.datastructures import Headers
import pytest

from app.rules.date import DateRule
from app.rules.user_agent import UserAgentRule

url = "http://example.com"


def test_redirect__valid_token(test_client: TestClient):
    data = [
        {
            "rule_type": "date",
            "url": url,
            "context": {
                "start": str(datetime.now() - timedelta(days=15)),
                "end": str(datetime.now() + timedelta(days=15)),
            },
        },
    ]

    response = test_client.post("/redirect", json=data)

    assert response.status_code == status.HTTP_200_OK, response.json()
    assert response.json() == {"url": url}


@pytest.mark.parametrize(
    ("context", "is_match"),
    [
        (
            {
                "start": str(datetime.now() - timedelta(days=15)),
                "end": str(datetime.now() + timedelta(days=15)),
            },
            True,
        ),
        (
            {
                "start": str(datetime.now()),
                "end": str(datetime.now() + timedelta(days=1)),
            },
            True,
        ),
        (
            {
                "start": str(datetime.now()),
                "end": str(datetime.now() - timedelta(days=1)),
            },
            False,
        ),
        (
            {
                "start": str(datetime.now() + timedelta(days=1)),
                "end": str(datetime.now()),
            },
            False,
        ),
    ],
)
def test_datetime_redirect(context: dict, is_match: bool):
    request = Request({"type": "http"})

    rule = DateRule(context=context, url=url, request=request)

    assert rule.match() == is_match


@pytest.mark.parametrize(
    ("context", "is_match"),
    [
        (
            {"agent": "chrome"},
            True,
        ),
        (
            {"agent": "safari"},
            False,
        ),
        (
            {"agent": "mobile"},
            False,
        ),
    ],
)
def test_user_agent_redirect(context: dict, is_match: bool):
    request = Request(
        {"type": "http", "headers": Headers({"user-agent": "chrome"}).raw}
    )

    rule = UserAgentRule(context=context, url=url, request=request)

    assert rule.match() == is_match
