from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

HEADER_LINKS = (By.CSS_SELECTOR, "[id*='utilityNav']")


@given('Open target main page')
def open_target_main(context):
    context.app.main_page.open_main_page()
    #
    # context.driver.wait.until(
    #     EC.element_to_be_clickable(SEARCH_FIELD),
    #     message='Search field not clickable'
    # )


@when('Search for {search_word}')
def search_product(context, search_word):
    context.app.header.search(search_word)
    sleep(6)


@when('Click on Cart icon')
def click_cart(context):
    context.app.header.click_cart()

@when('Click Sign In')
def click_sign_in(context):
    context.app.header.click_sign_in()
@when('Navigate to side menu and click Sign In')
def navigate_to_side_menu(context):
    context.app.side_menu.navigate_to_side_menu()
@then('Verify at least 1 link shown')
def verify_1_header_link_shown(context):
    link = context.driver.find_element(*HEADER_LINKS)
    print(link)


@then('Verify {link_amount} links shown')
def verify_all_header_links_shown(context, link_amount):
    link_amount = int(link_amount) # "6" => int 6
    links = context.driver.find_elements(*HEADER_LINKS)
    print(links)
    assert len(links) == link_amount, f'Expected {link_amount} links, but got {len(links)}'