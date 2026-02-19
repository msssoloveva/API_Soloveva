import pytest
import requests

from api.delete_notes import DeleteNotes
from api.get_notes import GetNotes
from api.post_notes import PostNotes
from api.post_authorization import PostAuthorization
from api.post_registration import PostRegistration
from test.data.json_for_post_registration import JsonForPostRegistration
from test.data.json_for_post_notes import JsonForPostNotes


@pytest.fixture
def post_registration():
    return PostRegistration()


@pytest.fixture
def post_authorization():
    return PostAuthorization()


@pytest.fixture
def token(post_authorization):
    return post_authorization.get_token()


@pytest.fixture
def get_notes(token):
    return GetNotes(token)


@pytest.fixture
def post_notes(token):
    return PostNotes(token)


@pytest.fixture
def create_note(post_notes):
    return post_notes.create_note()


@pytest.fixture
def id_note(create_note, get_notes):
    return get_notes.get_notes_id(title=JsonForPostNotes.data_post["title"])


@pytest.fixture
def delete_notes(token, id_notes):
    return DeleteNotes(token=token, note_id=id_notes)

# @pytest.fixture
# def notes_id():
#     return JsonForPostNotes.data_post()
# @pytest.fixture
# def registration_data():
#     return JsonForPostRegistration.data_post.copy()

# @pytest.fixture
# def new_post_registration():
#     return {
#     "email": "soloveva@test.ru",
#     "password": "Banan1234",
#     "username": "Svetlana"
#     }
