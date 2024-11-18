from base.base_page import BasePage

class CrmPage(BasePage):

    _PAGE_URL = "https://release-crm.qa-playground.com/"

    _DASHBOARD_PAGE = "//a[text()='Dashboard']"
    _CONTACTS_PAGE = "//a[text()='Contacts']"
    _COMPANIES_PAGE = "//a[text()='Companies']"
    _DEALS_PAGE = "//a[text()='Deals']"

    def click_contacts_page(self):
        contacts_page = self.driver.find_element(*self._CONTACTS_PAGE)
        contacts_page.click()
        assert contacts_page.text == "CONTACTS"
        print("Contacts Page")

    def click_companies_page(self):
        companies_page = self.driver.find_element(*self._COMPANIES_PAGE)
        companies_page.click()
        assert companies_page.text == "COMPANIES"
        print("Companies Page")

    def click_deals_page(self):
        deals_page = self.driver.find_element(*self._DEALS_PAGE)
        deals_page.click()
        assert deals_page.text == "DEALS"
        print("Deals Page")

    def click_dashboard_page(self):
        dashboard_page = self.driver.find_element(*self._DASHBOARD_PAGE)
        dashboard_page.click()
        assert dashboard_page.text == "DASHBOARD"
        print("Dashboard Page")
