import requests

from test.data.json_for_post_notes import JsonForPostNotes

class PostNotes:
    BASE_URL = "http://185.240.103.201:8000"
    ENDPOINT = "/api/notes"
    HEADERS = {"accept": "application/json","Content-Type": "application/json","Authorization": "должна быть переменная"}
    def user_notes(self):
        response_notes=requests.post(url=f"{self.BASE_URL}{self.ENDPOINT}", headers=self.HEADERS,
                                            json=JsonForPostNotes.data_post)
        return response_notes