import pytest
from fixture.application import Application
import json
import os.path

web_app = None
target = None


@pytest.fixture
def app(request):
    global web_app
    global target
    browser = request.config.getoption("--browser")
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), request.config.getoption("--target"))
        with open(config_file) as f:
            target = json.load(f)
    if web_app is None or not web_app.is_valid():
        web_app = Application(browser=browser, base_url=target['baseUrl'])
    web_app.session_helper.ensure_login(username=target['username'], password=target['password'])

    return web_app


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        web_app.session.ensure_logout()
        web_app.destroy()

    request.addfinalizer(fin)
    return web_app


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--target", action="store", default="target.json")
