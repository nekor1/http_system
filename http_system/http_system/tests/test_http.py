import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from http_system.request.builder import HttpRequestBuilder
from http_system.client import BaseHttpClient

from http_system.middleware.logging import LoggingMiddleware
from http_system.middleware.auth import AuthMiddleware
from http_system.middleware.cache import CacheMiddleware
from http_system.middleware.retry import RetryMiddleware
from http_system.middleware.compression import CompressionMiddleware


def test_builder_creates_request():
    req = (
        HttpRequestBuilder("https://test.com")
        .set_method("POST")
        .add_header("Content-Type", "application/json")
        .set_timeout(10)
        .build()
    )

    assert req.url == "https://test.com"
    assert req.method == "POST"
    assert req.timeout == 10


def test_decorator_chain_execution():
    req = HttpRequestBuilder("https://test.com").build()

    client = BaseHttpClient()
    client = LoggingMiddleware(client)
    client = AuthMiddleware(client)
    client = CacheMiddleware(client)

    result = client.execute(req)

    assert "response" in result


def test_full_middleware_chain():
    req = HttpRequestBuilder("https://test.com").build()

    client = BaseHttpClient()
    client = LoggingMiddleware(client)
    client = AuthMiddleware(client)
    client = CacheMiddleware(client)
    client = RetryMiddleware(client)
    client = CompressionMiddleware(client)

    result = client.execute(req)

    assert isinstance(result, str)


def test_without_middleware():
    req = HttpRequestBuilder("https://test.com").build()

    client = BaseHttpClient()
    result = client.execute(req)

    assert "response" in result