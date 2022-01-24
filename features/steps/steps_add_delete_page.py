from behave import given, when, then

'''Scenario: Add Element button is loaded'''
@given('Add Element page url')
def step_impl(context):
    context.url = 'https://the-internet.herokuapp.com/add_remove_elements/'


@when('page loaded')
def step_impl(context):
    context.add_delete_page.goto(context.url)


@then('button Add Element can be located on page')
def step_impl(context):
    assert context.add_delete_page.add_button.is_visible() is True


'''Scenario Outline: Delete button adding'''
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


'''Scenario: Delete button action'''
@given('Add Element page loaded and {number} of delete buttons visible')
def step_impl(context, number):
    context.url = 'https://the-internet.herokuapp.com/add_remove_elements/'
    context.add_delete_page.goto(context.url)
    for _ in range(int(number)):
        context.add_delete_page.add_button.click()


@when('Any delete button clicked {number_click} of times')
def step_impl(context, number_click):
    for _ in range(int(number_click)):
        button_delete = context.add_delete_page.added_buttons.first
        button_delete.click()


@then('{number_rem} of delete buttons remains')
def step_impl(context, number_rem):
    count = context.add_delete_page.get_added_buttons_count()
    assert count == int(number_rem)
