import pytest


@pytest.mark.login_page
class TestLoginFunctionality:

    def test_check_title(self, login_page):
        login_page.login_title_exists()

    @pytest.mark.parametrize('username, password, result_text', (
            ('admin@admin.ru', '1234', 'Welcome ! user'),
            ('admin123@admin.ru', '1234567', 'Login failed'),
    ))
    def test_login(self, login_page, username, password, result_text):
        login_page.login(username, password)
        login_result = login_page.get_text_after_login()
        assert login_result == result_text
