import requests

from test.data.json_for_post_authorization import JsonForPostAuthorization


class PostAuthorization:
    BASE_URL = "http://185.240.103.201:8000"
    ENDPOINT = "/api/login"
    HEADERS = {"accept": "application/json", "Content-Type": "application/json"}
    def user_authorization(self):
        response_authorization=requests.post(url=f"{self.BASE_URL}{self.ENDPOINT}", headers=self.HEADERS,
                                            json=JsonForPostAuthorization.data_authorization)
        return response_authorization

registration = PostAuthorization()
response = registration.user_authorization()
print(f"✅ Успешно создан. Status code: {response.status_code}")
print(f"📦 Тело ответа POST: {response.json()}")