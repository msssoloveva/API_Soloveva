import requests


class GetNotes:
    BASE_URL = "http://185.240.103.201:8000"
    ENDPOINT = "/api/notes"
    HEADERS = {"accept": "application/json", "Authorization": "должна быть переменная"}
    def user_notes(self):
        response_notes=requests.get(url=f"{self.BASE_URL}{self.ENDPOINT}", headers=self.HEADERS)
        return response_notes

