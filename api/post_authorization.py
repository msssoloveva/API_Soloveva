from api.base_api import BaseApi
from test.data.json_for_post_authorization import JsonForPostAuthorization


class PostAuthorization(BaseApi):
    ENDPOINT = "/api/login"

    def user_authorization(self):
        response_authorization = self._request(method="POST", json=JsonForPostAuthorization.data_authorization)
        return response_authorization

    def get_token(self):
        auth = self.user_authorization()
        return auth.json()['token']


authorization = PostAuthorization()
response = authorization.get_token()
print(f" Token Bearer: {response}")
# print(f" Тело ответа POST: {response.json()}")
