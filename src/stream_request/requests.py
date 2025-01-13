from dataclasses import dataclass

@dataclass
class Request:
    url: str
    method: str
    headers: dict
    body: str
    stream: bool = False

class RequestBuilder:
    url: str
    method: str
    headers: dict

    def __init__(self, url: str, method: str, headers: dict):
        self.url = url
        self.method = method
        self.headers = headers


    def build(self, options: dict):
        return Request(self.url, self.method, self.headers, **options)
