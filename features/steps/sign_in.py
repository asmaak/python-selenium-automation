from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

@then('Verify Sign In form opened')
def verify_sign_in(context):
    context.app.sign_in_page.verify_sign_in_page_opened()