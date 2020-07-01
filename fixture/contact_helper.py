from selenium.webdriver.support.select import Select
from model.contact import Contact
import re


class ContactHelper:
    def __init__(self, web_driver):
        self.web_driver = web_driver

    def open_contact(self):
        wd = self.web_driver
        if not (wd.current_url.endswith == "index.php"):
            wd.find_element_by_link_text("add new").click()

    def open_home_page(self):
        wd = self.web_driver
        if not (wd.current_url == "http://localhost/addressbook/" and len(wd.find_elements_by_name("add")) > 0):
            wd.find_element_by_link_text("home").click()

    def create(self, contact):
        wd = self.web_driver
        self.open_contact()
        self.fill_contact_form(contact)
        # submit
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.return_to_home_page()
        self.contact_cache = None

    def fill_contact_form(self, contact):
        wd = self.web_driver
        self.change_field_value_contact("firstname", contact.firstname)
        self.change_field_value_contact("middlename", contact.middlename)
        self.change_field_value_contact("lastname", contact.lastname)
        self.change_field_value_contact("nickname", contact.nickname)
        self.change_field_value_contact("title", contact.title)
        self.change_field_value_contact("company", contact.company)
        self.change_field_value_contact("address", contact.address)
        self.change_field_value_contact("home", contact.home)
        self.change_field_value_contact("mobile", contact.mobile)
        self.change_field_value_contact("work", contact.work)
        self.change_field_value_contact("fax", contact.fax)
        self.change_field_value_contact("email", contact.email)
        self.change_field_value_contact("byear", contact.byear)

        self.change_field_selected_value("bday", contact.bday)
        self.change_field_selected_value("bmonth", contact.bmonth)

    def change_field_value_contact(self, field_name, text):
        wd = self.web_driver
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def change_field_selected_value(self, field_name, field_value):
        wd = self.web_driver
        if field_value is None:
            return

        if field_name is None:
            raise Exception('ТЕКСТ ОШИБКИ!')

        wd.find_element_by_name(field_name).click()
        Select(wd.find_element_by_name(field_name)).select_by_visible_text(field_value)
        wd.find_element_by_xpath(f'//option[@value=\'{field_value}\']').click()

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.web_driver
        self.select_contact_by_index(index)
        # self.accept_next_alert = True
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.open_home_page()
        self.contact_cache = None

    def select_first_contact(self):
        wd = self.web_driver
        wd.find_element_by_name("selected[]").click()

    def select_contact_by_index(self, index):
        wd = self.web_driver
        wd.find_elements_by_name("selected[]")[index].click()

    def select_contact_by_id(self, contact_id):
        wd = self.web_driver
        wd.find_element_by_css_selector("input[id='%s']" % contact_id).click()

    def modify_first_contact(self):
        self.modify_contact_by_index(0)

    def modify_contact_by_index(self, index, new_contact):
        wd = self.web_driver
        self.open_home_page()
        self.select_contact_by_index(index)
        # open modification form
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
        # fill contact form
        self.fill_contact_form(new_contact)
        # submit modification
        wd.find_element_by_name("update").click()
        wd.find_element_by_link_text("home page").click()
        self.contact_cache = None

    def return_to_home_page(self):
        wd = self.web_driver
        if not (wd.current_url.endswith == ("http://localhost/addressbook/")):
            wd.find_element_by_link_text("home").click()

    def count(self):
        wd = self.web_driver
        self.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            # получаем список контактов
            wd = self.web_driver
            self.return_to_home_page()
            self.contact_cache = []

            for element in wd.find_elements_by_css_selector("tr[name=entry]"):
                id = element.find_element_by_name("selected[]").get_attribute("value")
                first_name = element.find_element_by_css_selector("td:nth-child(3)").text
                last_name = element.find_element_by_css_selector("td:nth-child(2)").text
                all_phones = element.find_element_by_css_selector("td:nth-child(6)").text
                self.contact_cache.append(
                    Contact(firstname=first_name, lastname=last_name, id=id, all_phones_from_home_page=all_phones))
            return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):
        wd = self.web_driver
        self.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self, index):
        wd = self.web_driver
        self.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        self.open_contact_to_edit_by_index(index)
        wd = self.web_driver
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        home = wd.find_elements_by_name("home").get_attribute("value")
        work = wd.find_elements_by_name("work").get_attribute("value")
        mobile = wd.find_elements_by_name("mobile").get_attribute("value")
        phone2 = wd.find_elements_by_name("phone2").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, address=address, id=id, home=home, work=work,
                       mobile=mobile, phone2=phone2)

    def get_contact_from_view_page(self, index):
        wd = self.web_driver
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        home = re.search("H: (.*)", text).group(1)
        work = re.search("W: (.*)", text).group(1)
        mobile = re.search("M: (.*)", text).group(1)
        phone2 = re.search("P: (.*)", text).group(1)
        return Contact(home=home, work=work, mobile=mobile, phone2=phone2)

