from behave import given, when, then


@given('Add Element page url')
def step_impl(context):
    context.url = 'https://the-internet.herokuapp.com/add_remove_elements/'


@when('page loaded')
def step_impl(context):
    context.add_delete_page.goto(context.url)


@then('button Add Element can be located on page')
def step_impl(context):
    assert context.add_delete_page.add_button.is_visible() is True


@given('Add Element page loaded')
def step_impl(context):
    context.url = 'https://the-internet.herokuapp.com/add_remove_elements/'


@when('Add Element button clicked {number} of times')
def step_impl(context, number):
    context.add_delete_page.goto(context.url)
    for _ in range(int(number)):
        context.add_delete_page.add_button.click()


@then('{number} Delete buttons added')
def step_impl(context, number):
    count = context.add_delete_page.get_added_buttons_count()
    assert count == int(number)
