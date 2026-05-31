import os
from pathlib import Path
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Găsește .env indiferent de unde rulează pytest
load_dotenv(Path(__file__).parent.parent / ".env")

BASE_URL = os.getenv("BASE_URL", "https://cosminstore.onrender.com")

def login(driver, username=None, password=None):
    """
    Funcție reutilizabilă de login.
    O apelăm din orice test care necesită autentificare.
    """
    username = username or os.getenv("TEST_USERNAME", "testuser")
    password = password or os.getenv("TEST_PASSWORD", "testpass123")
    
    driver.get(f"{BASE_URL}/login/")
    
    driver.find_element(By.NAME, "username").clear()
    driver.find_element(By.NAME, "username").send_keys(username)
    driver.find_element(By.NAME, "password").clear()
    driver.find_element(By.NAME, "password").send_keys(password)
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

def wait_for_element(driver, by, value, timeout=10):
    """
    Așteaptă până când un element apare în pagină.
    Util când pagina se încarcă mai lent.
    """
    return WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((by, value))
    )

def wait_for_url(driver, url, timeout=10):
    """
    Așteaptă până când URL-ul se schimbă la cel așteptat.
    """
    WebDriverWait(driver, timeout).until(
        EC.url_contains(url)
    )