import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

        # Wait for elements to load

    def scroll_to_element(self, selector):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(By.XPATH, selector))

    def wait_for_element(self, selector, timeout=40):
        return self.driver.find_element(By.XPATH, selector)

    def wait_for_until_element_exist(self, selector):
        return  WebDriverWait(self.driver, 20).until(
                    EC.presence_of_element_located((By.XPATH, selector)))
    def click_element(self, element):
        element.click()
        time.sleep(5)


    def accessByEmailForLogin(self, url):
        self.driver.get(url)
        # Log in to the platform (replace with your login elements)
        self.wait_for_element("//button[contains(text(), 'Start Demo')]").click()  # Assuming a login button
        self.wait_for_element("//label[contains(text(), 'Corporate Email')]//following::input").send_keys(
            "abc@email.com")
        self.wait_for_element("//img[@alt='checkbox']").click()
        self.wait_for_element("//button[contains(text(), 'Get started')]").click()
        time.sleep(5)

        try:
            if self.wait_for_element("//p[contains(@class, 'StyledErrorText')]").is_displayed():
                self.wait_for_element("//button[contains(text(), 'Login')]").click()
                self.wait_for_until_element_exist("//input[@data-testid = 'login-user-id']").send_keys(
                    "2091002414")
                self.wait_for_until_element_exist("//input[@data-testid = 'login-password']").send_keys("cgI$!eOZt6t2")
                self.wait_for_until_element_exist("//button[contains(text(), 'Sign in')]").click()
                time.sleep(20)

        except NoSuchElementException:
            self.driver(By.XPATH, "//button[contains(text(), 'Experience now')]").click()