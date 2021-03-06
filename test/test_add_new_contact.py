from model.contact import Contact
import pytest

from data.contact import constant as testdata

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_new_contact(app, contact):
    old_contacts = app.contact_helper.get_contact_list()
    app.contact_helper.create(contact)
    n = app.contact_helper.count()
    assert len(old_contacts) + 1 == n
    new_contacts = app.contact_helper.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
