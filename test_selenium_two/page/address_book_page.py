from selenium.webdriver.common.by import By

# from test_selenium_two.page.add_department_page import Department
from test_selenium_two.page.base_page import BasePage


class AddressBook(BasePage):

    def goto_member(self):
        pass

    # def goto_department(self):
    #     return Department(self.driver)

    def get_list(self):
        departments = self.driver.find_elements(By.CSS_SELECTOR, ".jstree-anchor")
        department = []
        for depart in departments:
            print(depart.text)
            department.append(depart.text)
        return department

