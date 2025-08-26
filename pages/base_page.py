from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class BasePage:
    """Базовый класс для всех Page Objects"""
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def find_element(self, locator, timeout=10):
        """Поиск элемента с ожиданием"""
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
        except TimeoutException:
            raise NoSuchElementException(f"Element {locator} not found within {timeout} seconds")
    
    def find_elements(self, locator, timeout=10):
        """Поиск элементов с ожиданием"""
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_all_elements_located(locator)
            )
        except TimeoutException:
            return []
    
    def click_element(self, locator, timeout=10):
        """Клик по элементу с ожиданием"""
        element = self.find_element(locator, timeout)
        element.click()
    
    def input_text(self, locator, text, timeout=10):
        """Ввод текста в поле с ожиданием"""
        element = self.find_element(locator, timeout)
        element.clear()
        element.send_keys(text)
    
    def get_text(self, locator, timeout=10):
        """Получение текста элемента"""
        element = self.find_element(locator, timeout)
        return element.text
    
    def is_element_present(self, locator, timeout=5):
        """Проверка наличия элемента"""
        try:
            self.find_element(locator, timeout)
            return True
        except (TimeoutException, NoSuchElementException):
            return False
    
    def wait_for_element_visible(self, locator, timeout=10):
        """Ожидание видимости элемента"""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False
    
    def scroll_to_element(self, locator):
        """Прокрутка к элементу"""
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
