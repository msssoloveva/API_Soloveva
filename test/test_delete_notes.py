from test.data.json_for_post_notes import JsonForPostNotes


class TestDeleteNotes:
    def test_delete_note(self, delete_note_by_title, post_notes, get_notes):
        original_title = JsonForPostNotes.data_post["title"]
        JsonForPostNotes.data_post["title"] = "синий"
        JsonForPostNotes.data_post["title"] = original_title
        create_response = post_notes.creating_note()
        assert create_response.status_code == 201
        response = delete_note_by_title("синий")
        assert response.status_code == 200
