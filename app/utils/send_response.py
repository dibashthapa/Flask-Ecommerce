from abc import ABC
from flask import render_template

response_status = {
    "success": 200,
    "bad_request": 400,
    "unauthorized": 401,
    "not_found": 404,
    "internal_error": 500,
}


class Response(ABC):
    """A Response base abstract class for template response attributes"""

    status_code: str
    message: str

    def __init__(self, status_code, message):
        pass

    def send(self, template: str, *args, **kwargs):
        return render_template(template, *args, **kwargs)


class BadRequestResponse(Response):
    def __init__(self, message="Bad Request"):
        super().__init__(response_status["bad_request"], message)
        self.send("400.html")


class NotFoundResponse(Response):
    def __init__(self, message="Not Found"):
        super().__init__(response_status["not_found"], message)
        self.send("404.html")


class InternalErrorResponse(Response):
    def __init__(self, message="Internal Error"):
        super().__init__(response_status["internal_error"], message)
        self.send("500.html")
