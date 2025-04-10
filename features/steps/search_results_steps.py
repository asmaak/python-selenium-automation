from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


SEARCH_RESULTS_TEXT = (By.XPATH, "//div[@data-test='lp-resultsCount']")
ADD_CART_BUTTON_SIDE_NAV=(By.CSS_SELECTOR, "[data-test='orderPickupButton']")
ITEM_ADDED=(By.CSS_SELECTOR, "[data-test='modal-drawer-heading']")
SIDE_NAV_PRODUCT_NAME=(By.CSS_SELECTOR,"[data-test='content-wrapper'] h4")
LISTINGS=(By.CSS_SELECTOR,"[data-test='@web/site-top-of-funnel/ProductCardWrapper']")
PRODUCT_TITLE=(By.CSS_SELECTOR,"[data-test='product-title']")
PRODUCT_IMAGE=(By.CSS_SELECTOR,"[data-test='@web/ProductCard/ProductCardImage/primary']")

@then('Verify correct search results shown for {expected_text}')
def verify_search_results(context, expected_text):
    context.app.search_results_page.verify_search_results(expected_text)

@then('Verify {expected_text} in URL')
def verify_results_url(context, expected_text):
    context.app.search_results_page.verify_results_url(expected_text)



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
    context.app.search_results_page.click_add_to_cart_button()


@when('Store product name')
def store_product_name(context):
    context.driver.wait.until(
        EC.visibility_of_element_located(SIDE_NAV_PRODUCT_NAME),
        message='Product name not visible'
    )
    context.product_name= context.driver.find_element(*SIDE_NAV_PRODUCT_NAME).text
    print('product name store is :', context.product_name)

@when('Click on add to cart button from side navigation')
def click_on_add_to_cart_button_from_side_nav(context):
    context.driver.find_element(*ADD_CART_BUTTON_SIDE_NAV).click()
    sleep(6)
@then('Verify that every product has a name and an image')
def verify_product_name_and_image_(context):
    # To see ALL listings (comment out if you only check top ones):
    # context.driver.execute_script("window.scrollBy(0,2000)", "")
    # sleep(2)
    # context.driver.execute_script("window.scrollBy(0,1000)", "")
    # sleep(2)

    products= context.driver.find_elements(*LISTINGS)[:8]
    print(products)
    for product in products:
        title=product.find_element(*PRODUCT_TITLE).text
        assert title,'Product title not shown'
        print(title)
        product.find_element(*PRODUCT_IMAGE)