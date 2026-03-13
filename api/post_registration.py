from api.base_api import BaseApi


class PostRegistration(BaseApi):
    ENDPOINT = "/api/register"

    def user_registration(self, email, password, username):
        body = {"email": email, "password": password, "username": username}
        response_registration = self._request(method="POST", json=body)
        return response_registration
