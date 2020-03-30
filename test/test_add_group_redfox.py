# -*- coding: utf-8 -*-
from python_training.model.group import Group


def test_add_group_redfox(app):
    app.session_helper.login(username="admin", password="secret")
    app.group_helper.create(Group(name="222", header="333", footer="444"))
    app.session_helper.logout()


def test_add_empty_group_redfox(app):
    app.session_helper.login(username="admin", password="secret")
    app.group_helper.create(Group(name="", header="", footer=""))
    app.session_helper.logout()
