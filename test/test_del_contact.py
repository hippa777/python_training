from model.contact import Contact


def test_delete_first_contact(app):
    if len(app.contact_helper.get_contact_list()) == 0:
        app.contact_helper.create(
            Contact(firstname="Tata", middlename="Dmitrievna", lastname="Ivanova", nickname="tata",
                    company="asd-groop", address="USSR", home="111111111",
                    mobile="222222222", work="333333333", fax="444444444",
                    email="tata@tata.ru",
                    bday="17", bmonth="January", byear="2000", title="123"))

    app.contact_helper.delete_first_contact()
