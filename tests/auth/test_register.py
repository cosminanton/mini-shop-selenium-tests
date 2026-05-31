import pytest
import os
import time
from pages.register_page import RegisterPage

@pytest.mark.auth
class TestRegister:
    """
    Teste pentru pagina de înregistrare.

    """

    def test_register_new_user(self, driver):
        """
        Scenariul: Un utilizator nou se înregistrează cu succes.
        Așteptat: Este redirectat la homepage.
        """
        # Username unic la fiecare rulare
        username = f"testuser_{int(time.time())}"
        
        page = RegisterPage(driver)
        page.register(
            username=username,
            email=f"{username}@test.com",
            password=os.getenv("TEST_PASSWORD", "testpass123")
        )

        assert page.is_registered(), \
            f"Register failed! Current URL: {driver.current_url}"

    def test_register_redirects_to_home(self, driver):
        """
        Scenariul: După register, userul ajunge pe homepage.
        Așteptat: URL-ul e homepage-ul.
        """
        username = f"testuser2_{int(time.time())}"
        
        page = RegisterPage(driver)
        page.register(
            username=username,
            email=f"{username}@test.com",
            password="testpass123"
        )

        assert "/" in driver.current_url, \
            f"Expected redirect to home, got: {driver.current_url}"