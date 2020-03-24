# -*- coding: utf-8 -*-
from group import Group


def test_add_group_redfox(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="222", header="333", footer="444"))
    app.session.logout()


def test_add_empty_group_redfox(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()
