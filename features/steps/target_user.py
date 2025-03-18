from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open target main page')
def open_target_main(context):
    context.driver.get('https://www.target.com/')

@when('Click on cart icon')
def click_sign_in(context):
    context.driver.find_element(By.CSS_SELECTOR,"[data-test='@web/CartIcon']").click()
    sleep(6)
@then('Verify Your cart is empty” message is shown')
def verify_cart_is_empty(context):
    actual_text = context.driver.find_element(By.XPATH, "//h1[text()='Your cart is empty']").text
    expected_text = 'Your cart is empty'
    assert expected_text in actual_text, f'Error. Text {expected_text} not in {actual_text}'


@when('Click Sign In')
def click_sign_in(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/AccountLink']").click()
    sleep(6)

@when('click Sign In side menu')
def click_sign_in_side_menu(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='accountNav-signIn']").click()
    sleep(6)


@then('Verify Sign In form opened')
def verify_sign_in_form(context):
    actual_text = context.driver.find_element(By.XPATH, "//h1[contains(@class, 'styles_ndsHeading')]").text
    expected_text = 'Sign in'
    assert expected_text in actual_text, f'Error. Text {expected_text} not in {actual_text}'




