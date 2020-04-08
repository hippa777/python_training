# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group_redfox(app):
    app.group_helper.create(Group(name="222", header="333", footer="444"))


def test_add_empty_group_redfox(app):
    app.group_helper.create(Group(name="", header="", footer=""))
