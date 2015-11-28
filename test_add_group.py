# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_add_group(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

    def Open_Home_Page(self, wd):
        wd.get("http://localhost/addressbook/")

    def Login(self, wd):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("Admin")
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_css_selector("input[type=\"submit\"]").click()

    def Open_Group_Page(self, wd):
        wd.find_element_by_link_text("groups").click()

    def Create_Group(self, wd):
        # Init Group creation
        wd.find_element_by_name("new").click()
        # Fill Group form
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys("FirstGroupName")
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys("FirstGroupHeader")
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys("FirstGroupFooter")
        # Submit Group creation:
        wd.find_element_by_name("submit").click()

    def Return_to_Groups_Page(self, wd):
        wd.find_element_by_link_text("group page").click()

    def Logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def test_test_add_group(self):
        wd = self.wd
        self.Open_Home_Page(wd)
        self.Login(wd)
        self.Open_Group_Page(wd)
        self.Create_Group(wd)
        self.Return_to_Groups_Page(wd)
        self.Logout(wd)

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
