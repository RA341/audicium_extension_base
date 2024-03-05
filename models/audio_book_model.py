import datetime
from dataclasses import field, dataclass
from typing import List
from book_uri_model import BookUri


@dataclass
class AudioBook:
    bookUris: List[BookUri]
    coverImage: str
    bookUrl: str
    title: str
    genre: str = None
    author: str = None
    uploader: str = None
    description: str = None
    uploadDate_in_iso_format: str = None
    timeStamps: List[int] = field(default_factory=list)
    durationInSeconds: int = None
