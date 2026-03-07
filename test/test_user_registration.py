class TestUserRegistration:
    def test_user_registration(self, user_registration_post):
        response = user_registration_post.user_registration()
        json_response = response.json()
        assert response.status_code == 201
