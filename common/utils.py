import re
from passlib.hash import pbkdf2_sha512

class Utils:

    @staticmethod
    def is_email_safe(email: str) ->bool:
        email_address_matcher = re.compile(r'^[\w-]+@([\w-]+\.)+[\w]+$')
        return True if email_address_matcher.match(email) else False

    @staticmethod
    def create_hashed_password(password: str) -> str:
        return pbkdf2_sha512.encrypt(password)

    @staticmethod
    def verify_password(password: str, hashed_password: str) ->bool:
        return pbkdf2_sha512.verify(password, hashed_password)