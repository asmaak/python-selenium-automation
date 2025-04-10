from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
SUBTOTAL_CART=(By.XPATH, "//div[./span[contains(text(), 'subtotal')]]")
CART_ITEM_TITLE=(By.CSS_SELECTOR,"[data-test='cartItem-title']")

@when('Open cart page')
def open_target_main(context):
    context.app.cart_page.open()
    # context.driver.get('https://www.target.com/cart')
    # sleep(2)

@then("Verify 'Your cart is empty' message is shown")
def verify_cart_empty(context):
    context.app.cart_page.cart_empty()


@then("Verify cart has {amount} item(s)")
def verify_cart_has_1_item(context,amount):
    context.app.cart_page.verify_cart_has_items(amount)


@then('Verify cart has correct product')
#store before context.product_name
def verify_cart_has_correct_product(context):
     product_name_in_cart= context.driver.find_element(*CART_ITEM_TITLE).text
     print(f'product name in the cart: {product_name_in_cart}')
     # assert context.product_name in product_name_in_cart, f'Expected {context.product_name} in cart but got {product_name_in_cart}'
     assert context.product_name[0:20] == product_name_in_cart[:20], f'Expected {context.product_name[:20] }  did not match {product_name_in_cart[:20]}'

     # assert context.product_name == product_name_in_cart, f'Expected {context.product_name }  did not match {product_name_in_cart}'
@then('Verify correct page open')
def verify_page_opened(context):
    context.app.cart_page.verify_cart_page_opens()

