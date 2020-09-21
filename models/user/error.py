class UserError(Exception):
    def __init__(self, message):
        self.message = message

class UserAlreadyExit(UserError):
    pass


class UserNotFound(UserError):
    pass


class InvalidEmailAddess(UserError):
    pass


class IncorrectPassword(UserError):
    pass