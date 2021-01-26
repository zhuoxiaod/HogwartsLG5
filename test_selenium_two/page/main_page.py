from selenium.webdriver.common.by import By

from test_selenium_two.page.add_department_page import Department
from test_selenium_two.page.address_book_page import AddressBook
from test_selenium_two.page.base_page import BasePage


class MainPage(BasePage):

    def goto_address_book(self):
        self.find(By.XPATH, "//*[@class='frame_nav_item_title']").click()
        return AddressBook(self.driver)

    def goto_member(self):
        self.find(By.XPATH, "//*[@class='index_service_cnt_itemWrap']").click()
        return Department(self.driver)


