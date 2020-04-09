from selenium import webdriver

from fixture import ContactHelper
from fixture.group_helper import GroupHelper
from fixture.session_helper import SessionHelper


class Application:
    def __init__(self):
        webdriver_firefox = webdriver.Firefox()
        self.wd = webdriver_firefox
        # инициализируем классы для работы с функциональностью приложения
        self.session_helper = SessionHelper(self.wd)
        self.contact_helper = ContactHelper(self.wd)
        self.group_helper = GroupHelper(self.wd)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def destroy(self):
        self.wd.quit()
