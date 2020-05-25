# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group_redfox(app):
    old_groups = app.group_helper.get_group_list()
    app.group_helper.create(Group(name="222", header="333", footer="444"))
    new_groups = app.group_helper.get_group_list()
    assert len(old_groups)+1 == len (new_groups)


def test_add_empty_group_redfox(app):
    old_groups = app.group_helper.get_group_list()
    app.group_helper.create(Group(name="", header="", footer=""))
    new_groups = app.group_helper.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
