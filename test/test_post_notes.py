class TestPostNotes:
    def test_create_note(self, post_notes, teardown_note):
        response = post_notes.creating_note()
        json_response = response.json()
        assert response.status_code == 201
        assert json_response["message"] == "Заметка создана!"

    def test_create_note_with_invalid_token(self, teardown_note):
        obj_note = PostNotes("")
        response = obj_note.creating_note()
        json_response = response.json()
        assert response.status_code == 403
        assert json_response["message"] == "Token is invalid or expired!"

    def test_creating_note_without_token(self, post_notes, teardown_note):
        response = post_notes.creating_note_without_token()
        json_response = response.json()
        assert response.status_code == 401
        assert json_response["message"] == "Token is missing!"
