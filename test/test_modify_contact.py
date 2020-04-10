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
    app.contact_helper.modify_first_contact(Contact(middlename="New middlename"))
    app.contact_helper.modify_first_contact(Contact(lastname="New lastname"))
    app.contact_helper.modify_first_contact(Contact(nickname="New nickname"))
    app.contact_helper.modify_first_contact(Contact(company="New company"))
    app.contact_helper.modify_first_contact(Contact(address="New address"))
    app.contact_helper.modify_first_contact(Contact(home="11111111"))
    app.contact_helper.modify_first_contact(Contact(mobile="22222"))
    app.contact_helper.modify_first_contact(Contact(work="33333"))
    app.contact_helper.modify_first_contact(Contact(fax="44444"))
    app.contact_helper.modify_first_contact(Contact(email="New@email"))
    app.contact_helper.modify_first_contact(Contact(title="New title"))
    app.contact_helper.modify_first_contact(Contact(bday="11"))
    app.contact_helper.modify_first_contact(Contact(bmonth='June'))
    app.contact_helper.modify_first_contact(Contact(byear='1900'))
