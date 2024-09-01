import pytest

from fastapi.testclient import TestClient
from app.main import app
from app import db


@pytest.fixture
def test_client():
    return TestClient(app)


@pytest.fixture
def _set_db():
    db.DB["valid-token"] = [
        {
            "type": "date",
            "url": "http://example.com",
            "context": {},
        },
    ]
