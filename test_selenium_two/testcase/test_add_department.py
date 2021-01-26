import json

from test_selenium_two.page.base_page import BasePage
from test_selenium_two.page.main_page import MainPage


class TestAdddpt():

    def setup_class(self):
        self.main = MainPage()

    def test_add_department(self):
        result = self.main.goto_member().add_department("部门6").get_list()
        assert "部门6" in result

    # def test_add_department_two(self):
    #     result = self.main.goto_address_book().goto_department("部门3")
    #     assert "部门3" in result
    #
    # def test_add_department_fail(self):
    #     result = self.main.goto_member().add_department("部门2")
    #     assert "部门2" not in result
