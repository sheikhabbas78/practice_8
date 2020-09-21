from dataclasses import dataclass, field
import uuid
from typing import Dict

from models.model import Model
from common.utils import Utils
import models.user.error as UserErrors


@dataclass
class UserModel(Model):
    collection: str = field(init=False, default='users')
    username: str
    email: str
    password: str
    image_name: str
    _id: str = field(default_factory=lambda: uuid.uuid4().hex)

    def json(self) -> Dict:
        return {"_id": self._id, "username": self.username, "email": self.email,
                "password": self.password, "image_name": self.image_name}

    @classmethod
    def find_by_email(cls, email: str) -> "UserModel":
        try:
            user = cls.find_one_by("email", email)
            return user
        except TypeError:
            raise UserErrors.UserNotFound('user with this email not found')



    @classmethod
    def register_user(cls, username: str, email: str, password: str, filename: str) -> bool:
        if not Utils.is_email_safe(email):
            raise UserErrors.InvalidEmailAddess('invalid email address')

        try:
            user = cls.find_by_email(email)
            raise UserErrors.UserAlreadyExit('user with this email already exits')
        except UserErrors.UserNotFound:
            UserModel(username, email, Utils.create_hashed_password(password), filename).save_to_mongo()
            return True

    @classmethod
    def login_user(cls, email: str, password: str) -> bool:
        user = UserModel.find_by_email(email)
        if not Utils.verify_password(password, user.password):
                raise UserErrors.IncorrectPassword('incorrect password')
        return True












