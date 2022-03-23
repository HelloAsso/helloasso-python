from unittest.mock import Mock

from requests import Response


class FakeResponse(Response):
    def __init__(self, data, status_code=200):
        self.data = data
        self.status_code = status_code

    def json(self) -> dict:
        return self.data


class FakeErrorResponse(object):
    def __init__(self, status_code):
        self.request = {"method": 123}
        self.reason = "reason"
        self.status_code = status_code
        self.method = "method"
        self.url = "url"
        self.path_url = "path_url"
        self.headers = "headers"
        self.body = "body"
        self.content = "content"


class IterErrorRaiser(object):
    """Raise error until X retry"""

    def __init__(self, status_code, max_retry):
        self.max_retry = max_retry
        self.status_code = status_code
        self.retry = 0
        self.get = Mock(side_effect=self._get)

    def _get(self, *args, **kwargs):
        if self.retry == self.max_retry:
            return FakeResponse({})
        else:
            self.retry += 1
            return FakeErrorResponse(self.status_code)
