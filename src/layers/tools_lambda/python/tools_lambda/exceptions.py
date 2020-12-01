class WebResponseError(Exception):
    def __init__(self):
        super(WebResponseError, self).__init__(
            '\nThe lambda return will be a tuple with a status code and message response like: 200, "ok" ')
