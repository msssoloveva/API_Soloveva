import requests

from test.data.json_for_post_registration import JsonForPostRegistration



class PostRegistration:
    BASE_URL = "http://185.240.103.201:8000"
    ENDPOINT = "/api/register"
    HEADERS = {"accept": "application/json", "Content-Type": "application/json"}

    def user_registration(self):

        response_registration = requests.post(url=f"{self.BASE_URL}{self.ENDPOINT}", headers=self.HEADERS,
                                            json=JsonForPostRegistration.data_post)

        return response_registration


registration = PostRegistration()
response = registration.user_registration()
print(f"✅ Успешно создан. Status code: {response.status_code}")
print(f"📦 Тело ответа POST: {response.json()}")

