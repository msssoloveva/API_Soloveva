import pytest
from api.delete_notes import DeleteNotes
from api.get_notes import GetNotes
from api.post_notes import PostNotes
from api.post_authorization import PostAuthorization
from api.post_registration import PostRegistration


@pytest.fixture
def user_registration_post():
    return PostRegistration()


@pytest.fixture
def user_authorization_login():
    return PostAuthorization()


@pytest.fixture
def token(user_authorization_login):
    return user_authorization_login.get_token()


@pytest.fixture
def get_notes(token):
    return GetNotes(token)


@pytest.fixture
def post_notes(token):
    return PostNotes(token)


@pytest.fixture
def create_note(post_notes):
    return post_notes.creating_note()


@pytest.fixture
def get_note_id_by_title(get_notes):
    def _get_id(title: str):
        note_id = get_notes.get_notes_id(title=title)
        return note_id

    return _get_id


@pytest.fixture
def delete_note(token):
    return DeleteNotes(token=token)


@pytest.fixture
def deleting_notes(delete_note):
    yield
    delete_note.delete_note()


@pytest.fixture
def delete_note_id_by_title(get_note_id_by_title, delete_note):
    def _delete_by_title(title: str):
        note_id = get_note_id_by_title(title)
        if note_id:
            delete_note.note_id = note_id
            response = delete_note.delete_note()
            return response
        else:
            print(f"Заметка не найдена")
            return None

    return _delete_by_title
