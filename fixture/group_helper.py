class GroupHelper:
    def __init__(self, web_driver):
        self.web_driver = web_driver

    def create(self, group):
        wd = self.web_driver
        self.open_groups_page()
        # init group creation
        wd.find_element_by_name("new").click()
        # fill group form
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()

    def open_groups_page(self):
        wd = self.web_driver
        wd.find_element_by_link_text("groups").click()

    def delete_first_group(self):
        wd = self.web_driver
        self.open_groups_page()
        # select first group
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()

    def get_list_group(self):
        # получаем список групп
        wd = self.web_driver
        self.open_groups_page()
        list = wd.find_elements_by_class_name("group")
        return list

    def edit_first_group(self):
        wd = self.web_driver
        self.open_groups_page()
        # select first group
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("(//input[@name='edit'])[2]").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys("777")
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys("uuu")
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys("ppp")
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()


    def return_to_groups_page(self):
        wd = self.web_driver
        wd.find_element_by_link_text("group page").click()
