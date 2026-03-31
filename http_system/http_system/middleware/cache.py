from .base import Middleware

class CacheMiddleware(Middleware):
    def execute(self, request):
        print("Checking cache")
        return super().execute(request)