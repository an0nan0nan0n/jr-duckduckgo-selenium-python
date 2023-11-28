"""
Locators for all test pages.
"""

from selenium.webdriver.common.by import By


class SearchPageLocators:
    SEARCH_INPUT = (By.XPATH, "//*[@id='searchbox_input']")
    SEARCH_BUTTON = (By.XPATH, "//*[@aria-label='Search']")
    RESULTS = (By.XPATH, "//*[@data-testid='mainline']//*[@data-testid='result']")
