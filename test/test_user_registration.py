class TestUserRegistration:
    def test_user_registration(self, post_registration):
        response = post_registration.post_registration()
        json_response = response.json()
        assert response.status_code == 201
        assert json_response["message"] == "Успешная регистрация!"

    def test_user_already_registered(self, post_registration):
        response = post_registration.post_registration()
        json_response = response.json()
        assert response.status_code == 409
        assert json_response["message"] == "Пользователь с таким email уже существует"
