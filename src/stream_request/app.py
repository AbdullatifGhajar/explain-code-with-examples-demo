from src.stream_request.client import HttpClient
from src.stream_request.requests import RequestBuilder
from src.stream_request.response import ResponseBody


class App:
    request_builder: RequestBuilder
    http_client: HttpClient

    def __init__(self, request_builder: RequestBuilder, http_client: HttpClient):
        self.request_builder = request_builder
        self.http_client = http_client

    def chat(self, prompt: str):
        request = self.request_builder.build({"body": prompt})
        response = self.http_client.fetch(request)
        casted_response = ResponseBody(**response.body)

        return casted_response.text


if __name__ == "__main__":
    app = App(
        RequestBuilder("http://localhost:8080/chat", "POST", {"Content-Type": "application/json"}),
        HttpClient("localhost", 8080)
    )

    print(app.chat("Hello"))
