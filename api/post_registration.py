from api.base_api import BaseApi
from test.data.json_for_post_registration import JsonForPostRegistration


class PostRegistration(BaseApi):
    ENDPOINT = "/api/register"

    def user_registration(self):
        response_registration = self._request(method="POST", json=JsonForPostRegistration.data_post)
        return response_registration
