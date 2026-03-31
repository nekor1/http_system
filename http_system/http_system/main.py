from request.builder import HttpRequestBuilder
from client import BaseHttpClient

from middleware.logging import LoggingMiddleware
from middleware.auth import AuthMiddleware
from middleware.cache import CacheMiddleware
from middleware.retry import RetryMiddleware
from middleware.compression import CompressionMiddleware

# Builder
request = (
    HttpRequestBuilder("https://api.test.com")
    .set_method("POST")
    .set_auth("token123")
    .add_header("Content-Type", "application/json")
    .build()
)

# Decorator chain
client = BaseHttpClient()
client = LoggingMiddleware(client)
client = AuthMiddleware(client)
client = CacheMiddleware(client)
client = RetryMiddleware(client)
client = CompressionMiddleware(client)

# Execute
response = client.execute(request)
print(response)