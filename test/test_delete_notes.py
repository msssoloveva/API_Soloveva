class TestDeleteNotes:
    def test_delete_note(self, take_create_note, delete_notes):
        assert take_create_note is not None
        response = delete_notes.delete_note(take_create_note)
        assert response.status_code == 200
        json_response = response.json()
        assert json_response["message"] == "Note deleted!"
        print(f"Заметка {take_create_note} успешно удалена")
