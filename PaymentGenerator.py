from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime
from datetime import datetime
import time
import os
import getpass
#~~~~~~~~~~~~~~~~~~~~~~~ Client Information ~~~~~~~~~~~~~~~~~~~~~~~~~~#
#above below the date 1/1/2017
startMonth = 1
startDate = 1
startYear = 2017
#number of coupons to print
numberOfPayments = 12
#price of each coupon
price = "$100.00"
#who to pay each check to
payableTo = "Hua Cheng"
#where to mail the check to
mailToLine1 = "P O Box 700173"
mailToLine2 = "San Jose CA 95129"
#the clients name
clientName = "Thomas Nichols"
#the address of the client
propertyAddress1 = "43905 North Dome Ct"
propertyAddress2 = "Coarsegold, CA 94112"
#~~~~~~~~~~~~~~~~~~~~~~ Selenium Information ~~~~~~~~~~~~~~~~~~~~~~~~#
url = "https://accounts.google.com/signin/v2/identifier?service=wise&passive=true&continue=http%3A%2F%2Fdrive.google.com%2F%3Futm_source%3Den_US&utm_medium=button&utm_campaign=web&utm_content=gotodrive&usp=gtd&ltmpl=drive&urp=https%3A%2F%2Fwww.google.com%2F&flowName=GlifWebSignIn&flowEntry=ServiceLogin"
user = "drivefiletest@gmail.com"
pwd = "gdrivetest123"
driveLocation = "C:\\Users\\austi\\Desktop\\chromedriver.exe"
timeDelay = 25
switchDelay = 2
documentName = str(numberOfPayments) + " payments from " + clientName
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Code ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
driver = webdriver.Chrome(driveLocation)
driver.get(url)

#email
emailLoginElem = WebDriverWait(driver, timeDelay).until(EC.visibility_of_element_located((By.XPATH, '//input[@type="email"]')))
emailLoginElem.send_keys(user)
nextElem = WebDriverWait(driver, timeDelay).until(EC.visibility_of_element_located((By.XPATH, '//div[@id="identifierNext"]')))
nextElem.click()

#password
passLoginElem =  WebDriverWait(driver, timeDelay).until(EC.visibility_of_element_located((By.XPATH, '//input[@type="password"]')))
passLoginElem.send_keys(pwd)
nextElem = WebDriverWait(driver, timeDelay).until(EC.visibility_of_element_located((By.XPATH, '//div[@id="passwordNext"]')))
nextElem.click()

WebDriverWait(driver, timeDelay).until(EC.presence_of_element_located((By.XPATH, '//*[@id="drive_main_page"]/div[2]/div/div[1]/div/div/div[3]/div[2]/div/div[2]/div/div[1]/div/div')))
myDriveElem = WebDriverWait(driver, timeDelay).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="drive_main_page"]/div[2]/div/div[1]/div/div/div[3]/div[2]/div/div[2]/div/div[1]/div/div')))
#making a document, slides, then speadsheet
#click the My Drive button
myDriveElem.click()
#click the make document method
makeDocumentElem = WebDriverWait(driver, timeDelay).until(EC.visibility_of_element_located((By.XPATH, '//div[@class="h-w a-w h-w a-w-Xi a-w-Mr"]/div[@class="a-w-x"]/div[6]')))
makeDocumentElem.click();
#move to the second window
time.sleep(switchDelay)
driver.switch_to_window(driver.window_handles[1])

print(BOLD + "Giving the document a name of: " + documentName + END)

renameElem = WebDriverWait(driver, timeDelay).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="docs-title-widget"]/input')))
renameElem.clear()
renameElem.send_keys("")
renameElem.send_keys(documentName)
renameElem.send_keys(u'\ue006')
time.sleep(switchDelay)
#share with a friend
