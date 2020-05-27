from model.group import Group


def test_delete_first_group(app):
    if len(app.group_helper.get_group_list()) == 0:
        app.group_helper.create(Group(name="222", header="333", footer="444"))

    old_groups = app.group_helper.get_group_list()
    app.group_helper.delete_first_group()
    new_groups = app.group_helper.get_group_list()
    assert len(old_groups) - 1 == len(new_groups), 'После удаления группы, количество групп не изменилось'
    old_groups[0:1] = []
    assert old_groups == new_groups

