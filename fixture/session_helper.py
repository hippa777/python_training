class SessionHelper:
    def __init__(self, wd):
        self.wd = wd

    def login(self, username, password):
        wd = self.wd
        self.open_home_page()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def logout(self):
        wd = self.wd
        wd.find_element_by_link_text("Logout").click()
        wd.find_element_by_name("user")

    def ensure_logout(self):
        if self.is_logged_in():
            self.logout()

    def is_logged_in_as(self, username):
        wd = self.wd
        return wd.find_element_by_xpath("//div[@id='top']/form/b").text == "(" + username + ")"

    def is_logged_in(self):
        wd = self.wd
        # если мы на пустой странице - мы не залогинены
        if wd.current_url == 'about:blank':
            return False

        return len(wd.find_elements_by_link_text("Logout")) > 0

    def ensure_login(self, username, password):
        if not self.is_logged_in():
            self.login(username, password)
            return

        if not self.is_logged_in_as(username):
            self.logout()
            self.login(username, password)
