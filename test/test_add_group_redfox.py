# -*- coding: utf-8 -*-
from model.group import Group

def test_add_group_redfox(app):
    old_groups = app.group_helper.get_group_list()
    group = Group(name="222", header="333", footer="444")
    app.group_helper.create(group)
    new_groups = app.group_helper.get_group_list()
    assert len(old_groups)+1 == len(new_groups)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_add_empty_group_redfox(app):
    old_groups = app.group_helper.get_group_list()
    group = Group(name="", header="", footer="")
    app.group_helper.create(group)
    new_groups = app.group_helper.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

