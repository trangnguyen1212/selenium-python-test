# coding=utf-8
import pytest
from pages.main_page import MainPage
from tests.base_test import BaseTest


class TestTrading(BaseTest):

    @pytest.fixture
    def load_pages(self):
        self.page = MainPage(self.driver, self.wait)
        self.page.login_page()

    def test_stop_loss_take_profit(self):
        self.page = MainPage(self.driver, self.wait)
        self.page.stop_loss_take_profit()

    def test_edit_pending_order(self):
        self.page = MainPage(self.driver, self.wait)
        self.page.edit_pending_order()

    def test_edit_close_partial_close_Open_position(self):
        self.page = MainPage(self.driver, self.wait)
        self.page.edit_close_partial_close_Open_position()

    def test_limt_order_with_expiry_till_day(self):
        self.page = MainPage(self.driver, self.wait)
        self.page.limt_order_with_expiry_till_day()

    def test_limt_order_with_expiry_till_canceled(self):
        self.page = MainPage(self.driver, self.wait)
        self.page.limt_order_with_expiry_till_Cancelled()
