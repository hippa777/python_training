def test_delete_first_contact(app):
    app.session_helper.login(username="admin", password="secret")
    app.contact_helper.delete_first_contact()
    app.session_helper.logout()