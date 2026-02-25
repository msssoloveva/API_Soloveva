from api.base_api import BaseApi


class DeleteNotes(BaseApi):
    ENDPOINT = f"/api/notes"

    def __init__(self, token):
        self.token = token
        self.note_id = None

    def delete_note(self, note_id=None):
        if note_id:
            # Используем переданный ID
            response_notes = self._request(method="DELETE", note_id=note_id, need_token=True)
        else:
            # Используем сохраненный ID
            response_notes = self._request(method="DELETE", note_id=self.note_id, need_token=True)

        return response_notes
