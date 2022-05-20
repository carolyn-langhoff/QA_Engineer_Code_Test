# This is Carolyn's attempt at automating testing of the Todo application for Open Drives.

#Imports
from codeop import CommandCompiler
from msilib.schema import LaunchCondition, SelfReg
import time
from urllib.request import urlopen
from selenium import webdriver
from setuptools import Command
import urllib3
from webdriver_manager.firefox import GeckoDriverManager




 #The following is a test to make sure selenium, node js, etc. are running correctly

#Opens the firefox browser and the application
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver.maximize_window()
driver.get("http://localhost:3000") 




#Keeps the browser open for a moment
time.sleep(3)
driver.quit()