class PostError(Exception):
    def __init__(self, message):
        self.message = message

class PostNotFound(PostError):
    pass

class PostAlreadyExit(PostError):
    pass
