from model.contact import Contact
from random import randrange


def test_modify_contact_name(app):
    if app.contact_helper.count() == 0:
        app.contact_helper.create(
            Contact(firstname="Tata", middlename="Dmitrievna", lastname="Ivanova", nickname="tata",
                    company="asd-groop", address="USSR", home="111111111",
                    mobile="222222222", work="333333333", fax="444444444",
                    email="tata@tata.ru",
                    bday="17", bmonth="January", byear="2000", title="123"))
    old_contacts = app.contact_helper.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="New firstname", middlename="New middlename", lastname="New lastname",
                      nickname="New nickname", company="New company", address="New address", home="11111111",
                      mobile="22222",
                      work="33333", fax="44444", email="New@email", bday="13", bmonth="June", byear="1900",
                      title="New title")
    contact.id = old_contacts[index].id
    app.contact_helper.modify_contact_by_index(index, contact)
    new_contacts = app.contact_helper.get_contact_list()
    assert len(old_contacts) == len(new_contacts), 'После изменения имени группы, количество групп изменено'
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
