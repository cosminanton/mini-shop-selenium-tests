from selenium.webdriver.common.by import By
from utils.helpers import wait_for_element, BASE_URL


class RegisterPage:
    """
    Reprezintă pagina de înregistrare.
    """

    URL = f"{BASE_URL}/register/"

    # Elementele paginii
    USERNAME_INPUT = (By.NAME, "username")
    EMAIL_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.NAME, "password")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

    def __init__(self, driver):
        self.driver = driver

    
    
    def open(self):
        """Deschide pagina de register"""
        self.driver.get(self.URL)
        return self

    def enter_username(self, username):
        field = wait_for_element(self.driver, *self.USERNAME_INPUT)
        field.clear()
        field.send_keys(username)
        return self

    def enter_email(self, email):
        field = wait_for_element(self.driver, *self.EMAIL_INPUT)
        field.clear()
        field.send_keys(email)
        return self

    def enter_password(self, password):
        field = wait_for_element(self.driver, *self.PASSWORD_INPUT)
        field.clear()
        field.send_keys(password)
        return self

    def submit(self):
        self.driver.find_element(*self.SUBMIT_BUTTON).click()
        return self

    def register(self, username, email, password):
        """Combină toți pașii într-o singură metodă"""
        self.open()
        self.enter_username(username)
        self.enter_email(email)
        self.enter_password(password)
        self.submit()
        return self

    def is_registered(self):
        """Verifică dacă înregistrarea a reușit — redirectează la home"""
        return self.driver.current_url == f"{BASE_URL}/"