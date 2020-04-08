from model.contact import Contact


def test_modify_contact_firstname(app):
    app.contact_helper.modify_first_contact(Contact(firstname="New firstname"))


def test_modify_contact_middlename(app):
    app.contact_helper.modify_first_contact(Contact(middlename="New middlename"))


def test_modify_contact_lastname(app):
    app.contact_helper.modify_first_contact(Contact(lastname="New lastname"))


def test_modify_contact_nickname(app):
    app.contact_helper.modify_first_contact(Contact(nickname="New nickname"))


def test_modify_contact_company(app):
    app.contact_helper.modify_first_contact(Contact(company="New company"))


def test_modify_contact_address(app):
    app.contact_helper.modify_first_contact(Contact(address="New address"))


def test_modify_contact_home(app):
    app.contact_helper.modify_first_contact(Contact(home="11111111"))


def test_modify_contact_mobile(app):
    app.contact_helper.modify_first_contact(Contact(mobile="22222"))


def test_modify_contact_work(app):
    app.contact_helper.modify_first_contact(Contact(work="33333"))


def test_modify_contact_fax(app):
    app.contact_helper.modify_first_contact(Contact(fax="44444"))


def test_modify_contact_email(app):
    app.contact_helper.modify_first_contact(Contact(email="New@email"))


def test_modify_contact_title(app):
    app.contact_helper.modify_first_contact(Contact(title="New title"))


def test_modify_contact_bday(app):
    app.contact_helper.modify_first_contact(Contact(bday="11"))


def test_modify_contact_bmonth(app):
    app.contact_helper.modify_first_contact(Contact(bmonth='June'))


def test_modify_contact_byear(app):
    app.contact_helper.modify_first_contact(Contact(byear='1900'))
