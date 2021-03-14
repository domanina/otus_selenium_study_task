from Pages.BaseApp import BasePage
from selenium.webdriver.common.by import By


class MainSeacrhLocators:
    LOCATOR_SEARCH = (By.NAME, "search")
    LOCATOR_ITEM = (By.ID, "cart")
    LOCATOR_CATEGORIES = (By.CLASS_NAME, "visible-xs")
    LOCATOR_IMG_CATEGORIES = (By.CLASS_NAME, "img-responsive")
    LOCATOR_BRANDS = (By.LINK_TEXT, "Brands")


class ElementsFinder2(BasePage):

    def __init__(self, browser):
        super().__init__(browser)
        self.driver = browser

    def check_elements_main_page(self):
        return self.find_element(MainSeacrhLocators.LOCATOR_SEARCH),\
               self.find_element(MainSeacrhLocators.LOCATOR_ITEM),\
               self.find_element(MainSeacrhLocators.LOCATOR_CATEGORIES),\
               self.find_element(MainSeacrhLocators.LOCATOR_IMG_CATEGORIES),\
               self.find_element(MainSeacrhLocators.LOCATOR_BRANDS)



