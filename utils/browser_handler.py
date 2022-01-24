from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium import webdriver
import json
import time

class BrowserHandler:
    def __init__(self, driver_path, base_url):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.browser = webdriver.Chrome(driver_path, options=options)
        self.browser.get(base_url)
        self.browser.maximize_window()
        self.browser.implicitly_wait(10)
        self.browser.delete_all_cookies()
        self.add_cookies()
    
    def add_cookies(self):
        with open('cookies.txt', 'r') as f:
            cookies_list = json.load(f)
            for cookie in cookies_list:
                self.browser.add_cookie(cookie)

    def get_url(self):
        self.browser.get_url()

    def find_elements(self, content):
        return self.browser.find_elements(By.XPATH, content)

    def mouse_slide_move(self):
        Action_1 = ActionChains(self.browser)
        Action_2 = ActionChains(self.browser)
        MoveElement = self.browser.find_element('//section[@class="jobs-search__left-rail"]')
        Action_1.move_to_element(MoveElement)
        Action_1.move_by_offset(245, -250)
        Action_1.perform()
        move_times = 5
        while move_times > 0:
            Action_2.click_and_hold()
            Action_2.move_by_offset(0, 100)
            Action_2.release()
            time.sleep(1)
            move_times = move_times - 1
            Action_2.perform()

    def quit(self):
        self.browser.quit()