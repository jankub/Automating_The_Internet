from playwright.sync_api import sync_playwright
from pages.add_delete_element import AddDeleteElem


def before_feature(context, scenario):
    context.manager = sync_playwright()
    context.playwright = context.manager.start()
    context.browser = context.playwright.chromium.launch(headless=False)
    context.context = context.browser.new_context()
    context.page = context.context.new_page()
    context.add_delete_page = AddDeleteElem(context.page)


def after_feature(context, scenario):
    context.manager.__exit__()
