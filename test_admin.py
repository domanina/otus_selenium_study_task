import allure
from Pages.admin_page import ElementsFinder
from selenium.common.exceptions import NoSuchElementException


@allure.feature('Authorization')
@allure.title("Authorization from admin page")
@allure.description("Checking auth without checking token...")
def test_try_to_login(browser):
    admin_page = ElementsFinder(browser)
    admin_page.open("https://demo.opencart.com/admin/")
    with allure.step("Enter log/pass"):
        admin_page.check_elements_admin_page()
        admin_page.enter_login_password("Lissa", "12345")
        admin_page.click_on_login_button()
    with allure.step("Check page"):
        admin_page.check_next_autorizated_page()


@allure.feature('Check elements')
@allure.title("Authorizated checking for a table")
def test_check_table(browser):
    admin_page = ElementsFinder(browser)
    admin_page.open("https://demo.opencart.com/admin/")
    with allure.step("Check count in table"):
        admin_page.click_on_login_button()
        assert admin_page.find_table_with_colums() == 84


@allure.feature('Authorization')
@allure.title("Logout")
def test_check_logout(browser):
    admin_page = ElementsFinder(browser)
    admin_page.open("https://demo.opencart.com/admin/")
    with allure.step("Enter log/pass"):
        admin_page.enter_login_password("Lissa", "12345")
    admin_page.click_on_login_button()
    with allure.step("Check next page"):
        admin_page.click_on_logout_button()
        next_page = "https://demo.opencart.com/admin/index.php?route=common/login"
        cur_URL = str(admin_page.current_url())
        assert cur_URL == next_page


@allure.feature('Authorization')
@allure.title("Forgotten password")
def test_forget_password(browser):
    admin_page = ElementsFinder(browser)
    admin_page.open("https://demo.opencart.com/admin/")
    admin_page.click_on_forgot_pass_button()
    with allure.step("Check url"):
        next_page = "https://demo.opencart.com/admin/index.php?route=common/forgotten"
        cur_URL = str(admin_page.current_url())
        assert cur_URL == next_page
    admin_page.enter_email_to_reset("demo@opencart.com")
    admin_page.click_on_reset_button()
    with allure.step("Check message"):
        reset_text = "An email with a confirmation link has been sent your admin email address.\n×"
        assert reset_text == admin_page.find_text_after_reset()
