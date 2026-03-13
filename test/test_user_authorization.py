class TestUserAuthorization:
    def test_user_authorization(self, user_authorization_login):
        response = user_authorization_login.user_authorization(email="soloveva3@test.ru", password="Banan3")
        assert response.status_code == 200

    def test_token_authorization(self, user_authorization_login):
        token_auth = user_authorization_login.get_token(email="soloveva3@test.ru", password="Banan3")
        assert token_auth is not None

    def test_user_authorization_error_email(self, user_authorization_login):
        response = user_authorization_login.user_authorization(email="", password="Banan3")
        assert response.status_code == 401
        json_response = response.json()
        assert json_response["message"] == "Ошибка авторизации... Пожалуйста, проверь почту или пароль"

    def test_user_authorization_error_password(self, user_authorization_login):
        response = user_authorization_login.user_authorization(email="soloveva3@test.ru", password="")
        assert response.status_code == 401
        json_response = response.json()
        assert json_response["message"] == "Ошибка авторизации... Пожалуйста, проверь почту или пароль"
