from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&')
driver.find_element(By.XPATH, "//a[@aria-label='www.amazon.com']")
driver.find_element(By.ID,"ap_email")
driver.find_element(By.ID,"continue")
driver.find_element(By.XPATH, "//a[contains(@href,'ap_signin_notification_condition_of_use')]")
driver.find_element(By.XPATH, "//a[contains(@href,'ref=ap_signin_notification_privacy_notice?')]")
driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']")
driver.find_element(By.ID,"auth-fpp-link-bottom")
driver.find_element(By.ID,"ap-other-signin-issues-link")
driver.find_element(By.ID,"createAccountSubmit")







