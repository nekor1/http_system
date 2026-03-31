from .base import Middleware

class LoggingMiddleware(Middleware):
    def execute(self, request):
        print("Logging request")
        return super().execute(request)