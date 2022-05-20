# This is Carolyn's attempt at automating testing of the Todo application for Open Drives.

#Imports
import time
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager


 #The following is a test to make sure selenium, node js, etc. are running correctly

#Opens the firefox browser
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver.maximize_window()
driver.get("https://google.com")

#Keeps the browser open for a moment
time.sleep(3)
driver.quit()