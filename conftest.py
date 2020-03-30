import pytest
from python_training.fixture.application import Application


@pytest.fixture(scope="session")
def app(request):
    application = Application()
    request.addfinalizer(application.destroy)
    return application
