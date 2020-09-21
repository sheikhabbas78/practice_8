from dataclasses import dataclass, field
import uuid
from typing import Dict

from models.model import Model
import models.blog.error as BlogErrors


@dataclass
class BlogModel(Model):
    collection: str = field(init=False, default='blogs')
    title: str
    description: str
    author_id: str
    _id: str = field(default_factory=lambda: uuid.uuid4().hex)

    @classmethod
    def find_by_author_id(cls, author_id: str) -> "BlogModel":
        try:
            return cls.find_many_by("author_id", author_id)
        except TypeError:
            raise BlogErrors.BlogNotFound('Blog with this name not found')

    @classmethod
    def find_by_id(cls, _id: str) -> "BlogModel":
        try:
            return cls.find_one_by("_id", _id)
        except TypeError:
            raise BlogErrors.BlogNotFound('blog not found')

    @classmethod
    def find_by_title(cls, title: str) -> "BlogModel":
        try:
            return cls.find_one_by("title", title)
        except TypeError:
            raise BlogErrors.BlogNotFound('blog not found')

    def json(self) -> Dict:
        return {"_id": self._id, "author_id": self.author_id, "title": self.title, "description": self.description}

    @classmethod
    def save_blog(cls, title: str, description: str, author_id: str) -> bool:
        try:
            blog = BlogModel.find_by_title(title)
            raise BlogErrors.BlogAlreadyExit('blog with this title already exit')
        except BlogErrors.BlogNotFound:
            BlogModel(title, description, author_id).save_to_mongo()
            return True

