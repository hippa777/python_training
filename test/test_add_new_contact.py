from model.contact import Contact


def test_new_contact(app):
    app.contact_helper.create(
        Contact(firstname="Tata", middlename="Dmitrievna", lastname="Ivanova", nickname="tata",
                company="asd-groop", address="USSR", home="111111111",
                mobile="222222222", work="333333333", fax="444444444",
                email="tata@tata.ru",
                bday="17", bmonth="January", byear="2000", title="123"))
