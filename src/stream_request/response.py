from dataclasses import dataclass

@dataclass
class Response:
    status_code: int
    body: dict


@dataclass
class ResponseBody:
    text: str

@dataclass
class StreamResponseBody:
    stream: list[str]