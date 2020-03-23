# -*- coding: utf-8 -*-
import pytest
from group import Group
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group_redfox(app):
    app.session.login(username="admin", password="secret")
    app.create_group(Group(name="222", header="333", footer="444"))
    app.session.logout()


def test_add_empty_group_redfox(app):
    app.session.login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.session.logout()
