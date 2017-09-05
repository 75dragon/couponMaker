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
startMonth = 10
startDate = 1
startYear = 2017
#number of coupons to print
numberOfPayments = 24
#price of each coupon
amount = "$2037.73"
lateFee = "$203.78"
lateAmount = "$2,241.51"
#who to pay each check to
payableToPerson = "Ling Meng"
rentalTenant = "Susanne Stevenson"
#where to mail the check to
mailToLine1 = "P O Box 700173"
mailToLine2 = "San Jose CA 95170"

#the address of the client
propertyAddress1 = "5Th Ave 2 North East"
propertyAddress2 = "Carmel, CA 93921"
#~~~~~~~~~~~~~~~~~~~~~~ Selenium Information ~~~~~~~~~~~~~~~~~~~~~~~~#
url = "https://accounts.google.com/signin/v2/identifier?service=wise&passive=true&continue=http%3A%2F%2Fdrive.google.com%2F%3Futm_source%3Den_US&utm_medium=button&utm_campaign=web&utm_content=gotodrive&usp=gtd&ltmpl=drive&urp=https%3A%2F%2Fwww.google.com%2F&flowName=GlifWebSignIn&flowEntry=ServiceLogin"
user = "drivefiletest@gmail.com"
pwd = "gdrivetest123"
driveLocation = "C:\\Users\\Austin Cheng\\Desktop\\chromedriver.exe"
timeDelay = 5
switchDelay = 2
#~~~~~~~~~~~~~~~~~~~ Coupon Making Information ~~~~~~~~~~~~~~~~~~~~~~#
couponDividerS = "----------------------------------------------------------------------------------------------------------------------------"
paymentNumberS = "Payment Number"
dueDateS = "Due Date"
paymentDueS = "Payment Due"
ifReceivedAfterS = "If Received After"
lateFeeAmountS = "Late Fee Amount"
LPADS = "Late Payment Amount Due"
couponNumber = 1
payableTo = "Payable To: "
mailTo = "Mail To: "
name = "Name: "
propertyAddress = "Property Address: "
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
actionChains = ActionChains(driver)
time.sleep(switchDelay)
actionChains.send_keys(u'\ue015').send_keys(u'\ue015').send_keys(u'\ue015').send_keys(u'\ue015').send_keys(u'\ue006').perform()
#move to the second window
time.sleep(switchDelay)
driver.switch_to_window(driver.window_handles[1])
#we are inside the google doc right now

for x in range(1, numberOfPayments + 1):
    actionChains = ActionChains(driver)
    time.sleep(switchDelay)
    actionChains.key_down(u'\ue00a').send_keys('b').key_up(u'\ue00a').send_keys(u'\ue015').send_keys(u'\ue014').send_keys(u'\ue014').send_keys(u'\ue014').send_keys(u'\ue014').send_keys(u'\ue014').send_keys(u'\ue014').send_keys(u'\ue015').send_keys(u'\ue007').perform()
    #do the first line of the table
    actionChains = ActionChains(driver)
    time.sleep(switchDelay)
    actionChains.send_keys(paymentNumberS).send_keys(u'\ue004').send_keys(dueDateS).send_keys(u'\ue004').send_keys(paymentDueS).send_keys(u'\ue004').send_keys(ifReceivedAfterS).send_keys(u'\ue004').send_keys(lateFeeAmountS).send_keys(u'\ue004').send_keys(LPADS).send_keys(u'\ue004').perform()
    #do the second line of the table
    actionChains = ActionChains(driver)
    time.sleep(switchDelay)
    actionChains.send_keys(str(couponNumber)).send_keys(u'\ue004').send_keys(str(startMonth) + '/' + str(startDate) + '/' + str(startYear)).send_keys(u'\ue004').send_keys(amount).send_keys(u'\ue004').send_keys(str(startMonth) + '/' + str(startDate + 9) + '/' + str(startYear)).send_keys(u'\ue004').send_keys(lateFee).send_keys(u'\ue004').send_keys(lateAmount).send_keys(u'\ue015').send_keys(u'\ue007').perform()
    #payable to and name
    actionChains = ActionChains(driver)
    time.sleep(switchDelay)
    actionChains.key_down(u'\ue009').send_keys('b').key_up(u'\ue009').send_keys(payableTo).key_down(u'\ue009').send_keys('b').key_up(u'\ue009').send_keys('     ').send_keys(payableToPerson + '                               ').key_down(u'\ue009').send_keys('b').key_up(u'\ue009').send_keys(name).key_down(u'\ue009').send_keys('b').key_up(u'\ue009').send_keys(rentalTenant).send_keys(u'\ue007').perform();
    #mail to line 1
    actionChains = ActionChains(driver)
    time.sleep(switchDelay)
    actionChains.key_down(u'\ue009').send_keys('b').key_up(u'\ue009').send_keys(mailTo).key_down(u'\ue009').send_keys('b').key_up(u'\ue009').send_keys('     ').send_keys(mailToLine1 + '                          ').key_down(u'\ue009').send_keys('b').key_up(u'\ue009').send_keys(propertyAddress).key_down(u'\ue009').send_keys('b').key_up(u'\ue009').send_keys(propertyAddress1).send_keys(u'\ue007').perform();
    #mail to line 2
    actionChains = ActionChains(driver)
    time.sleep(switchDelay)
    actionChains.send_keys('                  ' + mailToLine2).send_keys('                                                ').send_keys(propertyAddress2).send_keys(u'\ue007').perform();
    #divider
    actionChains = ActionChains(driver)
    time.sleep(switchDelay)
    actionChains.send_keys(u'\ue007').send_keys(couponDividerS).send_keys(u'\ue007').send_keys(u'\ue007').perform();
    startMonth = startMonth + 1;
    couponNumber = couponNumber + 1;
    if (startMonth > 12):
        startMonth = 1;
        startYear = startYear + 1;
