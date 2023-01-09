import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from instafollowers import InstaFollowers


options=Options()
options.add_experimental_option("detach",True)
options.add_argument("start-maximized")


chrome_driver_path="C:\\Users\\USER\\Desktop\\my_python\\chromedriver.exe"
website_URL='https://instagram.com'

driver=webdriver.Chrome(service_log_path=chrome_driver_path,options=options)

SIMILAR_ACC='aubree.valentine_'
INSTA_ID='your_email'
INSTA_PASSWORD='your_password'

driver.get(website_URL)
time.sleep(5)
username=driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[1]/div/label/input')
username.send_keys(INSTA_ID)
password=driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[2]/div/label/input')
password.send_keys(INSTA_PASSWORD)
time.sleep(2)
log_in=driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[3]/button')
log_in.click()
time.sleep(15)
print("logged in successfully")
print(driver.window_handles)

# driver.switch_to()
# heading=driver.find_element(By.XPATH,'//*[@id="mount_0_0_5W"]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/h2')
# print(heading.text)

# WebDriverWait(driver,40).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="mount_0_0_96"]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]'))).click()

# no_notify=driver.find_element(By.XPATH,'//*[@id="mount_0_0_96"]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')
# no_notify.click()
time.sleep(2)
search=driver.find_element(By.XPATH,'//*[@id="mount_0_0_fD"]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div[1]/div/div[2]/div[2]/div/a/div/div/div/div/svg')
search.click()
time.sleep(2)
search_bar=driver.find_element(By.XPATH,'//*[@id="mount_0_0_fD"]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[1]/div/input')
search.send_keys(SIMILAR_ACC)
time.sleep(2)
first_id=driver.find_element(By.XPATH,'//*[@id="mount_0_0_fD"]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div/a/div')
first_id.click()
follows_link=driver.find_element(By.XPATH,'//*[@id="mount_0_0_fD"]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/header/section/ul/li[2]/a/div')
follows_link.click()
time.sleep(2)
acc_div=driver.find_elements(By.XPATH,'//*[@id="mount_0_0_fD"]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div')
for acc in acc_div:
    print(acc.text)

