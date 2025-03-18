from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# Start Chrome browser:
driver_path = ChromeDriverManager().install()
driver = webdriver.Chrome(service=Service(driver_path))
driver.maximize_window()
driver.implicitly_wait(5)

# Open amazon create page
driver.get('https://www.amazon.com/ap/register?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3F_encoding%3DUTF8%26ref_%3Dnav_newcust&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0')
sleep(5)
driver.find_element(By.CSS_SELECTOR,'.a-icon-logo')
driver.find_element(By.CSS_SELECTOR,'h1.a-spacing-small')
driver.find_element(By.CSS_SELECTOR,'#ap_customer_name')
driver.find_element(By.CSS_SELECTOR,'#ap_email')
driver.find_element(By.CSS_SELECTOR,'#ap_password')
driver.find_element(By.XPATH,"//div[contains(text(), 'Passwords must be')]")
driver.find_element(By.CSS_SELECTOR,'#ap_password_check')
driver.find_element(By.CSS_SELECTOR,'#continue')
driver.find_element(By.CSS_SELECTOR,"[href*='notification_condition']")
driver.find_element(By.CSS_SELECTOR,"[href*='notification_privacy']")
driver.find_element(By.CSS_SELECTOR,"[href*='signin']")







# driver.find_element(, "//*[@data-test='@web/AccountLink']").click()
#
# driver.find_element(By.XPATH, "//*[@data-test='accountNav-signIn']").click()
#
# # Verification
# expected = 'Sign into your Target account'
# actual = driver.find_element(By.XPATH, "//h1[contains(@class, 'styles_ndsHeading')]").text
# assert expected == actual, f'Expected {expected} did not match actual {actual}'
#
# # OR:
# # driver.find_element(By.XPATH, "//span[text()='Sign into your Target account']")
#
# # Make sure login button is shown
# driver.find_element(By.ID, 'login')