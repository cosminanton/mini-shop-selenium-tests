import pytest
import os
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv

load_dotenv(Path(__file__).parent / ".env")

BASE_URL = os.getenv("BASE_URL", "https://cosminstore.onrender.com")

@pytest.fixture(scope="session")
def driver():
    """
    Pornește Chrome o singură dată pentru toată sesiunea de teste.
    scope="session" = un singur browser pentru toate testele
    """
    options = webdriver.ChromeOptions()
    
    if os.getenv("HEADLESS", "true") == "true":
        options.add_argument("--headless")  # fără UI vizibil
    
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    driver.implicitly_wait(10)  # așteaptă max 10s pentru elemente
    
    yield driver  # dă browser-ul testelor
    
    driver.quit()  # închide browser-ul la final

@pytest.fixture(scope="session", autouse=True)
def warmup(driver):
    """Trezeste Render inainte de teste"""
    import time
    driver.get("https://cosminstore.onrender.com")
    time.sleep(5)  # așteaptă puțin pentru a se asigura că Render e trezit
    
@pytest.fixture
def base_url():
    return BASE_URL