from model.contact import Contact


def test_new_contact(app):
    old_contacts = app.contact_helper.get_contact_list()
    contact = Contact(firstname="Tata", middlename="Dmitrievna", lastname="Ivanova", nickname="tata",
                      company="asd-groop", address="USSR", home="111111111",
                      mobile="222222222", work="333333333", fax="444444444",
                      email="tata@tata.ru",
                      bday="17", bmonth="January", byear="2000", title="123")
    app.contact_helper.create(contact)
    new_contacts = app.contact_helper.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
