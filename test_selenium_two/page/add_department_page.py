from time import sleep

from selenium.webdriver.common.by import By

from test_selenium_two.page.address_book_page import AddressBook
from test_selenium_two.page.base_page import BasePage


class Department(BasePage):

    _name = (By.XPATH, "name")
    def add_department(self, dname):
        self.find(By.XPATH, "//*[@class='member_colLeft_top_addBtn']").click()
        self.find(By.XPATH, "//*[@class='js_create_party']").click()
        self.find(*self._name).send_keys(dname)
        self.find(By.XPATH, "//*[@class='js_parent_party_name']").click()
        self.find(By.CSS_SELECTOR, ".qui_dialog_body.ww_dialog_body [id='1688850701784008_anchor']").click()
        self.find(By.XPATH, "//*[@class='qui_btn ww_btn ww_btn_Blue']").click()
        self.driver.refresh()
        sleep(2)
        return AddressBook(self.driver)

    # def add_department_fail(self, dname):
    #     self.find(By.XPATH, "//*[@class='js_create_dropdown']").click()
    #     self.find(By.XPATH, "//*[@class='js_create_party']").click()
    #     self.find(self._departname, "//*[@class='ww_inputText']").send_keys(dname)
    #     self.find(By.XPATH, "//*[@class='js_toggle_party_list']").click()
    #     self.find(By.XPATH, "//*[@class='jstree-anchor']").click()
    #     self.find(By.XPATH, "//*[@class='ww_btn_Blue']").click()
    #     return AddressBook(self.driver)