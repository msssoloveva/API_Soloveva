from api.base_api import BaseApi
from test.data.json_for_post_notes import JsonForPostNotes


class PostNotes(BaseApi):
    ENDPOINT = "/api/notes"

    def __init__(self, token):
        self.token = token

    def creating_note(self):
        response_notes = self._request(method="POST", need_token=True, json=JsonForPostNotes.data_post)
        return response_notes

    def creating_note_without_token(self):
        response_notes = self._request(method="POST", json=JsonForPostNotes.data_post)
        return response_notes
