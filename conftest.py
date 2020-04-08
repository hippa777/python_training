import pytest
from fixture.application import Application


@pytest.fixture(scope="session")
def app(request):
    fixture = Application()
    fixture.session_helper.login(username="admin", password="secret")
    def fin():
        fixture.session_helper.logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture
