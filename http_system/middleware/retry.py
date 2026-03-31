from .base import Middleware

class RetryMiddleware(Middleware):
    def execute(self, request):
        print("Retry logic")
        return super().execute(request)