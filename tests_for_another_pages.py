from Pages.categories_page import ElementsFinder1
from Pages.main_page import ElementsFinder2
from Pages.product_page import ElementsFinder3
from Pages.profile_page import ElementsFinder4


def test_check_elements_categories_page(browser, url, headless):
    categories_page = ElementsFinder1(browser)
    categories_page.open("https://demo.opencart.com/index.php?route=product/category&path=20")
    categories_page.check_elements_cat_page()


def test_check_elements_main_page(browser, url, headless):
    main_page = ElementsFinder2(browser)
    main_page.open("https://demo.opencart.com/")
    main_page.check_elements_main_page()


def test_check_elements_product_page(browser, url, headless):
    product_page = ElementsFinder3(browser)
    product_page.open("https://demo.opencart.com/index.php?route=product/product&path=57&product_id=49")
    product_page.check_elements_prod_page()


def test_check_elements_profile_page(browser, url, headless):
    profile_page = ElementsFinder4(browser)
    profile_page.open("https://demo.opencart.com/index.php?route=account/login")
    profile_page.check_elements_prof_page()