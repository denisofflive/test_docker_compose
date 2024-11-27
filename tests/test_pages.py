import time

import pytest

from base.base_test import BaseTest

class TestPages(BaseTest):

    # Поставил timesleep, чтобы можно было посмотреть не так быстро? как отрабатывают тесты

    @pytest.mark.t
    def test_click_on_pages(self):
        self.crm_page.open()
        time.sleep(1)
        self.crm_page.click_contacts_page()
        time.sleep(1)
        self.crm_page.click_companies_page()
        time.sleep(1)
        self.crm_page.click_deals_page()
        time.sleep(1)
        self.crm_page.click_dashboard_page()
        time.sleep(1)


    def test_search_in_deals(self):
        self.deals_page.open()
        time.sleep(1)
        self.deals_page.click_switch_button()
        time.sleep(1)
        self.deals_page.click_and_search_in_field()
        time.sleep(1)
        self.deals_page.assert_searched()
        time.sleep(1)

    def test_search_on_contacts_page(self):
        self.contacts_page.open()
        time.sleep(1)
        self.contacts_page.click_and_search_in_contacts_page()
        time.sleep(1)
        self.contacts_page.click_on_natalie_kutch()
        time.sleep(1)
        self.contacts_page.assert_title_natalie_kutch()
        time.sleep(1)
