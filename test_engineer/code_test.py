# This is Carolyn's attempt at automating testing of the Todo application for Open Drives.

#Imports
from codeop import CommandCompiler
from msilib.schema import LaunchCondition, SelfReg
from pickle import TRUE
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.firefox import GeckoDriverManager


#As a side note and to maintain transparency, I did look up how to open webpages as I had never needed to open a webpage from within my code before.

#Opens the firefox browser and the application thus demonstrating that the application does run.
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver.maximize_window()
driver.get("http://localhost:3000") 

#Test ability to create a to-do list item




inputBlank = driver.find_element_by_xpath('/html/body/div/div/form/input')
addItemButton = driver.find_element_by_xpath('/html/body/div/div/form/button')

#Type new task into the inputBlank
inputBlank.send_keys("Wash laundry") 
addItemButton.click()
inputBlank.send_keys("Meal Prep") 
addItemButton.click()

time.sleep(5)

#Test ability to check off or complete a to-do list item


#Xpath /html/body/div/div/ul/li[1]/span
checkBox = driver.find_element_by_xpath('/html/body/div/div/ul/li[1]/span')
checkBox.click()
 
time.sleep(5)

#Test ability to uncheck a to-do list item


#Re-assigns the fourth list item to "checkBox" for the purposes of testing the ability to uncheck
checkBox = driver.find_element_by_xpath('/html/body/div/div/ul/li[4]/span')
checkBox.click() 
time.sleep(5)

#Test the ability to delete a to-do list item


#Xpath /html/body/div/div/ul/li[1]/button
deleteX = driver.find_element_by_xpath('/html/body/div/div/ul/li[1]/button')    
deleteX.click() #Deletes the first item in the todo list


#Keeps the browser open for a moment
time.sleep(10)
driver.quit()