from selenium.webdriver.support.select import Select


class ContactHelper:
    def __init__(self, web_driver):
        self.web_driver = web_driver

    def open_contact(self):
        wd = self.web_driver
        wd.find_element_by_link_text("add new").click()

    def create(self, contact):
        wd = self.web_driver
        self.open_contact()
        self.fill_contact_form(contact)
        # submit
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

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
        wd = self.web_driver
        self.select_first_contact()
        self.accept_next_alert = True
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()

    def select_first_contact(self):
        wd = self.web_driver
        wd.find_element_by_name("selected[]").click()

    def edit_first_contact(self):
        wd = self.web_driver
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys("Tata1")
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys("Dmitrievna2")
        wd.find_element_by_xpath("//form[@action='edit.php']").click()
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys("Ivanova3")
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys("tata4")
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys("1235")
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys("USSR6")
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys("1111111117")
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys("2222222228")
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys("3333333339")
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys("4444444440")
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys("t1ata@tata.ru")
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text("2")
        wd.find_element_by_xpath("//option[@value='2']").click()
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text("February")
        wd.find_element_by_xpath("//option[@value='February']").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys("2001")
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
        wd.find_element_by_link_text("home page").click()


    def modify_first_contact(self, new_contact_data):
        wd = self.web_driver
        self.select_first_contact()
        # open modification form
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        # fill contact form
        self.fill_contact_form(new_contact_data)
        # submit modification
        wd.find_element_by_name("update").click()
        wd.find_element_by_link_text("home page").click()
   





