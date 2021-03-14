from Pages.admin_page import ElementsFinder


def test_try_to_login(browser, url, headless):
    admin_page = ElementsFinder(browser)
    admin_page.open("https://demo.opencart.com/admin/")
    admin_page.check_elements_admin_page()
    admin_page.enter_login_password("Lissa", "12345")
    admin_page.click_on_login_button()
    admin_page.check_next_autorizated_page()


def test_check_table(browser, url, headless):
    admin_page = ElementsFinder(browser)
    admin_page.open("https://demo.opencart.com/admin/")
    admin_page.click_on_login_button()

    assert admin_page.find_table_with_colums() == 84


def test_check_logout(browser, url, headless):
    admin_page = ElementsFinder(browser)
    admin_page.open("https://demo.opencart.com/admin/")
    admin_page.enter_login_password("Lissa", "12345")
    admin_page.click_on_login_button()

    admin_page.click_on_logout_button()
    next_page = "https://demo.opencart.com/admin/index.php?route=common/login"
    cur_URL = str(admin_page.current_url())
    assert cur_URL == next_page


def test_forget_password(browser, url, headless):
    admin_page = ElementsFinder(browser)
    admin_page.open("https://demo.opencart.com/admin/")
    admin_page.click_on_forgot_pass_button()
    next_page = "https://demo.opencart.com/admin/index.php?route=common/forgotten"
    cur_URL = str(admin_page.current_url())
    assert cur_URL == next_page

    admin_page.enter_email_to_reset("demo@opencart.com")
    admin_page.click_on_reset_button()
    reset_text = "An email with a confirmation link has been sent your admin email address.\n×"
    assert reset_text == admin_page.find_text_after_reset()
#
#
#
#
#
#
#
#
#
#
#
#
