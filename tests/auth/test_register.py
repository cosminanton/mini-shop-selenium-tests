import pytest
import os
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
        page = RegisterPage(driver)
        page.register(
            username=os.getenv("TEST_USERNAME", "testuser"),
            email=os.getenv("TEST_EMAIL", "test@test.com"),
            password=os.getenv("TEST_PASSWORD", "testpass123")
        )

        assert page.is_registered(), \
            f"Register failed! Current URL: {driver.current_url}"

    def test_register_redirects_to_home(self, driver):
        """
        Scenariul: După register, userul ajunge pe homepage.
        Așteptat: URL-ul e homepage-ul.
        """
        page = RegisterPage(driver)
        page.register(
            username="testuser2",
            email="test2@test.com",
            password="testpass123"
        )

        assert "/" in driver.current_url, \
            f"Expected redirect to home, got: {driver.current_url}"