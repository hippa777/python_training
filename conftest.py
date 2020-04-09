import pytest
from fixture.application import Application

web_app = None


@pytest.fixture
def app():
    global web_app
    if web_app is None:
        web_app = Application()
    else:
        if not web_app.is_valid():
            web_app = Application()

    web_app.session_helper.ensure_login(username="admin", password="secret")
    return web_app


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        web_app.session_helper.ensure_logout()
        web_app.destroy()

    request.addfinalizer(fin)
    return web_app
