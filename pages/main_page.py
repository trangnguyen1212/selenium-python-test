import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage

class MainPage(BasePage):

    def __init__(self, driver, wait):
        self.url = "https://www.aquariux.com/solutions/trader/"
        #self.locator = locators
        super().__init__(driver, wait)

    def login_page(self):
        self.accessByEmailForLogin(self.url)

    # 1. Test User stop loss and take profit
    def stop_loss_take_profit(self):
        self.login_page()

        # Select dropdown
        dropdown_element = self.wait_for_until_element_exist("//div[@data-testid='trade-dropdown-order-type']//div")
        dropdown_element.click()
        # Select by visible text (change "Option Text" to the actual option text)
        stop_option = self.driver.find_element(By.XPATH, "//div[@data-testid='trade-dropdown-order-type-stop']")
        stop_option.click()
        sell_button = self.driver.find_element(By.XPATH, "//div[@data-testid='trade-button-order-sell']")
        sell_button.click()
        #collapse
        self.wait_for_element("//div[contains(text(), 'Trade Details (USD)')]").click()
        increase_volumne = self.driver.find_element(By.XPATH, "//div[@data-testid='trade-input-volume-increase']")
        increase_volumne.click()
        input_price = self.driver.find_element(By.XPATH, "//input[@data-testid='trade-input-price']")
        input_price.send_keys("7")
        increase_stoploss = self.driver.find_element(By.XPATH,
                                                     "//div[@data-testid='trade-input-stoploss-price-increase']")
        increase_stoploss.click()
        increase_takeprofit = self.driver.find_element(By.XPATH,
                                                       "//div[@data-testid='trade-input-takeprofit-price-increase']")
        # expand
        self.wait_for_element("//div[contains(text(), 'Trade Details (USD)')]").click()
        increase_takeprofit.click()
        self.driver.find_element(By.XPATH, "//button[contains(text(), 'Place Sell Order')]").click()
        self.driver.find_element(By.XPATH, "//button[contains(text(), 'Confirm')]").click()
        # Validate order confirmation message
        self.wait_for_until_element_exist("//div[@data-testid='trade-confirmation-label']")
        order_confirmation = self.driver.find_element(By.XPATH, "//div[@data-testid='notification-description']").text
        assert "Stop Order Submitted" in order_confirmation
        print("Market order placed successfully with Stop Loss and Take Profit.")

    # 2. edit, partial close and close Open position
    def edit_close_partial_close_Open_position(self):
        self.login_page()

        # Select dropdown
        dropdown_element = self.wait_for_until_element_exist("//div[@data-testid='trade-dropdown-order-type']//div")
        dropdown_element.click()
        market_option = self.driver.find_element(By.XPATH, "//div[@data-testid='trade-dropdown-order-type-market']")
        market_option.click()
        # Create Open position
        buy_button = self.driver.find_element(By.XPATH, "//div[@data-testid='trade-button-order-buy']")
        buy_button.click()
        self.driver.find_element(By.XPATH, "//button[contains(text(), 'Place Buy Order')]").click()
        self.driver.find_element(By.XPATH, "//button[contains(text(), 'Confirm')]").click()

        # Edit a position
        self.driver.find_element(By.XPATH, "//div[@data-testid='asset-open-button-edit']").click()
        # collapse
        self.wait_for_element("//div[contains(text(), 'Trade Details (USD)')]").click()
        input_price = self.driver.find_element(By.XPATH, "//input[@data-testid='edit-input-price']")
        input_price.send_keys("7")
        input_stoploss_price = self.driver.find_element(By.XPATH, "//input[@data-testid='edit-input-stoploss-price']")
        input_stoploss_price.send_keys("7")
        input_stoploss_points = self.driver.find_element(By.XPATH, "//input[@data-testid='edit-input-stoploss-points']")
        input_stoploss_points.send_keys("2")
        input_takeprofit_price = self.driver.find_element(By.XPATH,
                                                          "//input[@data-testid='edit-input-takeprofit-price']")
        input_takeprofit_price.send_keys("1")
        input_takeprofit_points = self.driver.find_element(By.XPATH,
                                                           "//input[@data-testid='edit-input-takeprofit-points']")
        input_takeprofit_points.send_keys("1")
        # expand
        self.wait_for_element("//div[contains(text(), 'Trade Details (USD)')]").click()
        self.driver.find_element(By.XPATH, "//button[contains(text(), 'Update Buy Order')]").click()

        # Close a position
        self.driver.find_element(By.XPATH, "//div[@data-testid='asset-open-button-close']").click()
        self.driver.find_element(By.XPATH, "//button[contains(text(), 'Close Order')]").click()

    # 3 edit Pending Orders for all values included
    def edit_pending_order(self):
        self.login_page()

        # move to pending tab
        pending_tab = self.driver.find_element(By.XPATH, "//div[@data-testid='tab-asset-order-type-pending-orders']")
        pending_tab.click()

        # Edit Pending Orders
        self.driver.find_element(By.XPATH, "//div[@data-testid='asset-pending-button-edit']").click()
        input_price = self.driver.find_element(By.XPATH, "//input[@data-testid='edit-input-price']")
        input_price.send_keys("7")
        input_stoploss_price = self.driver.find_element(By.XPATH, "//input[@data-testid='edit-input-stoploss-price']")
        input_stoploss_price.send_keys("7")
        input_stoploss_points = self.driver.find_element(By.XPATH, "//input[@data-testid='edit-input-stoploss-points']")
        input_stoploss_points.send_keys("2")
        input_takeprofit_price = self.driver.find_element(By.XPATH,
                                                          "//input[@data-testid='edit-input-takeprofit-price']")
        input_takeprofit_price.send_keys("1")
        input_takeprofit_points = self.driver.find_element(By.XPATH,
                                                           "//input[@data-testid='edit-input-takeprofit-points']")
        input_takeprofit_points.send_keys("1")
        self.driver.find_element(By.XPATH, "//button[contains(text(), 'Update Sell Order')]").click()