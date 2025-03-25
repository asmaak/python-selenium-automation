from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep
PRODUCT_ID=(By.CSS_SELECTOR,"[data-test='product-title']")
COLOR_OPTIONS=(By.CSS_SELECTOR,"div[aria-label='Carousel'] li img")
SELECTED_COLOR = (By.CSS_SELECTOR, "[data-test='@web/VariationComponent'] div[aria-label*='color']")

@given('Open target product {product_id} page')
def open_product_page(context, product_id):
    context.driver.get(f'https://www.target.com/p/{product_id}')
    sleep(8)

    # context.driver.wait.until(
    #     EC.element_to_be_clickable(PRODUCT_ID),
    #     message ='Product title not clickable'
    # )
@then('Verify user can click through colors')
def verify_colors(context):
    expected_colors=['black/gum','dark khaki','grey','navy/tan','white/navy/red','white/sand/tan']
    actual_colors=[]
    colors=context.driver.find_elements(*COLOR_OPTIONS)
    for color in colors:
        color.click()
        selected_color = context.driver.find_element(*SELECTED_COLOR).text  # 'Color\nBlack'
        selected_color = selected_color.split('\n')[1]
        actual_colors.append(selected_color)
        # print("actual colors",actual_colors)
    assert expected_colors == actual_colors, f'Expected {expected_colors} did not match actual {actual_colors}'

