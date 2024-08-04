from datetime import datetime, timedelta
import uuid
import pytest

from fastapi.testclient import TestClient
from fastapi import status

from app.db import DB


def test_create_rule(test_client: TestClient, mocker):
    token = uuid.uuid4()
    mocker.patch("app.redirect.uuid.uuid4", return_value=token)
    data = {
        "url": "http://example.com",
        "context": {
            "start": str(datetime.now()),
            "end": str(datetime.now() + timedelta(days=1)),
        },
        "rule_type": "date",
    }

    response = test_client.post("/rule", json=data)

    assert response.status_code == status.HTTP_200_OK, response.json()
    assert response.json() == data | {"token": str(token)}
    assert DB[str(token)] is not None


@pytest.mark.parametrize(
    "context",
    (
        {"start": str(datetime.now())},
        {"end": str(datetime.now())},
        {},
    ),
)
def test_create_rule__date_validate(test_client: TestClient, context):
    data = {
        "url": "http://example.com",
        "context": context,
        "rule_type": "date",
    }

    response = test_client.post("/rule", json=data)

    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY, response.json()
    assert response.json() == {"detail": "Unknown format"}


@pytest.mark.parametrize(
    "context",
    (
        {"agent": None},
        {},
    ),
)
def test_create_rule__user_agent_validate(test_client: TestClient, context):
    data = {
        "url": "http://example.com",
        "context": context,
        "rule_type": "user_agent",
    }

    response = test_client.post("/rule", json=data)

    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY, response.json()
    assert response.json() == {"detail": "Unknown format"}


@pytest.mark.usefixtures("_set_db")
def test_redirect(mocker, test_client: TestClient):
    mocker.patch("app.redirect.requests.post", return_value="http://example.com")
    response = test_client.get("/redirect/valid-token", allow_redirects=False)

    assert response.status_code == status.HTTP_302_FOUND, response.json()
    assert response.headers["location"] == "http://example.com"
