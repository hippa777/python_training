from selenium import webdriver

from python_training.fixture import ContactHelper
from python_training.fixture.group_helper import GroupHelper
from python_training.fixture.session_helper import SessionHelper


class Application:
    def __init__(self):
        webdriver_firefox = webdriver.Firefox()
        self.wd = webdriver_firefox
        self.wd.implicitly_wait(30)
        # открываем домашнюю страницу приложения
        self.open_home_page()
        # инициализируем классы для работы с функциональностью приложения
        self.contact_helper = ContactHelper(self.wd)
        self.session_helper = SessionHelper(self.wd)
        self.group_helper = GroupHelper(self.wd)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()
