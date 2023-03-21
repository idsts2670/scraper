# import libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as bs
import re as re
import time
import pandas as pd
import os

# data input
# The location of the web driver in your system, a username, and a password to log in with
## https://www.linkedin.com/
## first get the chrome webdriver on your local: https://bit.ly/3FHqvF7
## my webdriver path: /Users/satoshiido/Documents/chromedriver_mac_arm64/chromedriver
PATH = input("Enter the Webdriver path: ")
## input your linkedin account username or email address
USERNAME = input("Enter the username: ")
## input your linkedin account password
PASSWORD = input("Enter the password: ")
print(PATH)
print(USERNAME)
print(PASSWORD)


# web launch
# web documents of WebDriver for Chrome: https://chromedriver.chromium.org/getting-started
# how to include the ChromeDriver location in Mac OS System PATH: https://bit.ly/3lvBnz3
# when you get error: "“chromedriver” cannot be opened because the developer cannot be verified": https://bit.ly/3lqukb1
driver = webdriver.Chrome(PATH)
time.sleep(5)
driver.get("https://www.linkedin.com/uas/login")
time.sleep(5)
