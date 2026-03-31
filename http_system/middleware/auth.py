from .base import Middleware

class AuthMiddleware(Middleware):
    def execute(self, request):
        if request.auth_token:
            print("Auth applied")
        return super().execute(request)