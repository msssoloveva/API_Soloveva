import requests

from test.data.json_for_post_notes import JsonForPostNotes

class DeleteNotes:
    BASE_URL = "http://185.240.103.201:8000"
    ENDPOINT = f"/api/notes/{note_id}"
    HEADERS = f"{'accept': 'application/json','Content-Type': 'application/json','Authorization': '{self.token}'}"

    def __init__(self, token, note_id):
        self.note_id = note_id
        self.token = token

    def headers(self):
        return {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.token}"
        }

    def delete_notes(self):
        response_notes=requests.post(url=f"{self.BASE_URL}{self.ENDPOINT}", headers=self.HEADERS,
                                            json=JsonForPostNotes.data_post)
        return response_notes