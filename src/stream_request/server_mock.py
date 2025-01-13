from src.stream_request.requests import Request
from src.stream_request.response import Response


class ServerMock:
    @staticmethod
    def handle(request: Request):
        if request.stream:
            return Response(200, {"stream": ["Hello", "World", "Streamed"]})
        else:
            return Response(200, {"text": "Hello World"})