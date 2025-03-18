from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open target main page')
def open_target_main(context):
    context.driver.get('https://www.target.com/')
    sleep(6)


@when('Click on cart icon')
def click_sign_in(context):
    context.driver.find_element(By.CSS_SELECTOR,"[data-test='@web/CartIcon']").click()
    sleep(6)
@then('Verify Your cart is empty” message is shown')
def verify_cart_is_empty(context):
    actual_text = context.driver.find_element(By.XPATH, "//h1[text()='Your cart is empty']").text
    expected_text = 'Your cart is empty'
    assert expected_text in actual_text, f'Error. Text {expected_text} not in {actual_text}'


