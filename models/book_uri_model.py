from dataclasses import dataclass


@dataclass
class BookUri:
    title: str
    uri: str
    file_uri: str
    duration: str
