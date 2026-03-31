class RequestExecutor:
    def execute(self, request):
        raise NotImplementedError


class BaseHttpClient(RequestExecutor):
    def execute(self, request):
        print(f"Sending {request.method} request to {request.url}")
        return f"response from {request.url}"