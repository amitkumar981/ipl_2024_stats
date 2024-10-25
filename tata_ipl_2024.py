# importing necessary libraries
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
import time

# Website URL and WebDriver path
website = 'https://www.iplt20.com/stats/2024'
path = r"C:\Users\redhu\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"
s = Service(path)

# Start WebDriver
driver = webdriver.Chrome(service=s)
driver.get(website)
time.sleep(5)

