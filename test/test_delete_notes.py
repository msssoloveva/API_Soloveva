class TestDeleteNotes:
    def test_delete_note(self, take_create_note, delete_notes):
        note_id = take_create_note
        assert note_id is not None
        response = delete_notes.delete_notes(note_id)
        assert response.status_code == 200
        json_response = response.json()
        assert json_response["message"] == "Note deleted!"
        print(f"Заметка {note_id} успешно удалена")

    def test_delete_all_notes(self, get_notes, delete_notes):
        response = get_notes.get_all_notes()
        assert response.status_code == 200
        all_notes = response.json()
        if len(all_notes) < 1:
            print("Нет заметок для удаления")
            return
        deleted_count = 0
        for note in all_notes:
            note_id = note["id"]
            delete_response = delete_notes.delete_notes(note_id)
            if delete_response.status_code == 200:
                deleted_count += 1
                print(f" Удалена заметка ID: {note_id}")
        print(f"Всего удалено: {deleted_count} из {len(all_notes)}")
