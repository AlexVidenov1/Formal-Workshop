class Comment:
    CONTENT_LEN_MIN = 3
    CONTENT_LEN_MAX = 200
    CONTENT_LEN_ERR = f'Content must be between {CONTENT_LEN_MIN} and {CONTENT_LEN_MAX} characters long!'

    # Todo: Finish the implementation
    # Names of methods/attributes should be exactly match those in the README file

    def __init__(self, user, content):
        self.user = user
        self.content = content

    def validate(self):
        if len(self.content) < Comment.CONTENT_LEN_MIN or len(self.content) > Comment.CONTENT_LEN_MAX:
            raise ValueError(Comment.CONTENT_LEN_ERR)
