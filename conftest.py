import pytest
from fixture.application import Application
import json
import os.path
import importlib
import jsonpickle

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


def pytest_generate_tests(metafunc):
    for web_app in metafunc.fixturenames:
        if web_app.startswith("data_"):
            testdata = load_from_module(web_app[5:])
        metafunc.parametrize(web_app, testdata, ids=[str(x) for x in testdata])


def load_from_module(module):
    return importlib.import_module("data.%s" % module).testdata


def load_from_json(file):
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/%s.json" % file)) as f:
        return jsonpickle.decode(f.read())
