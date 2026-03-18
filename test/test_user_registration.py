class TestUserRegistration:
    def test_user_registration(self, user_registration):
        response = user_registration.user_registration(email="soloveva3@test.ru", password="Banan3",
                                                            username="Svetlana3")
        json_response = response.json()
        assert response.status_code == 201
        assert json_response["message"] == "Успешная регистрация!"

    def test_user_already_registered(self, user_registration):
        response = user_registration.user_registration(email="soloveva3@test.ru", password="Banan3",
                                                            username="Svetlana3")
        json_response = response.json()
        assert response.status_code == 409
        assert json_response["message"] == "Пользователь с таким email уже существует"
