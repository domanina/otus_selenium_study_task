from Pages.BaseApp import BasePage
from selenium.webdriver.common.by import By


class ProductSeacrhLocators:
    LOCATOR_ADD_BUTTON = (By.CLASS_NAME, "btn.btn-primary.btn-lg.btn-block")
    LOCATOR_INPUT_COUNT = (By.CSS_SELECTOR, "#input-quantity")
    LOCATOR_PRICE = (By.TAG_NAME, "h2")
    LOCATOR_SEARCH_BUTTON = (By.CLASS_NAME, "btn.btn-default.btn-lg")
    LOCATOR_REVIEWS = (By.LINK_TEXT, "Reviews (0)")


class ElementsFinder3(BasePage):

    def __init__(self, browser):
        super().__init__(browser)
        self.driver = browser

    def check_elements_prod_page(self):
        return self.find_element(ProductSeacrhLocators.LOCATOR_ADD_BUTTON), \
               self.find_element(ProductSeacrhLocators.LOCATOR_INPUT_COUNT), \
               self.find_element(ProductSeacrhLocators.LOCATOR_PRICE), \
               self.find_element(ProductSeacrhLocators.LOCATOR_SEARCH_BUTTON), \
               self.find_element(ProductSeacrhLocators.LOCATOR_REVIEWS)