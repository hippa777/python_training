from model.group import Group


def test_modify_group_name(app):
    if app.group_helper.count() == 0:
        app.group_helper.create(Group(name="222", header="333", footer="444"))
    old_groups = app.group_helper.get_group_list()
    group = Group(name="New group")
    group.id = old_groups[0].id
    app.group_helper.modify_first_group(group)
    new_groups = app.group_helper.get_group_list()
    assert len(old_groups) == len(new_groups), 'После изменения имени группы, количество групп изменено'
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_modify_group_header(app):
    if app.group_helper.count() == 0:
        app.group_helper.create(Group(name="222", header="333", footer="444"))
    old_groups = app.group_helper.get_group_list()
    app.group_helper.modify_first_group(Group(header="New header"))
    new_groups = app.group_helper.get_group_list()
    assert len(old_groups) == len(new_groups), 'После изменения хедера группы, количество групп изменено'


def test_modify_group_footer(app):
    if app.group_helper.count() == 0:
        app.group_helper.create(Group(name="222", header="333", footer="444"))
    old_groups = app.group_helper.get_group_list()
    app.group_helper.modify_first_group(Group(footer="New footer"))
    new_groups = app.group_helper.get_group_list()
    assert len(old_groups) == len(new_groups), 'После изменения футера группы, количество групп изменено'
