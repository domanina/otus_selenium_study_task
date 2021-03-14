import allure
from Pages.categories_page import ElementsFinder1
from Pages.main_page import ElementsFinder2
from Pages.product_page import ElementsFinder3
from Pages.profile_page import ElementsFinder4

@allure.feature('Check elements')
@allure.title("Checking elements on categories page")
def test_check_elements_categories_page(browser):
    categories_page = ElementsFinder1(browser)
    categories_page.open("https://demo.opencart.com/index.php?route=product/category&path=20")
    categories_page.check_elements_cat_page()

@allure.feature('Check elements')
@allure.title("Checking elements on main page")
def test_check_elements_main_page(browser):
    main_page = ElementsFinder2(browser)
    main_page.open("https://demo.opencart.com/")
    main_page.check_elements_main_page()

@allure.feature('Check elements')
@allure.title("Checking elements on product page")
def test_check_elements_product_page(browser):
    product_page = ElementsFinder3(browser)
    product_page.open("https://demo.opencart.com/index.php?route=product/product&path=57&product_id=49")
    product_page.check_elements_prod_page()

@allure.feature('Check elements')
@allure.title("Checking elements on profile page")
def test_check_elements_profile_page(browser):
    profile_page = ElementsFinder4(browser)
    profile_page.open("https://demo.opencart.com/index.php?route=account/login")
    profile_page.check_elements_prof_page()