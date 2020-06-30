from model.contact import Contact
from random import randrange


def test_delete_some_contact(app):
    if app.contact_helper.count() == 0:
        app.contact_helper.create(
            Contact(firstname="Tata", middlename="Dmitrievna", lastname="Ivanova", nickname="tata",
                    company="asd-groop", address="USSR", home="111111111",
                    mobile="222222222", work="333333333", fax="444444444",
                    email="tata@tata.ru",
                    bday="17", bmonth="January", byear="2000", title="123"))

    old_contacts = app.contact_helper.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact_helper.delete_contact_by_index(index)
    new_contacts = app.contact_helper.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts), 'После удаления контакта, количество контактов не изменилось'
    old_contacts[index:index+1] = []
    assert old_contacts == new_contacts
