from .base import Middleware

class CompressionMiddleware(Middleware):
    def execute(self, request):
        print("Compressing request")
        return super().execute(request)