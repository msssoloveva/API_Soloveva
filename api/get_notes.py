from api.base_api import BaseApi


class GetNotes(BaseApi):
    ENDPOINT = "/api/notes"

    def __init__(self, token):
        self.token = token

    def get_all_notes(self):
        response_all_notes = self._request(method="GET", need_token=True)
        return response_all_notes

    def get_notes_id(self, title):
        all_notes = self.get_all_notes().json()
        for note in all_notes:
            if note['title'] == title:
                return note['id']
        return None
