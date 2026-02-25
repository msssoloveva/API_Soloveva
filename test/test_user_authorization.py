class TestUserAuthorization:
    def test_user_authorization(self, user_authorization_login):
        response = user_authorization_login.user_authorization()
        assert response.status_code == 200
        print(response.status_code)

    def test_token_authorization(self, user_authorization_login):
        token_auth = user_authorization_login.get_token()
        assert token_auth is not None
        print(token_auth)
