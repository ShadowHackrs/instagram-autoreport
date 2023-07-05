banner = '''

      ░██████╗██╗░░██╗░█████╗░██████╗░░█████╗░░██╗░░░░░░░██╗  ██╗░░██╗░█████╗░░█████╗░██╗░░██╗███████╗██████╗░  
      ██╔════╝██║░░██║██╔══██╗██╔══██╗██╔══██╗░██║░░██╗░░██║  ██║░░██║██╔══██╗██╔══██╗██║░██╔╝██╔════╝██╔══██╗  
      ╚█████╗░███████║███████║██║░░██║██║░░██║░╚██╗████╗██╔╝  ███████║███████║██║░░╚═╝█████═╝░█████╗░░██████╔╝  
      ░╚═══██╗██╔══██║██╔══██║██║░░██║██║░░██║░░████╔═████║░  ██╔══██║██╔══██║██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗  
      ██████╔╝██║░░██║██║░░██║██████╔╝╚█████╔╝░░╚██╔╝░╚██╔╝░  ██║░░██║██║░░██║╚█████╔╝██║░╚██╗███████╗██║░░██║  
      ╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░░╚════╝░░░░╚═╝░░░╚═╝░░  ╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝  

                                        ██╗███╗░░██╗░██████╗████████╗░█████╗░  
                                        ██║████╗░██║██╔════╝╚══██╔══╝██╔══██╗  
                                        ██║██╔██╗██║╚█████╗░░░░██║░░░███████║  
                                        ██║██║╚████║░╚═══██╗░░░██║░░░██╔══██║  
                                        ██║██║░╚███║██████╔╝░░░██║░░░██║░░██║  
                                       ╚═╝╚═╝░░╚══╝╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝  

                     ░█████╗░██╗░░░██╗████████╗░█████╗░██████╗░███████╗██████╗░░█████╗░██████╗░████████╗
                     ██╔══██╗██║░░░██║╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝
                     ███████║██║░░░██║░░░██║░░░██║░░██║██████╔╝█████╗░░██████╔╝██║░░██║██████╔╝░░░██║░░░
                     ██╔══██║██║░░░██║░░░██║░░░██║░░██║██╔══██╗██╔══╝░░██╔═══╝░██║░░██║██╔══██╗░░░██║░░░
                     ██║░░██║╚██████╔╝░░░██║░░░╚█████╔╝██║░░██║███████╗██║░░░░░╚█████╔╝██║░░██║░░░██║░░░
                     ╚═╝░░╚═╝░╚═════╝░░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░░░░░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░
'''

print(banner)

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# Prompt the user for email and password
email = input("Enter your email or phone number: ")
password = input("Enter your password: ")

# Prompt the user for the account URL and number of reports
account_url = input("Enter the account URL you want to report: ")
report_count = int(input("Enter the number of reports you want to send: "))

chrome_options = Options()
chrome_options.add_argument("--disable-notifications")
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.instagram.com/accounts/login/")

time.sleep(4)
driver.find_element(By.NAME, "username").send_keys(email)
time.sleep(2)
driver.find_element(By.NAME, "password").send_keys(password)
driver.find_element(By.XPATH, '//button[@type="submit"]').click()
time.sleep(4)

def report_account():
    driver.get(account_url)
    time.sleep(4)
    dropdown_button = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/div[1]/div[2]/div')
    dropdown_button.click()                           
    time.sleep(2)
    report_button = driver.find_element(By.XPATH, '//button[contains(text(), "Report")]')
    report_button.click()
    time.sleep(2)
    inappropriate_button = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[3]/button[2]/div/div[1]')
    inappropriate_button.click()
    time.sleep(2)
    report_account_button = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[1]/button[1]/div/div[1]')
    report_account_button.click()
    time.sleep(3)
    report_account_button = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[1]/button[1]/div/div[1]')
    report_account_button.click()
    time.sleep(3)



for i in range(report_count):
    report_account()
    time.sleep(3)

driver.quit()
