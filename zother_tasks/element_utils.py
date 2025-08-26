"""Утилиты для работы с элементами"""
from time import sleep

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def wait_for_element_clickable(driver, locator, timeout=10):
    """Ожидание кликабельности элемента"""
    try:
        WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        return True
    except TimeoutException:
        return False


def wait_for_element_visible(driver, locator, timeout=10):
    """Ожидание видимости элемента"""
    try:
        WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
        return True
    except TimeoutException:
        return False


def wait_for_element_present(driver, locator, timeout=10):
    """Ожидание присутствия элемента в DOM"""
    try:
        WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located(locator)
        )
        return True
    except TimeoutException:
        return False


def safe_click(driver, locator, timeout=10):
    """Безопасный клик с ожиданием кликабельности"""
    if wait_for_element_clickable(driver, locator, timeout):
        element = driver.find_element(*locator)
        element.click()
        return True
    return False


def safe_input(driver, locator, text, timeout=10):
    """Безопасный ввод текста с ожиданием видимости"""
    if wait_for_element_visible(driver, locator, timeout):
        element = driver.find_element(*locator)
        element.clear()
        element.send_keys(text)
        return True
    return False


def get_element_text(driver, locator, timeout=10):
    """Получение текста элемента с ожиданием"""
    if wait_for_element_visible(driver, locator, timeout):
        element = driver.find_element(*locator)
        return element.text
    return ""


def is_element_displayed(driver, locator, timeout=5):
    """Проверка отображения элемента"""
    try:
        element = driver.find_element(*locator)
        return element.is_displayed()
    except:
        return False


def scroll_to_element(driver, locator):
    """Прокрутка к элементу"""
    try:
        element = driver.find_element(*locator)
        driver.execute_script("arguments[0].scrollIntoView();", element)
        sleep(0.5)  # Небольшая пауза для завершения прокрутки
        return True
    except:
        return False


def take_screenshot(driver, filename):
    """Создание скриншота"""
    try:
        driver.save_screenshot(filename)
        return True
    except:
        return False
