from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_open_brower(browser, url, headless):
    link = "https://demo.opencart.com/"
    browser.get(link)
    assert link == browser.current_url

    try:
        search = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.NAME, "search")),
        )
        item = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, "cart"))
        )
        cat = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "visible-xs"))
        )
        img = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "img-responsive"))
        )
        brands = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Brands"))
        )

    finally:
        browser.quit()


def test_categories_brower(browser, url, headless):
    link = "https://demo.opencart.com/index.php?route=product/category&path=20"
    browser.get(link)

    try:
        search = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.NAME, "search")),
        )
        item = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "fa.fa-home"))
        )
        cat = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "price"))
        )
        good = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Samsung SyncMaster 941BW"))
        )
        pc = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "PC (0)"))
        )

    finally:
        browser.quit()


def test_cart_brower(browser, url, headless):
    link = "https://demo.opencart.com/index.php?route=product/product&path=57&product_id=49"
    browser.get(link)

    try:
        price = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "h2")),
        )
        button = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "btn.btn-primary.btn-lg.btn-block"))
        )
        cat = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#input-quantity"))
        )
        sear_but = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "btn.btn-default.btn-lg"))
        )
        rew0 = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Reviews (0)"))
        )

    finally:
        browser.quit()


def test_login_brower(browser, url, headless):
    link = "https://demo.opencart.com/index.php?route=account/login"
    browser.get(link)

    try:
        price = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "h2")),
        )
        cat = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input.btn-primary"))
        )
        email = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, "input-email"))
        )
        acc = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "My Account"))
        )
        forgot = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Forgotten Password"))
        )

    finally:
        browser.quit()


def test_admin_brower(browser, url, headless):
    link = "https://demo.opencart.com/admin/"
    browser.get(link)

    try:
        lock = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "fa.fa-lock")),
        )
        user = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "fa.fa-user"))
        )
        passw = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.NAME, "password"))
        )
        log = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "btn.btn-primary"))
        )
        forgot = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Forgotten Password"))
        )

    finally:
        browser.quit()







    # button = browser.find_element_by_css_selector("button.btn")
    # button.click()

# try:
#     browser = webdriver.Firefox()
#     browser.get("http://suninjuly.github.io/huge_form.html")
#     elements = browser.find_elements_by_tag_name("input")
#     for element in elements:
#        element.send_keys("Мой ответ")
#
#     button = browser.find_element_by_css_selector("button.btn")
#     button.click()
#
# finally:
#     time.sleep(10)
#     # закрываем браузер после всех манипуляций
#     browser.quit()