from selenium import webdriver

from fixture import ContactHelper
from fixture.group_helper import GroupHelper
from fixture.session_helper import SessionHelper


class Application:
    def __init__(self, browser, base_url):
        if browser == "Firefox":
            self.wd = webdriver.Firefox()
        elif browser == "Chrome":
            self.wd = webdriver.Chrome()
        elif browser == "Ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        # webdriver_firefox = webdriver.Firefox()
        # self.wd = webdriver_firefox
        self.wd.implicitly_wait(30)
        # инициализируем классы для работы с функциональностью приложения
        self.session_helper = SessionHelper(self.wd)
        self.contact_helper = ContactHelper(self.wd)
        self.group_helper = GroupHelper(self.wd)
        self.base_url = base_url

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")
        wd.get(self.base_url)

    def destroy(self):
        self.wd.quit()
