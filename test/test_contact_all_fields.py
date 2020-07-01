from model.contact import Contact
from random import randrange
import re


def test_contact_all_fields_contact(app):
    if app.contact_helper.count() == 0:
        app.contact_helper.create(
            Contact(firstname="Tata", middlename="Dmitrievna", lastname="Ivanova", nickname="tata",
                    company="asd-groop", address="USSR", home="111111111",
                    mobile="222222222", work="333333333", fax="444444444",
                    email="tata@tata.ru", email2="tata@mail.ru", email3="tata@gg.ru", address2="USSA Bali",
                    phone2="77777777777",
                    bday="17", bmonth="January", byear="2000", title="123"))
        all_contacts = app.contact_helper.get_contact_list()
        index = randrange(len(all_contacts))
        contact = all_contacts[index]
        contact_from_edit_page = app.contact_helper.get_contact_info_from_edit_page(index)
        assert contact.firstname == contact_from_edit_page.firstname
        assert contact.lastname == contact_from_edit_page.lastname
        assert contact.all_phones_from_home_page == app.contact_helper.merge_phones_like_on_home_page(
            contact_from_edit_page)
        assert contact.all_email == app.contact_helper.merge_emails_like_on_home_page(contact_from_edit_page)
        assert contact.address == contact_from_edit_page.address


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(
        filter(lambda x: x != "", map(lambda x: clear(x), filter(lambda x: x is not None,
                                                                 [contact.home, contact.work, contact.mobile,
                                                                  contact.phone2]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            filter(lambda x: x is not None, [contact.email, contact.email1, contact.email2])))
