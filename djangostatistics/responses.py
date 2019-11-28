from django.http import JsonResponse


class SuccessJsonResponse(JsonResponse):
    status_code = 200

    def __init__(self, response=None, *args, **kwargs):
        if response is None:
            super().__init__({}, *args, **kwargs)
        else:
            super().__init__(response, *args, **kwargs)


class AbstractFailureJsonResponse(JsonResponse):
    reason = None

    def __init__(self, *args, **kwargs):
        super().__init__({
            "reason": self.reason
        }, *args, **kwargs)


class IncorrectAccessMethod(AbstractFailureJsonResponse):
    reason = "incorrect_access_method"
    status_code = 405


class MalformedJson(AbstractFailureJsonResponse):
    reason = "malformed_json"
    status_code = 400
