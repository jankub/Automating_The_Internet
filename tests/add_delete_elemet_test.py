import time

from pages import add_delete_element
import unittest

from playwright.sync_api import sync_playwright
from playwright.sync_api._generated import Playwright


# before test:
#     -open browser
#     -create page
#     -get page object
#     -do test
#     -close browser

class AddDeleteTest(unittest.TestCase):

    def setUp(self) -> None:
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=False)
        self.context = self.browser.new_context()
        self.page = self.context.new_page()
        self.add_delete_page = add_delete_element.AddDeleteElem(self.page)

    def tearDown(self) -> None:
        self.browser.close()
        self.playwright.stop()
        print('tear down')

    def test_add_button_exists(self):
        assert self.add_delete_page.add_button.is_visible() is True

    def test_add_button_clickable(self):
        self.add_delete_page.add_button.click()
        time.sleep(2)
