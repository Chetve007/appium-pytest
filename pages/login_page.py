from appium.webdriver.common.appiumby import AppiumBy
from .base_page import BasePage


class LoginPage(BasePage):
    """Page Object для страницы логина"""
    
    # Локаторы элементов
    USERNAME_FIELD = (AppiumBy.ID, "com.example.login:id/username")
    PASSWORD_FIELD = (AppiumBy.ID, "com.example.login:id/password")
    LOGIN_BUTTON = (AppiumBy.ID, "com.example.login:id/login")
    LOGIN_TITLE = (AppiumBy.ID, "com.example.login:id/toolbar")
    LOGIN_RESULT = (AppiumBy.ID, "com.example.login:id/succestext")
    
    def enter_username(self, username):
        """Ввод имени пользователя"""
        self.input_text(self.USERNAME_FIELD, username)
    
    def enter_password(self, password):
        """Ввод пароля"""
        self.input_text(self.PASSWORD_FIELD, password)
    
    def click_login_button(self):
        """Клик по кнопке входа"""
        self.click_element(self.LOGIN_BUTTON)
    
    def login(self, username, password):
        """Выполнение полного процесса логина"""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()

    def login_title_exists(self):
        self.is_element_present(self.LOGIN_TITLE)

    def get_text_after_login(self):
        return self.get_text(self.LOGIN_RESULT)
    
    def clear_username_field(self):
        """Очистка поля имени пользователя"""
        element = self.find_element(self.USERNAME_FIELD)
        element.clear()
    
    def clear_password_field(self):
        """Очистка поля пароля"""
        element = self.find_element(self.PASSWORD_FIELD)
        element.clear()
    
    def get_username_field_text(self):
        """Получение текста из поля имени пользователя"""
        return self.get_text(self.USERNAME_FIELD)
    
    def get_password_field_text(self):
        """Получение текста из поля пароля"""
        return self.get_text(self.PASSWORD_FIELD)
