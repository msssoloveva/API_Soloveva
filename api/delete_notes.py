from api.base_api import BaseApi


class DeleteNotes(BaseApi):
    ENDPOINT = f"/api/notes"

    def __init__(self, token):
        self.token = token

    def delete_notes(self, note_id):
        response_delete = self._request(method="DELETE", note_id=note_id, need_token=True)
        return response_delete
