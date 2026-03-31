class HttpRequest:
    def __init__(self, url, method, headers, body,
                 timeout, retries, auth_token,
                 proxy, ssl_verify, follow_redirects,
                 cache_ttl, compression):
        self.url = url
        self.method = method
        self.headers = headers
        self.body = body
        self.timeout = timeout
        self.retries = retries
        self.auth_token = auth_token
        self.proxy = proxy
        self.ssl_verify = ssl_verify
        self.follow_redirects = follow_redirects
        self.cache_ttl = cache_ttl
        self.compression = compression