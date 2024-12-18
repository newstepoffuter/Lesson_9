from selene import browser
import pytest
from selenium import webdriver

@pytest.fixture(scope='session', autouse=True)
def browser_settings():
    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = 'eager'
    browser.config.driver.maximize_window()
    browser.config.driver_options = driver_options
    browser.config.base_url = 'https://demoqa.com'

    yield
    browser.quit()