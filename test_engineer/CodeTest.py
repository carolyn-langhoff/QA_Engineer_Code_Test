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


#As a side note and to maintain transparency, I did look up how to open webpages as I had never needed to open a webpage from within my code before.

#Opens the firefox browser and the application thuse demonstrating that the application does run.
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver.maximize_window()
driver.get("http://localhost:3000") 




#Keeps the browser open for a moment
time.sleep(3)
driver.quit()