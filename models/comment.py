from dataclasses import dataclass
from typing import Dict, List

from models.model import Model

@dataclass
class CommentModel(Model):
    post_id: str
    username: str
    comment: str

    def json(self) -> Dict:
        return {"_id": self._id, "post_id": self.post_id, "username": self.username, "comment": self.comment}

    @classmethod
    def find_by_post_id(cls, post_id) -> List["CommentModel"]:
        comments = CommentModel.find_many_by("post_id", post_id)
        return [cls(**comment) for comment in comments]
