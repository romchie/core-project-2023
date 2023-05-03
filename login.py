import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def main():

    url = "https://brightspace.binghamton.edu/"
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)

    browser = webdriver.Chrome(options=chrome_options)
    browser.get(url)

    username = browser.find_element(By.ID, "username")
    password = browser.find_element(By.ID, "password")

    cert_file = open(".credentials", 'r')
    credentials = cert_file.readlines()
    cert_file.close()
    username.send_keys(credentials[0].strip())
    password.send_keys(credentials[1].strip())
    login_button = browser.find_element(By.NAME, "submit")
    login_button.click()

    try:
        token = browser.find_element(By.NAME, "token")
    except:
        sys.exit("Unable to sign in. Try resetting username and password with [make resetuserpass]")

    verification = input("Enter 2FA code: ")
    token.send_keys(verification)
    token_login_button = browser.find_element(By.XPATH, "//form[@id='fm1']/button[1]")
    token_login_button.click()
    print("You've been successfully logged in!")

main()