def test_modify_group(app):
    app.session_helper.login(username="admin", password="secret")
    app.group_helper.edit_first_group()
    app.session_helper.logout()