def test_modify_contact(app):
    app.session_helper.login(username="admin", password="secret")
    app.contact_helper.edit_first_contact()
    app.session_helper.logout()