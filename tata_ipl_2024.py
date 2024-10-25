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

# Navigate to the batting statistics section
driver.find_element(By.XPATH, '//*[@id="battingTAB"]/div/a').click()
time.sleep(2)

# Initialize lists to store the data
bats = []
runs = []
total_matches = []
HS = []
avg_score = []
SR = []
hundreds = []
fifties = []
fours = []
sixes = []

# Extract batsman names
batsmans = driver.find_elements(By.CSS_SELECTOR, '.st-ply-name.ng-binding')
for batsman in batsmans:
    bats.append(batsman.text)

#extrect total runs 
run_class = driver.find_elements(By.XPATH, '//table/tbody/tr/td[3]')
for run in run_class:
    runs.append(run.text)

#Extract total matches played 
matches = driver.find_elements(By.XPATH, '//table/tbody/tr/td[4]')
for match in matches:
    total_matches.append(match.text)