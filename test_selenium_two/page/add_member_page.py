from selenium import webdriver

from test_selenium_two.page.add_department_page import Department
from test_selenium_two.page.base_page import BasePage
from selenium.webdriver.common.by import By


class Member(BasePage):

    def add_Member(self):
        pass


    def goto_department(self):
        return Department(self.driver)

