import time
import pytest



def test_admin_brower(browser, url, headless):
    # открыть страницу
    # очистить прля логина и пароля
    # ввнести свои данные
    # нажать кнопку логин
    # проверить переход
    link = "https://demo.opencart.com/admin/"
    browser.get(link)

    username = browser.find_element_by_name("username")
    username.clear()
    username.send_keys("Lissa")

    password = browser.find_element_by_name("password")
    password.clear()
    password.send_keys("test-test")

    button = browser.find_element_by_class_name("btn.btn-primary")
    button.click()

    cur_URL = str(browser.current_url)
    next_page_any_token = "https://demo.opencart.com/admin/index.php?route=common/dashboard&user_token="

    if cur_URL.startswith(next_page_any_token):
        pass
    else:
        raise AssertionError

# check goods page
def test_check_table_brower(browser, url, headless):
    link = "https://demo.opencart.com/admin/"
    browser.get(link)
    button = browser.find_element_by_class_name("btn.btn-primary")
    button.click()

    catalog = browser.find_element_by_class_name("fa.fa-tags.fw")
    catalog.click()
    cats = browser.find_element_by_link_text("Categories")
    cats.click()

    table = browser.find_element_by_tag_name("tr")
    colums = browser.find_elements_by_tag_name("td")
    assert len(colums) == 84

    first_colum = browser.find_element_by_link_text("Category Name")
    second_colum = browser.find_element_by_link_text("Sort Order")

#Check login and logout
def test_check_logout_brower(browser, url, headless):
    link = "https://demo.opencart.com/admin/"
    browser.get(link)
    button = browser.find_element_by_class_name("btn.btn-primary")
    button.click()

    login = browser.find_element_by_id("user-profile")
    button_logout = browser.find_element_by_class_name("fa.fa-sign-out")
    button_logout.click()
    next_page = "https://demo.opencart.com/admin/index.php?route=common/login"
    assert next_page == browser.current_url



def test_forget_brower(browser, url, headless):
    # открыть страницу
    # нажать кнопку forgotten password
    # проверить переход
    # ввести емейл
    #нажать кнопку резет
    #проверить наличие сооощения на странице и переход
    link = "https://demo.opencart.com/admin/"
    browser.get(link)

    button_forget = browser.find_element_by_link_text("Forgotten Password")
    button_forget.click()
    next_page = "https://demo.opencart.com/admin/index.php?route=common/forgotten"
    assert next_page == browser.current_url

    email = browser.find_element_by_id("input-email")
    email.send_keys("demo@opencart.com")
    button_reset = browser.find_element_by_class_name("btn.btn-primary")
    button_reset.click()
    next_page = "https://demo.opencart.com/admin/index.php?route=common/login"
    assert next_page == browser.current_url

    done = browser.find_element_by_class_name("alert.alert-success.alert-dismissible")
    print(done.text)
    assert done.text == "An email with a confirmation link has been sent your admin email address.\n×"








