from selenium.webdriver.common.by import By


class Locators:
    INPUT = (By.ID, "input")
    BUTTON = (By.XPATH, "//*[@id='']//*[@type='submit']")
    RESULTS = (By.XPATH, "//*[@data-testid='mainline']//*[@data-testid='result']")
