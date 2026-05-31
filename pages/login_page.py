from selenium.webdriver.common.by import By
from utils.helpers import wait_for_element, wait_for_url, BASE_URL


class LoginPage:
    """
    Reprezintă pagina de login.
    Conține toate elementele și acțiunile posibile pe această pagină.
    """

    URL = f"{BASE_URL}/login/"

    # Elementele paginii — selectori CSS/NAME
    USERNAME_INPUT = (By.NAME, "username")
    PASSWORD_INPUT = (By.NAME, "password")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".alert, .error, .invalid-feedback")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        """Deschide pagina de login"""
        self.driver.get(self.URL)
        return self

    def enter_username(self, username):
        field = wait_for_element(self.driver, *self.USERNAME_INPUT)
        field.clear()
        field.send_keys(username)
        return self

    def enter_password(self, password):
        field = wait_for_element(self.driver, *self.PASSWORD_INPUT)
        field.clear()
        field.send_keys(password)
        return self

    def submit(self):
        self.driver.find_element(*self.SUBMIT_BUTTON).click()
        return self

    def login(self, username, password):
        """Combină toți pașii de login într-o singură metodă"""
        self.open()
        self.enter_username(username)
        self.enter_password(password)
        self.submit()
        return self

    def is_logged_in(self):
        """Verifică dacă login-ul a reușit"""
        return "/login/" not in self.driver.current_url