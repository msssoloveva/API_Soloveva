import pytest
from api.delete_notes import DeleteNotes
from api.get_notes import GetNotes
from api.post_notes import PostNotes
from api.post_authorization import PostAuthorization
from api.post_registration import PostRegistration
from test.data.json_for_post_authorization import JsonForPostAuthorization
from test.data.json_for_post_notes import JsonForPostNotes


@pytest.fixture
def user_registration_post():
    return PostRegistration()


@pytest.fixture
def user_authorization_login():
    return PostAuthorization()


@pytest.fixture
def token(user_authorization_login):
    return user_authorization_login.get_token(email=JsonForPostAuthorization.data_authorization["email"],
                                              password=JsonForPostAuthorization.data_authorization["password"])


@pytest.fixture
def post_notes(token):
    return PostNotes(token)


@pytest.fixture
def create_note(post_notes):
    return post_notes.creating_note(JsonForPostNotes.data_post["content"], JsonForPostNotes.data_post["title"])


@pytest.fixture
def get_notes(token):
    return GetNotes(token)


@pytest.fixture
def delete_notes(token):
    return DeleteNotes(token=token)


@pytest.fixture
def teardown_note(get_notes, delete_notes):
    yield
    id_note = get_notes.get_notes_id(JsonForPostNotes.data_post["title"])
    delete_notes.delete_notes(id_note)


@pytest.fixture
def setup_teardown_note(take_create_note, delete_notes):
    yield
    delete_notes.delete_notes(take_create_note)


@pytest.fixture
def take_create_note(post_notes, get_notes):
    post_notes.creating_note(JsonForPostNotes.data_post["content"], JsonForPostNotes.data_post["title"])
    id_note = get_notes.get_notes_id(JsonForPostNotes.data_post["title"])
    return id_note
