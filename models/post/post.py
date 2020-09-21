from dataclasses import dataclass, field
import uuid
from typing import Dict
import datetime

from models.model import Model
import models.post.error as PostErrors

@dataclass
class PostModel(Model):
    collection: str = field(init=False, default='posts')
    title: str
    content: str
    blog_id: str
    image_name: str
    like: int = field(default=0)
    dislike: int = field(default=0)
    date: str = field(default_factory=lambda: datetime.datetime.utcnow())
    _id: str = field(default_factory=lambda: uuid.uuid4().hex)

    def json(self) -> Dict:
        return {"_id": self._id, "title": self.title,
                "content": self.content, "image_name": self.image_name,
                "blog_id": self.blog_id, "date": self.date, "like": self.like, "dislike": self.dislike}

    @classmethod
    def find_by_title(cls, title: str) ->"PostModel":
        try:
            post = cls.find_one_by("title", title)
            return post
        except TypeError:
            raise PostErrors.PostNotFound('post not found')

    @classmethod
    def find_by_blog_id(cls, blog_id: str) -> "PostModel":
        posts = cls.find_many_by("blog_id", blog_id)

        return posts













