from src.stream_request.requests import Request
from src.stream_request.server_mock import ServerMock


class HttpClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def fetch(self, request: Request):
        if request.stream:
            raise Exception("Use fetchStream instead")

        return ServerMock.handle(request)

    def fetchStream(self, request: Request):
        if not request.stream:
            raise Exception("Use fetch instead")

        return ServerMock.handle(request)