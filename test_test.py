from selenium import webdriver
import time



def test_open_brower(browser, url,headless):
    link = "https://demo.opencart.com/"
    browser.get(link)
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