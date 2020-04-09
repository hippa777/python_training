from model.contact import Contact


def test_modify_contact_firstname(app):
    if len(app.contact_helper.get_contact_list()) == 0:
        app.contact_helper.create(
            Contact(firstname="Tata", middlename="Dmitrievna", lastname="Ivanova", nickname="tata",
                    company="asd-groop", address="USSR", home="111111111",
                    mobile="222222222", work="333333333", fax="444444444",
                    email="tata@tata.ru",
                    bday="17", bmonth="January", byear="2000", title="123"))
    app.contact_helper.modify_first_contact(Contact(firstname="New firstname"))


def test_modify_contact_middlename(app):
    if len(app.contact_helper.get_contact_list()) == 0:
        app.contact_helper.create(
            Contact(firstname="Tata", middlename="Dmitrievna", lastname="Ivanova", nickname="tata",
                    company="asd-groop", address="USSR", home="111111111",
                    mobile="222222222", work="333333333", fax="444444444",
                    email="tata@tata.ru",
                    bday="17", bmonth="January", byear="2000", title="123"))
    app.contact_helper.modify_first_contact(Contact(middlename="New middlename"))


def test_modify_contact_lastname(app):
    if len(app.contact_helper.get_contact_list()) == 0:
        app.contact_helper.create(
            Contact(firstname="Tata", middlename="Dmitrievna", lastname="Ivanova", nickname="tata",
                    company="asd-groop", address="USSR", home="111111111",
                    mobile="222222222", work="333333333", fax="444444444",
                    email="tata@tata.ru",
                    bday="17", bmonth="January", byear="2000", title="123"))
    app.contact_helper.modify_first_contact(Contact(lastname="New lastname"))


def test_modify_contact_nickname(app):
    if len(app.contact_helper.get_contact_list()) == 0:
        app.contact_helper.create(
            Contact(firstname="Tata", middlename="Dmitrievna", lastname="Ivanova", nickname="tata",
                    company="asd-groop", address="USSR", home="111111111",
                    mobile="222222222", work="333333333", fax="444444444",
                    email="tata@tata.ru",
                    bday="17", bmonth="January", byear="2000", title="123"))
    app.contact_helper.modify_first_contact(Contact(nickname="New nickname"))


def test_modify_contact_company(app):
    if len(app.contact_helper.get_contact_list()) == 0:
        app.contact_helper.create(
            Contact(firstname="Tata", middlename="Dmitrievna", lastname="Ivanova", nickname="tata",
                    company="asd-groop", address="USSR", home="111111111",
                    mobile="222222222", work="333333333", fax="444444444",
                    email="tata@tata.ru",
                    bday="17", bmonth="January", byear="2000", title="123"))
    app.contact_helper.modify_first_contact(Contact(company="New company"))


def test_modify_contact_address(app):
    if len(app.contact_helper.get_contact_list()) == 0:
        app.contact_helper.create(
            Contact(firstname="Tata", middlename="Dmitrievna", lastname="Ivanova", nickname="tata",
                    company="asd-groop", address="USSR", home="111111111",
                    mobile="222222222", work="333333333", fax="444444444",
                    email="tata@tata.ru",
                    bday="17", bmonth="January", byear="2000", title="123"))
    app.contact_helper.modify_first_contact(Contact(address="New address"))


def test_modify_contact_home(app):
    if len(app.contact_helper.get_contact_list()) == 0:
        app.contact_helper.create(
            Contact(firstname="Tata", middlename="Dmitrievna", lastname="Ivanova", nickname="tata",
                    company="asd-groop", address="USSR", home="111111111",
                    mobile="222222222", work="333333333", fax="444444444",
                    email="tata@tata.ru",
                    bday="17", bmonth="January", byear="2000", title="123"))
    app.contact_helper.modify_first_contact(Contact(home="11111111"))


def test_modify_contact_mobile(app):
    if len(app.contact_helper.get_contact_list()) == 0:
        app.contact_helper.create(
            Contact(firstname="Tata", middlename="Dmitrievna", lastname="Ivanova", nickname="tata",
                    company="asd-groop", address="USSR", home="111111111",
                    mobile="222222222", work="333333333", fax="444444444",
                    email="tata@tata.ru",
                    bday="17", bmonth="January", byear="2000", title="123"))
    app.contact_helper.modify_first_contact(Contact(mobile="22222"))


def test_modify_contact_work(app):
    if len(app.contact_helper.get_contact_list()) == 0:
        app.contact_helper.create(
            Contact(firstname="Tata", middlename="Dmitrievna", lastname="Ivanova", nickname="tata",
                    company="asd-groop", address="USSR", home="111111111",
                    mobile="222222222", work="333333333", fax="444444444",
                    email="tata@tata.ru",
                    bday="17", bmonth="January", byear="2000", title="123"))
    app.contact_helper.modify_first_contact(Contact(work="33333"))


def test_modify_contact_fax(app):
    if len(app.contact_helper.get_contact_list()) == 0:
        app.contact_helper.create(
            Contact(firstname="Tata", middlename="Dmitrievna", lastname="Ivanova", nickname="tata",
                    company="asd-groop", address="USSR", home="111111111",
                    mobile="222222222", work="333333333", fax="444444444",
                    email="tata@tata.ru",
                    bday="17", bmonth="January", byear="2000", title="123"))
    app.contact_helper.modify_first_contact(Contact(fax="44444"))


def test_modify_contact_email(app):
    if len(app.contact_helper.get_contact_list()) == 0:
        app.contact_helper.create(
            Contact(firstname="Tata", middlename="Dmitrievna", lastname="Ivanova", nickname="tata",
                    company="asd-groop", address="USSR", home="111111111",
                    mobile="222222222", work="333333333", fax="444444444",
                    email="tata@tata.ru",
                    bday="17", bmonth="January", byear="2000", title="123"))
    app.contact_helper.modify_first_contact(Contact(email="New@email"))


def test_modify_contact_title(app):
    if len(app.contact_helper.get_contact_list()) == 0:
        app.contact_helper.create(
            Contact(firstname="Tata", middlename="Dmitrievna", lastname="Ivanova", nickname="tata",
                    company="asd-groop", address="USSR", home="111111111",
                    mobile="222222222", work="333333333", fax="444444444",
                    email="tata@tata.ru",
                    bday="17", bmonth="January", byear="2000", title="123"))
    app.contact_helper.modify_first_contact(Contact(title="New title"))


def test_modify_contact_bday(app):
    if len(app.contact_helper.get_contact_list()) == 0:
        app.contact_helper.create(
            Contact(firstname="Tata", middlename="Dmitrievna", lastname="Ivanova", nickname="tata",
                    company="asd-groop", address="USSR", home="111111111",
                    mobile="222222222", work="333333333", fax="444444444",
                    email="tata@tata.ru",
                    bday="17", bmonth="January", byear="2000", title="123"))
    app.contact_helper.modify_first_contact(Contact(bday="11"))


def test_modify_contact_bmonth(app):
    if len(app.contact_helper.get_contact_list()) == 0:
        app.contact_helper.create(
            Contact(firstname="Tata", middlename="Dmitrievna", lastname="Ivanova", nickname="tata",
                    company="asd-groop", address="USSR", home="111111111",
                    mobile="222222222", work="333333333", fax="444444444",
                    email="tata@tata.ru",
                    bday="17", bmonth="January", byear="2000", title="123"))
    app.contact_helper.modify_first_contact(Contact(bmonth='June'))


def test_modify_contact_byear(app):
    if len(app.contact_helper.get_contact_list()) == 0:
        app.contact_helper.create(
            Contact(firstname="Tata", middlename="Dmitrievna", lastname="Ivanova", nickname="tata",
                    company="asd-groop", address="USSR", home="111111111",
                    mobile="222222222", work="333333333", fax="444444444",
                    email="tata@tata.ru",
                    bday="17", bmonth="January", byear="2000", title="123"))
    app.contact_helper.modify_first_contact(Contact(byear='1900'))
