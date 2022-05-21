# This is Carolyn's attempt at automating testing of the Todo application for Open Drives.

#Imports
from codeop import CommandCompiler
from pickle import TRUE
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.firefox import GeckoDriverManager


#Variables
firstItem = "Meal Prep"
secondItem = "Wash Laundry"

#As a side note and to maintain transparency, I did look up how to open webpages as I had never needed to open a webpage from within my code before.

#Opens the firefox browser and the application thus demonstrating that the application does run.
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver.maximize_window()
driver.get("http://localhost:3000") 


#Test ability to create a to-do list item
@pytest.mark.input #Planning to run all tests using markers
def TestAdd():
    inputBlank = driver.find_element_by_xpath('/html/body/div/div/form/input')
    addItemButton = driver.find_element_by_xpath('/html/body/div/div/form/button')

    #Type new task into the inputBlank
    inputBlank.send_keys("secondItem") 
    addItemButton.click()
    inputBlank.send_keys("firstItem") 
    addItemButton.click()

    #Assigns the Xpath of the first and second todo list items to variables in order to allow validation using assert
    firstTodo = driver.find_element_by_xpath('/html/body/div/div/ul/li[1]')
    secondTodo = driver.find_element_by_xpath('/html/body/div/div/ul/li[2]')

    #Used to compare the contents of the first to-do list item and the intended input in order to test the functionality of adding an
    assert inputBlank.send_keys == TRUE #Attempt to test that the inputBlank is being typed into
    
    assert firstItem in firstTodo #Attempt to test that the given input "Meal Prep" is in the first item on the todo list (Should be since this test occurs after both items are added.)
    assert secondItem == secondTodo #Attempt to test that the second item on the todo list is equal to the variable that was input


time.sleep(5)

#Test ability to check off or complete a to-do list item
@pytest.mark.checkBox
def TestCheckBox():
    #Xpath /html/body/div/div/ul/li[1]/span
    checkBox = driver.find_element_by_xpath('/html/body/div/div/ul/li[1]/span')
    checkBox.click()
    assert checkBox.checked() == TRUE #Not sure if .checked() will work just testing it

    time.sleep(5)

    #Test ability to uncheck a to-do list item
    #Re-assigns the fourth list item to "checkBox" for the purposes of testing the ability to uncheck
    checkBox = driver.find_element_by_xpath('/html/body/div/div/ul/li[4]/span')
    checkBox.click() 
    assert checkBox.onClickDone() == "undone" #Different way of testing if the check box is checked/unchecked to see if that works.
    time.sleep(5)

#Test the ability to delete a to-do list item
@pytest.mark.delete
def TestDelete():
    #Xpath /html/body/div/div/ul/li[1]/button
    deleteX = driver.find_element_by_xpath('/html/body/div/div/ul/li[1]/button')    
    deleteX.click() #Deletes the first item in the todo list
    assert deleteX.onClickClose() == TRUE #Testing to see if the item was deleted, however a new item would be in that spot, so it may not work.

#Keeps the browser open for a moment
time.sleep(10)
driver.quit()