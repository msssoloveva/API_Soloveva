class TestGetNotes:
    def test_get_all_notes(self, get_notes, create_and_delete_note):
        response_getallnotes = get_notes.get_all_notes()
        json_response = response_getallnotes.json()
        assert response_getallnotes.status_code == 200
        assert isinstance(json_response, list)
        assert len(json_response) > 0

    def test_get_note_id(self, get_notes, create_and_delete_note):
        note_id = get_notes.get_notes_id("рулон")
        assert note_id is not None
        assert isinstance(note_id, int)


    def test_get_note_without_token(self, get_notes, create_and_delete_note):
        response = get_notes.get_notes_without_token()
        json_response = response.json()
        assert response.status_code == 401
        assert json_response["message"] == "Token is missing!"
