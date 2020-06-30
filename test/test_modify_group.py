from model.group import Group
from random import randrange

def test_modify_group_name(app):
    if app.group_helper.count() == 0:
        app.group_helper.create(Group(name="222", header="333", footer="444"))
    old_groups = app.group_helper.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="New group", header="New header", footer="New footer")
    group.id = old_groups[index].id
    app.group_helper.modify_group_by_index(index, group)
    new_groups = app.group_helper.get_group_list()
    assert len(old_groups) == len(new_groups), 'После изменения имени группы, количество групп изменено'
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)



