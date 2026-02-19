from api.base_api import BaseApi
from api.post_authorization import PostAuthorization


class DeleteNotes(BaseApi):
    ENDPOINT = f"/api/notes"

    def __init__(self, token, note_id):
        self.note_id = note_id
        self.token = token

    def delete_notes(self):
        response_notes = self._request(method="DELETE", note_id=self.note_id, need_token=True)
        return response_notes


token2 = PostAuthorization().user_authorization().json()['token']
# delete_id = DeleteNotes(token2, 3407)
# response = delete_id.delete_notes()
# print(f"Успешно удален. Status code: {response.status_code}")
# print(f"Тело ответа DELETE: {response.text}")
