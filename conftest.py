from pathlib import Path

import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions

from pages.login_page import LoginPage


def pytest_addoption(parser):
    parser.addoption("--apk-path", action="store", default=f'{Path(__file__).parent}/login_app.apk',
                     help="Path to apk file")
    parser.addoption("--appium-path", action="store", default='http://localhost:4723', help="Path to appium server url")
    parser.addoption("--platform-name", action="store", default='Android', help="Platform name")
    parser.addoption("--automation-name", action="store", default='UiAutomator2', help="Automation name")
    parser.addoption("--device-name", action="store", default='Pixel 9 Pro', help="Device name")


@pytest.fixture
def driver(request):
    """Фикстура для создания драйвера Appium"""

    # Настройки для Android
    platform_name = request.config.getoption("--platform-name")
    options = None
    if platform_name == 'Android':
        options = UiAutomator2Options()
    else:
        options = XCUITestOptions()

    options.platform_name = request.config.getoption("--platform-name")
    options.automation_name = request.config.getoption("--automation-name")
    options.device_name = request.config.getoption("--device-name")
    options.app = request.config.getoption("--apk-path")
    options.no_reset = False
    options.full_reset = True
    
    # Дополнительные настройки
    options.set_capability("appWaitActivity", "*")
    options.set_capability("appWaitDuration", 10000)
    options.set_capability("autoGrantPermissions", True)
    options.set_capability("newCommandTimeout", 60)
    
    driver = webdriver.Remote(request.config.getoption("--appium-path"), options=options)
    yield driver
    
    if driver:
        driver.quit()


@pytest.fixture
def login_page(driver):
    """Фикстура для создания объекта LoginPage"""
    return LoginPage(driver)
