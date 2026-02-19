class TestApi:
    def test_user_registration(self,post_registration):
        response = post_registration.user_registration()
        json_response = response.json()
        assert response.status_code == 201
        print(response.status_code)
        print(json_response)

    def test_user_authorization(self,post_authorization):
        response = post_authorization.user_authorization()
        assert response.status_code == 200
        print(response.status_code)

    def test_token_authorization(self,token):
        assert token is not None
        print(token)

    # def test_create_note(self,post_note, token):
    #     response = post_note.post_note()

    # def test_get_notes(self,post_notes):
    #     response = post_notes.get_notes()
    #     json_response = response.json()
