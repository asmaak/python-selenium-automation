from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


SEARCH_RESULTS_TEXT = (By.XPATH, "//div[@data-test='lp-resultsCount']")
ADD_CART_BUTTON_SIDE_NAV=(By.CSS_SELECTOR, "[data-test='orderPickupButton']")
ADD_CART_BUTTON=(By.CSS_SELECTOR, "[id*='addToCartButton']")
ITEM_ADDED=(By.CSS_SELECTOR, "[data-test='modal-drawer-heading']")

@then('Verify correct search results shown for {expected_text}')
def verify_search_results(context, expected_text):
    actual_text = context.driver.find_element(*SEARCH_RESULTS_TEXT).text
    assert expected_text in actual_text, f'Error. Text {expected_text} not in {actual_text}'

@given('Open target search products')
def open_target_main(context):
    context.driver.get('https://www.target.com/p/dakdk/-/A-92447823?preselect=86467779#lnk=sametab')
    sleep(6)

@when('Click on item to add in the cart')
def click_on_item(context):
    context.driver.find_element(By.CSS_SELECTOR, "#addToCartButtonOrTextIdFor86467779").click()

@then('Verify your item added')
def verify_item_added_to_cart(context):
    expected_result = 'Added to cart'
    actual_result = context.driver.find_element(*ITEM_ADDED).text
    assert expected_result == actual_result, f'Expected {expected_result} did not match actual {actual_result}'

@when('Click on add to cart button')
def click_on_add_to_cart_button(context):
    context.driver.find_element(*ADD_CART_BUTTON).click()
    sleep(6)

@when('Click on add to cart button from side navigation')
def click_on_add_to_cart_button_from_side_nav(context):
    context.driver.find_element(*ADD_CART_BUTTON_SIDE_NAV).click()
    sleep(6)
