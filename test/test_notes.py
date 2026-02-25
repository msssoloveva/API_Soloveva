from api.post_notes import PostNotes


class TestNotes:
    def test_create_note(self, post_notes, deleting_notes, get_note_id_by_title, delete_note):
        response = post_notes.creating_note()
        json_response = response.json()
        assert response.status_code == 201
        assert json_response["message"] == "Заметка создана!"
        note_id = get_note_id_by_title("синий")
        delete_note.note_id = note_id
        delete_response = delete_note.delete_note()
        assert delete_response.status_code == 200
        print(f"Заметка успешно удалена {note_id} ")

    def test_create_note_with_invalid_token(self):
        obj_note = PostNotes("")
        response = obj_note.creating_note()
        json_response = response.json()
        assert response.status_code == 403
        assert json_response["message"] == "Token is invalid or expired!"

    def test_creating_note_without_token(self, post_notes):
        response = post_notes.creating_note_without_token()
        json_response = response.json()
        assert response.status_code == 401
        assert json_response["message"] == "Token is missing!"

    def test_get_all_notes(self, get_notes):
        response = get_notes.get_all_notes()
        json_response = response.json()
        assert response.status_code == 200
        assert type(json_response) == list
        print(json_response)

    def test_get_note_id(self, get_note_id_by_title):
        note_id = get_note_id_by_title("синий")
        assert note_id is not None
        assert isinstance(note_id, int)
        print(f"ID заметки 'синий': {note_id}")

    def test_get_note_id_non(self, get_note_id_by_title):
        note_id = get_note_id_by_title("несуществующий_title")
        assert note_id is None

    def test_delete_note_id(self, delete_note_id_by_title):
        response = delete_note_id_by_title("синий")
        assert response.status_code == 200
