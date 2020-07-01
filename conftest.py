import pytest
from fixture.application import Application

web_app = None


@pytest.fixture(scope="session")
def app(request):
    global web_app
    browser = request.config.getoption("--browser")
    base_url = request.config.getoption("--baseUrl")
    if web_app is None:
        web_app = Application(browser=browser, base_url=base_url)
    else:
        if not web_app.is_valid():
            web_app = Application(browser=browser, base_url=base_url)

    web_app.session_helper.ensure_login(username="admin", password="secret")

    return web_app


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        web_app.session_helper.ensure_logout()
        web_app.destroy()

    request.addfinalizer(fin)
    return web_app


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--baseUrl", action="store", default="http: // localhost / addressbook /")
