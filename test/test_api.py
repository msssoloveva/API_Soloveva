from api.post_notes import PostNotes


class TestApi:
    # def test_user_registration(self,post_registration):
    #     response = post_registration.user_registration()
    #     json_response = response.json()
    #     assert response.status_code == 201
    #     print(response.status_code)
    #     print(json_response)
    #
    # def test_user_authorization(self,):
    #     response = post_authorization.user_authorization()
    #     assert response.status_code == 200
    #     print(response.status_code)

    def test_create_note(self,post_notes, deleting_notes):
        response = post_notes.creating_note()
        json_response = response.json()
        assert response.status_code == 201
        assert json_response["message"] == "Заметка создана!"

        # удалить за собой заметку но в фикстуре, сделать динамичную фикстуру получения id заметки по title
        # , возможно нужно будет после yield


    def test_create_note_with_invalid_token(self):
        obj_note = PostNotes("")
        response = obj_note.creating_note()
        json_response = response.json()
        assert response.status_code == 403
        assert json_response["message"] == "Token is invalid or expired!"

    def test_creating_note_without_token(self,post_notes):
        response = post_notes.creating_note_without_token()
        json_response = response.json()
        assert response.status_code == 401
        assert json_response["message"] == "Token is missing!"





    # def test_get_notes(self,post_notes):
    #     response = post_notes.get_notes()
    #     json_response = response.json()

    # def test_test_authorization(self,post_authorization):
    #     assert token is not None
    #     print(token)