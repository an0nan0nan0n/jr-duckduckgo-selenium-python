"""
BasePage that all other page class objects inherit from.
"""
import selenium.webdriver
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver: selenium.webdriver, wait: WebDriverWait):
        self.driver = driver
        self.wait = wait

    def driver_get_url(self, url: str):
        self.driver.get(url)

    def get_title(self):
        return self.driver.title
