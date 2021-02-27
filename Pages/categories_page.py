from Pages.BaseApp import BasePage
from selenium.webdriver.common.by import By


class CategoriesSeacrhLocators:
    LOCATOR_SEARCH = (By.NAME, "search")
    LOCATOR_HOME_ITEM = (By.CLASS_NAME, "fa.fa-home")
    LOCATOR_PRICE = (By.CLASS_NAME, "price")
    LOCATOR_SAMSUNG = (By.LINK_TEXT, "Samsung SyncMaster 941BW")
    LOCATOR_PC= (By.LINK_TEXT, "PC (0)")


class ElementsFinder1(BasePage):

    def __init__(self, browser):
        super().__init__(browser)
        self.driver = browser

    def check_elements_cat_page(self):
        return self.find_element(CategoriesSeacrhLocators.LOCATOR_SEARCH),\
               self.find_element(CategoriesSeacrhLocators.LOCATOR_HOME_ITEM),\
               self.find_element(CategoriesSeacrhLocators.LOCATOR_PRICE),\
               self.find_element(CategoriesSeacrhLocators.LOCATOR_SAMSUNG),\
               self.find_element(CategoriesSeacrhLocators.LOCATOR_PC)