class GroupHelper:
    def __init__(self, web_driver):
        self.web_driver = web_driver

    def create(self, group):
        wd = self.web_driver
        self.open_groups_page()
        wd.find_element_by_name("new").click()
        self.fill_group_form(group)
        # подтверждение создания группы
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()

    def fill_group_form(self, group):
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

    def change_field_value(self, field_name, text):
        wd = self.web_driver
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def open_groups_page(self):
        wd = self.web_driver
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("groups").click()

    def delete_first_group(self):
        wd = self.web_driver
        self.open_groups_page()
        # select first group
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()

    def get_group_list(self):
        # получаем список групп
        wd = self.web_driver
        self.open_groups_page()
        list = wd.find_elements_by_class_name("group")
        self.return_to_home_page()
        return list

    def select_first_group(self):
        wd = self.web_driver
        wd.find_element_by_name("selected[]").click()

    def modify_first_group(self, new_group_data):
        wd = self.web_driver
        self.open_groups_page()
        self.select_first_group()
        # open modification form
        wd.find_element_by_name("edit").click()
        # fill group form
        self.fill_group_form(new_group_data)
        # submit modification
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()

    def return_to_groups_page(self):
        wd = self.web_driver
        wd.find_element_by_link_text("group page").click()

    def return_to_home_page(self):
        wd = self.web_driver
        wd.find_element_by_link_text("home").click()
