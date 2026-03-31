class Middleware:
    def __init__(self, next_handler):
        self.next = next_handler

    def execute(self, request):
        return self.next.execute(request)