class TestDeleteNotes:
    def test_delete_note(self, take_create_note, delete_notes):
        note_id = take_create_note
        response = delete_notes.delete_note(note_id)
        assert response.status_code == 200
        json_response = response.json()
        assert json_response["message"] == "Note deleted!"
        print(f"Заметка {note_id} успешно удалена")
