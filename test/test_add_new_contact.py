# -*- coding: utf-8 -*-
import pytest
from contact import Contact
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_new_contact(app):
    app.session.login(username="admin", password="secret")
    app.create_new_contact(Contact(firstname="Tata", middlename="Dmitrievna", lastname="Ivanova", nickname="tata",
                                   company="asd-groop", address="USSR", homephone="111111111",
                                   mobile="222222222", workphone="333333333", fax="444444444",
                                   email="tata@tata.ru",
                                   bday="17", bmonth="January", byear="2000", title="123"))
    app.session.logout()
