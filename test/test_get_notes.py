class TestGetNotes:
    def test_get_all_notes(self, get_notes, setup_teardown_note):
        response_getallnotes = get_notes.get_all_notes()
        json_response = response_getallnotes.json()
        assert response_getallnotes.status_code == 200
        assert type(json_response) == list
        assert len(json_response) > 0

    def test_get_note_id(self, get_note_id_by_title, setup_teardown_note):
        note_id = get_note_id_by_title
        assert note_id is not None
        assert isinstance(note_id, int)

    def test_get_note_id_non(self, get_note_id_by_title):
        note_id = get_note_id_by_title("несуществующий_title")
        assert note_id is None
