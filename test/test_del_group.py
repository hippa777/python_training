def test_delete_first_group(app):
    app.session_helper.login(username="admin", password="secret")
    app.group_helper.delete_first_group()
    app.session_helper.logout()
