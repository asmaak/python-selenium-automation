from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
SUBTOTAL_CART=(By.XPATH, "//div[./span[contains(text(), 'subtotal')]]")

@when('Open cart page')
def open_target_main(context):
    context.driver.get('https://www.target.com/cart')
    sleep(2)

@then("Verify 'Your cart is empty' message is shown")
def verify_cart_empty(context):
    expected_result = 'Your cart is empty'
    actual_result = context.driver.find_element(By.CSS_SELECTOR, "[data-test='boxEmptyMsg']").text
    assert expected_result == actual_result, f'Expected {expected_result} did not match actual {actual_result}'

@then("Verify cart has {amount} item")
def verify_cart_has_1_item(context,amount):
    actual_result = context.driver.find_element(*SUBTOTAL_CART).text
    assert f'{amount} item' in actual_result, f'Expected {amount} items but got {actual_result}'
