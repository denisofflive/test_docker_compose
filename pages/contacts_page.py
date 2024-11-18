from selenium.webdriver import Keys

from base.base_page import BasePage

class ContactsPage(BasePage):

    _PAGE_URL = "https://release-crm.qa-playground.com/#/contacts"

    _SEARCH_CONTACTS_FIELD = "//input[@id='q']"
    _NATALIE_KUTCH = "//span[text()='Natalie Kutch']"
    _TITLE_NATALIE_KUTCH = "//div[@class='MuiBox-root css-182u9mc']"

    def click_and_search_in_contacts_page(self):
        search_contacts_field = self.driver.find_element(*self._SEARCH_CONTACTS_FIELD)
        search_contacts_field.click()
        search_contacts_field.send_keys("cold")
        search_contacts_field.send_keys(Keys.ENTER)

    def click_on_natalie_kutch(self):
        natalie_kutch = self.driver.find_element(*self._NATALIE_KUTCH)
        natalie_kutch.click()

    def assert_title_natalie_kutch(self):
        title_natalie_kutch = self.driver.find_element(*self._TITLE_NATALIE_KUTCH)
        assert "Natalie Kutch" in title_natalie_kutch.text
        print("Natalie Kutch")
