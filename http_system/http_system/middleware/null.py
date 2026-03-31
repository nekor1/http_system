class NullMiddleware:
    def execute(self, request):
        return "no middleware executed"