from selenium.webdriver import Keys

from base.base_page import BasePage


class DealsPage(BasePage):

    _PAGE_URL = "https://release-crm.qa-playground.com/#/deals"

    _SWITCH_BUTTON = "//input[@name='checkedC']"
    _SEARCH_FIELD = "//input[@id='q']"
    _TEXT_SEARCHED = "//p[text()='Quas alias sit']"

    def click_switch_button(self):
        switch_button = self.driver.find_element(*self._SWITCH_BUTTON)
        switch_button.click()

    def click_and_search_in_field(self):
        search_field = self.driver.find_element(*self._SEARCH_FIELD)
        search_field.click()
        search_field.send_keys("Quas alias sit")
        search_field.send_keys(Keys.ENTER)

    def assert_searched(self):
        text_searched = self.driver.find_element(*self._TEXT_SEARCHED)
        assert "Quas alias sit" in text_searched.text
        print("Quas alias sit")





