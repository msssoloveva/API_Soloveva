class TestUserAuthorization:
    def test_user_authorization(self, post_authorization):
        response = post_authorization.user_authorization(email="soloveva3@test.ru", password="Banan3")
        assert response.status_code == 200

    def test_user_authorization_error_email(self, post_authorization):
        response = post_authorization.user_authorization(email="", password="Banan3")
        assert response.status_code == 401
        json_response = response.json()
        assert json_response["message"] == "Ошибка авторизации... Пожалуйста, проверь почту или пароль"

    def test_user_authorization_error_password(self, post_authorization):
        response = post_authorization.user_authorization(email="soloveva3@test.ru", password="")
        assert response.status_code == 401
        json_response = response.json()
        assert json_response["message"] == "Ошибка авторизации... Пожалуйста, проверь почту или пароль"
