from api.base_api import BaseApi


class PostNotes(BaseApi):
    ENDPOINT = "/api/notes"

    def __init__(self, token):
        self.token = token

    def creating_note(self, content, title):
        body = {"content": content, "title": title}
        response_notes = self._request(method="POST", need_token=True, json=body)
        return response_notes

    def creating_note_without_token(self, content, title):
        body = {"content": content, "title": title}
        response_notes = self._request(method="POST", json=body)
        return response_notes
