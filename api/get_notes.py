from api.base_api import BaseApi
from api.post_authorization import PostAuthorization


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


token1 = PostAuthorization().user_authorization().json()['token']
# get_all = GetNotes(token1)
# all_notes = get_all.get_all_notes()
# print(f"Успешно получены все заметки. Status code: {all_notes.status_code}")
# print(f"Тело ответа всех заметок: {all_notes.json()}")
# get_id = GetNotes(token1).get_notes_id('синий')
# print(f"Успешно получена заметка id: {get_id}")
