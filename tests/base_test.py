"""
Default BaseTest object for setting up pytest fixtures for current browser configuration.
"""

import os
from pathlib import Path

import pytest
import yaml

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service as ServiceChrome
from selenium.webdriver.firefox.service import Service as ServiceFirefox
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

os.environ['WDM_LOG_LEVEL'] = '0'  # Hide WebDriver manager startup logs.


def config() -> yaml or Exception:
    path = Path(__file__).parent / "../data/config.yaml"
    if not os.path.exists(path):
        raise Exception(f"Failed to open config file path: {path}")
    try:
        with open(path) as config_file:
            data = yaml.load(config_file, Loader=yaml.CLoader)
        return data
    finally:
        config_file.close()


class BaseTest:

    @pytest.fixture(autouse=True)  # When this repo expands more fixtures like this will need to be in a separate file.
    def init_driver(self) -> None:
        if config()['browser'] == 'chrome':
            options = webdriver.ChromeOptions()
            if config()['headless']:
                options.add_argument('--headless')
                options.add_argument('--no-sandbox')
                options.add_argument('--disable-gpu')
                options.add_argument('--window-size=1920,1080')
            self.driver = webdriver.Chrome(service=ServiceChrome(ChromeDriverManager().install()), options=options)
        elif config()['browser'] == 'firefox':
            options = webdriver.FirefoxOptions()
            if config()['headless']:
                options.add_argument('--headless')
                options.add_argument('--no-sandbox')
                options.add_argument('--disable-gpu')
                options.add_argument('--window-size=1920,1080')
            self.driver = webdriver.Firefox(service=ServiceFirefox(GeckoDriverManager().install()), options=options)
        else:
            raise Exception("Incorrect Browser")

        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)
        yield self.wait, self.driver

        if self.driver is not None:
            self.driver.close()
            self.driver.quit()
