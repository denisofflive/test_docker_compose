from pages.contacts_page import ContactsPage
from pages.deals_page import DealsPage
from pages.crm_page import CrmPage

class BaseTest:


    def setup_method(self):
        self.deals_page = DealsPage(self.driver)
        self.crm_page = CrmPage(self.driver)
        self.contacts_page = ContactsPage(self.driver)

