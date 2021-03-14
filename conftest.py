import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import logging
import requests
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener

logging.basicConfig(level=logging.INFO, filename="logs/test1.log")


class MyListener(AbstractEventListener):

    def before_navigate_to(self, url, driver):
        logging.info(f"Opening  {url}")

    def after_navigate_to(self, url, driver):
        logging.info(f"Success opening {url}")

    def before_find(self, by, value, driver):
        logging.info(f"Looking for '{value}' with '{by}'")

    def after_find(self, by, value, driver):
        logging.info(f"Success finding '{value}' with '{by}'")

    def before_click(self, element, driver):
        logging.info(f"Clicking {element}")

    def after_click(self, element, driver):
        logging.info(f"Success click {element}")

    def before_quit(self, driver):
        logging.info(f"Ready to terminate {driver}")

    def after_quit(self, browser):
        logging.info(f"Finished")

    def on_exception(self, exception, driver):
        logging.error(f'GOT EXEPTIONS: {exception}')
        driver.save_screenshot(f'logs/{exception}.png')


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--executor", action="store", default="127.0.0.1")
    parser.addoption("--vnc", action="store_true", default=False)
    parser.addoption("--logs", action="store_true", default=False)


@pytest.fixture
def browser(request):
    browser = request.config.getoption("--browser")
    executor = request.config.getoption("--executor")
    vnc = request.config.getoption("--vnc")
    logs = request.config.getoption("--logs")
    executor_url = f"http://{executor}:4444/wd/hub"

    caps = {
        "browserName": browser,
        "screenResolution": "1280x720",
        "selenoid:options": {
            "enableVNC": vnc,
            "enableLog": logs,
        }
    }

    driver = EventFiringWebDriver(webdriver.Remote(
        command_executor=executor_url,
        desired_capabilities=caps
    ), MyListener())

    yield driver
    print("\nquit browser..")
    driver.quit()
