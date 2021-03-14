from Pages.BaseApp import BasePage
from selenium.webdriver.common.by import By


class ProfileSeacrhLocators:
    LOCATOR_EMAIL = (By.ID,  "input-email")
    LOCATOR_RETURNING_LOGIN = (By.CSS_SELECTOR, "input.btn-primary")
    LOCATOR_PRICE = (By.TAG_NAME, "h2")
    LOCATOR_FORG_PASS = (By.LINK_TEXT, "Forgotten Password")
    LOCATOR_MY_ACCOUNT = (By.LINK_TEXT, "My Account")


class ElementsFinder4(BasePage):

    def __init__(self, browser):
        super().__init__(browser)
        self.driver = browser

    def check_elements_prof_page(self):
        return self.find_element(ProfileSeacrhLocators.LOCATOR_EMAIL), \
               self.find_element(ProfileSeacrhLocators.LOCATOR_RETURNING_LOGIN), \
               self.find_element(ProfileSeacrhLocators.LOCATOR_PRICE), \
               self.find_element(ProfileSeacrhLocators.LOCATOR_FORG_PASS), \
               self.find_element(ProfileSeacrhLocators.LOCATOR_MY_ACCOUNT)