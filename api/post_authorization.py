from api.base_api import BaseApi


class PostAuthorization(BaseApi):
    ENDPOINT = "/api/login"

    def user_authorization(self, email, password):
        body = {"email": email, "password": password}
        response_authorization = self._request(method="POST", json=body)
        return response_authorization

    def get_token(self, email, password):
        auth = self.user_authorization(email, password)
        return auth.json()['token']
