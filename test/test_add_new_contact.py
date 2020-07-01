from model.contact import Contact
import pytest
import random
import string
from random import randint


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_phone():
    symbols = string.digits
    first = random.randint(1, 9)
    return str(first) + ''.join([random.choice(symbols)*8])


def random_email():
    symbols = string.ascii_letters + string.digits
    return "".join([random.choice(symbols) for i in range(random.randrange(3, 7, 1))]) + "@" + "".join(
        [random.choice(symbols) for i in range(random.randrange(3, 7, 1))]) + "." + "".join(
        [random.choice(symbols) for i in range(random.randrange(3, 7, 1))])


testdata = [
    Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 15),
            lastname=random_string("lastname", 15), nickname=random_string("nickname", 10),
            company=random_string("company", 20), address=random_string("address", 20),
            home=random_phone(),
            mobile=random_phone(), work=random_phone(), fax=random_phone(), email=random_email(),
            email2=random_email(), email3=random_email(),
            address2=random_string("address2", 15)) for i in
    range(5)
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_new_contact(app, contact):
    old_contacts = app.contact_helper.get_contact_list()
    app.contact_helper.create(contact)
    n = app.contact_helper.count()
    assert len(old_contacts) + 1 == n
    new_contacts = app.contact_helper.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
