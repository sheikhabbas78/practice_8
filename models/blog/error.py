class BlogError(Exception):
    def __init__(self, message):
        self.message = message


class BlogNotFound(BlogError):
    pass

class BlogAlreadyExit(BlogError):
    pass