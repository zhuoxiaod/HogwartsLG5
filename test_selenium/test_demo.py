import json
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestBaidu():
    def setup_method(self):
        self.driver = webdriver.Chrome()
    #
    def teardown_method(self):
        self.driver.quit()


    def test_cookie(self):
    #     # 获取cookie
    #     cookies = self.driver.get_cookies()
    #     # 以文件流形式，打开文件
    #     with open("cookie.json", "w") as f:
    #     # 存储cookie到cookie.json
    #         json.dump(cookies, f)
        # 以文件流形式打开文件
        self.driver.get("https://work.weixin.qq.com/")
        with open("cookie.json", "r") as f:
        # 读取cookie
            cookies = json.load(f)
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        sleep(3)
        self.driver.find_element(By.XPATH, "//*[@id='menu_customer']").click()
        sleep(5)

    # def test_weixin(self):
    #     self.driver.get("https://work.weixin.qq.com/")
    #     sleep(3)
    #     self.driver.find_element(By.XPATH, "//*[@class='index_top_operation_loginBtn']").click()
    #     sleep(8)


        self.driver.close()