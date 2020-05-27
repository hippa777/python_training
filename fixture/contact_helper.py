from selenium.webdriver.support.select import Select


class ContactHelper:
    def __init__(self, web_driver):
        self.web_driver = web_driver

    def open_contact(self):
        wd = self.web_driver
        if not (wd.current_url.endswith =="index.php"):
            wd.find_element_by_link_text("add new").click()


    def create(self, contact):
        wd = self.web_driver
        self.open_contact()
        self.fill_contact_form(contact)
        # submit
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.return_to_home_page()

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


    def return_to_home_page(self):
        wd = self.web_driver
        if not (wd.current_url.endswith ==("http://localhost/addressbook/")):
            wd.find_element_by_link_text("home").click()


    def get_contact_list(self):
        # получаем список контактов
        wd = self.web_driver
        self.return_to_home_page()
        if not (wd.current_url.endswith == ("http://localhost/addressbook/")):
            list_contact = wd.find_elements_by_class_name("center")
        return list_contact




