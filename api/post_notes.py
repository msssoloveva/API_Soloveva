from api.base_api import BaseApi
from api.post_authorization import PostAuthorization
from test.data.json_for_post_notes import JsonForPostNotes


class PostNotes(BaseApi):
    ENDPOINT = "/api/notes"

    def __init__(self, token):
        self.token = token

    def create_note(self):
        response_notes = self._request(method="POST", need_token=True, json=JsonForPostNotes.data_post)
        return response_notes

# token3 = PostAuthorization().user_authorization().json()['token']
# note = PostNotes(token3)
# add_create_note = note.create_note()
# print(f"Status code: {add_create_note.status_code}")
# print(f"Ответ: {add_create_note.json()}")
