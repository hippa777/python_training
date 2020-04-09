from model.group import Group


def test_delete_first_group(app):
    if len(app.group_helper.get_group_list()) == 0:
        app.group_helper.create(Group(name="222", header="333", footer="444"))

    app.group_helper.delete_first_group()
