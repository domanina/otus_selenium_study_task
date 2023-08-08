from Pages.BaseApp import BasePage
from selenium.webdriver.common.by import By
import allure


class AdminSeacrhLocators:
    LOCATOR_USERNAME_FIELD = (By.NAME, "username")
    LOCATOR_PASSWORD_FIELD = (By.NAME, "password")
    LOCATOR_LOGIN_BUTTON = (By.CLASS_NAME, "btn.btn-primary")
    LOCATOR_FORGOT_PASS_BUTTON = (By.LINK_TEXT, "Forgotten Password")
    LOCATOR_CATALOG = (By.CLASS_NAME, "fa.fa-tags.fw")
    LOCATOR_CATEGORIES = (By.LINK_TEXT,"Categories")
    LOCATOR_COLUMS = (By.TAG_NAME, "td")
    LOCATOR_LOGOUT_BUTTON = (By.CLASS_NAME, "fa.fa-sign-out")
    LOCATOR_EMAIL_FIELD = (By.ID, "input-email")
    LOCATOR_RESET_BUTTON = (By.CLASS_NAME,"btn.btn-primary")
    LOCATOR_CHECK_RESET = (By.CLASS_NAME,"alert.alert-success.alert-dismissible")
    LOCATOR_LOCK_ITEM = (By.CLASS_NAME,"fa.fa-lock")
    LOCATOR_USER_ITEM = (By.CLASS_NAME,"fa.fa-user")


class ElementsFinder(BasePage):

    def __init__(self, browser):
        super().__init__(browser)
        self.driver = browser

    def current_url(self):
        return self.browser.current_url

    def enter_login_password(self, username, password):
        login_field = self.find_element(AdminSeacrhLocators.LOCATOR_USERNAME_FIELD)
        login_field.clear()
        login_field.send_keys(username)

        pass_field = self.find_element(AdminSeacrhLocators.LOCATOR_PASSWORD_FIELD)
        pass_field.clear()
        pass_field.send_keys(password)

        return login_field, pass_field

    def enter_email_to_reset(self, email):
        email_field = self.find_element(AdminSeacrhLocators.LOCATOR_EMAIL_FIELD)
        email_field.send_keys(email)
        return email_field

    def find_text_after_reset (self):
        done = self.find_element(AdminSeacrhLocators.LOCATOR_CHECK_RESET)
        return done.text

    def click_on_login_button(self):
        with allure.step("click"):
            return self.find_element(AdminSeacrhLocators.LOCATOR_LOGIN_BUTTON).click()

    def click_on_logout_button(self):
        with allure.step("click"):
            return self.find_element(AdminSeacrhLocators.LOCATOR_LOGOUT_BUTTON).click()

    def click_on_forgot_pass_button(self):
        with allure.step("click"):
            return self.find_element(AdminSeacrhLocators.LOCATOR_FORGOT_PASS_BUTTON).click()

    def click_on_reset_button(self):
        with allure.step("click"):
            return self.find_element(AdminSeacrhLocators.LOCATOR_RESET_BUTTON).click()

    def check_next_autorizated_page(self):
        cur_URL = str(self.browser.current_url)
        next_page_any_token = "https://demo.opencart.com/admin/index.php?route=common/dashboard&user_token="

        if cur_URL.startswith(next_page_any_token):
            pass
        else:
            raise AssertionError

    def find_table_with_colums(self):
        self.find_element(AdminSeacrhLocators.LOCATOR_CATALOG).click()
        self.find_element(AdminSeacrhLocators.LOCATOR_CATEGORIES).click()
        return len(self.find_elements(AdminSeacrhLocators.LOCATOR_COLUMS))

    def check_elements_admin_page(self):
        lock_item = self.find_element(AdminSeacrhLocators.LOCATOR_LOCK_ITEM)
        user_item = self.find_element(AdminSeacrhLocators.LOCATOR_USER_ITEM)
        return lock_item, user_item






