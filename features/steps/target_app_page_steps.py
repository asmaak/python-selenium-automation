from behave import given, when, then
from time import sleep

@given ('Open Target App page')
def open_target_app_page(context):
     context.app.target_app_page.open_target_app()

@given('Store original window')
def store_original_window(context):
    context.original_window = context.app.base_page.get_current_window_handle()
    # context.app.base_page.get_current_window_handle()
    # current_window=context.driver.current_window_handle
    # print('current', current_window)
    # context.driver.switch_to.window(current_window)
    # print('Original window:', context.original_window)
@when('Click Privacy Policy link')
def click_privacy_link(context):
    context.app.target_app_page.click_pp_link()
#
@when('Switch to new window')
def switch_to_new_window(context):
    context.app.base_page.switch_to_new_window()
@then('Verify Privacy Policy page opened')
def verify_app_open(context):
    context.app.target_app_page.verify_app_opened()
@then('Close current page')
def close_page(context):
    context.app.base_page.close()
@then('Return to original window')
def switch_to_original_window(context):
    context.app.base_page.switch_to_window_by_id(context.original_window)
