from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


CELL_ITEMS=(By.CSS_SELECTOR, ".cell-item-content")
@given('Open circle page')
def open_circle_main(context):
    context.driver.get('https://www.target.com/circle')
    sleep(6)

@then('verify {number_benefits} benefit cells')
def verify_number_of_benefits(context, number_benefits):
    number_benefits=int(number_benefits)
    cells = context.driver.find_elements(*CELL_ITEMS)
    print(cells)
    assert len(cells) >= number_benefits, f'Expected {number_benefits} links, but got {len(cells)}'
