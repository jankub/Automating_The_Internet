from playwright.sync_api import Page

class AddDeleteElem:

    add_button_selector = '//*[@id="content"]/div/button'
    added_buttons_selector = '//*[@id="elements"]/*'

    def __init__(self, page: Page) -> None:
        self.page = page
        self.add_button = page.locator(AddDeleteElem.add_button_selector)
        self.added_buttons = page.locator(AddDeleteElem.added_buttons_selector)

    def add_button_visible(self):
        return self.add_button.is_visible()

    def get_added_buttons_count(self):
        return self.added_buttons.count()

    def goto(self, url):
        self.page.goto(url)
        return self


