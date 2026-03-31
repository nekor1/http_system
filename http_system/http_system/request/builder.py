from .http_request import HttpRequest

class HttpRequestBuilder:
    def __init__(self, url):
        self.url = url
        self.method = 'GET'
        self.headers = {}
        self.body = None
        self.timeout = 30
        self.retries = 3
        self.auth_token = None
        self.proxy = None
        self.ssl_verify = True
        self.follow_redirects = True
        self.cache_ttl = 0
        self.compression = None

    def set_method(self, method):
        self.method = method
        return self

    def add_header(self, key, value):
        self.headers[key] = value
        return self

    def set_body(self, body):
        self.body = body
        return self

    def set_timeout(self, timeout):
        self.timeout = timeout
        return self

    def set_auth(self, token):
        self.auth_token = token
        return self

    def build(self):
        if not self.url:
            raise ValueError("URL is required")

        return HttpRequest(
            self.url, self.method, self.headers, self.body,
            self.timeout, self.retries, self.auth_token,
            self.proxy, self.ssl_verify, self.follow_redirects,
            self.cache_ttl, self.compression
        )