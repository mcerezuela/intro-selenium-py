"""
This module contains shared fixtures.
"""

import pytest
import selenium.webdriver


@pytest.fixture
def browser():
  #Drivers
  CHROME_DRIVER_PATH = '../chromedriver.exe'

  # Initialize the ChromeDriver instance
  b = selenium.webdriver.Chrome(CHROME_DRIVER_PATH)

  # Make its calls wait up to 10 seconds for elements to appear
  b.implicitly_wait(10)

  # Return the WebDriver instance for the setup
  yield b

  # Quit the WebDriver instance for the cleanup
  b.quit()
