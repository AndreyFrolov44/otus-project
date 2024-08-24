import logging

from fastapi.testclient import TestClient
from pytest import LogCaptureFixture


def test_redirect__valid_token(test_client: TestClient, caplog: LogCaptureFixture):
    with caplog.at_level(logging.INFO):
        test_client.post("/redirect")

    assert "REQUEST START" in caplog.text
    assert "REQUEST END" in caplog.text
