# importing necessary libraries
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
import time

# Website URL and WebDriver path
website = 'https://www.iplt20.com/stats/2022'
path = r"C:\Users\redhu\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"
s = Service(path)

# Start WebDriver
driver = webdriver.Chrome(service=s)
driver.get(website)
time.sleep(5)

# Navigate to the batting statistics section
driver.find_element(By.XPATH,'//*[@id="battingTAB"]/div/a').click()
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

# Extrect highest score 
highest_score = driver.find_elements(By.XPATH, '//table/tbody/tr/td[7]')
for hs in highest_score:
    HS.append(hs.text)

#extract highest score
average_score = driver.find_elements(By.XPATH, '//table/tbody/tr/td[8]')
for avg in average_score:
    avg_score.append(avg.text)

#Extract strike rate 
strike_rate = driver.find_elements(By.XPATH, '//table/tbody/tr/td[10]')
for sr in strike_rate:
    SR.append(sr.text)

#extrect 100s 
hu = driver.find_elements(By.XPATH, '//table/tbody/tr/td[11]')
for hd in hu:
    hundreds.append(hd.text)

#extract 50s
t_fifties = driver.find_elements(By.XPATH, '//table/tbody/tr/td[12]')
for f in t_fifties:
    fifties.append(f.text)

#extract 4s
t_fours = driver.find_elements(By.XPATH, '//table/tbody/tr/td[13]')
for fo in t_fours:
    fours.append(fo.text)

#extract 6s
total_sixes = driver.find_elements(By.XPATH, '//table/tbody/tr/td[14]')
for s in total_sixes:
    sixes.append(s.text)

# Close the driver
driver.quit()

# Find the maximum length among all lists
max_len = max(len(bats), len(runs), len(total_matches), len(HS), len(avg_score),
              len(SR), len(hundreds), len(fifties), len(fours), len(sixes))

# Pad all lists with None to ensure they are the same length
def pad_list(lst, length):
    return lst + [None] * (length - len(lst))

bats = pad_list(bats, max_len)
runs = pad_list(runs, max_len)
total_matches = pad_list(total_matches, max_len)
HS = pad_list(HS, max_len)
avg_score = pad_list(avg_score, max_len)
SR = pad_list(SR, max_len)
hundreds = pad_list(hundreds, max_len)
fifties = pad_list(fifties, max_len)
fours = pad_list(fours, max_len)
sixes = pad_list(sixes, max_len)

# Convert data to a DataFrame
data = {
    'Batsman': bats,
    'Runs': runs,
    'Matches': total_matches,
    'Highest Score': HS,
    'Average': avg_score,
    'Strike Rate': SR,
    'Hundreds': hundreds,
    'Fifties': fifties,
    'Fours': fours,
    'Sixes': sixes
}
df = pd.DataFrame(data)

# Save DataFrame to CSV in VS Code
df.to_csv('IPL_Stats_2022.csv', index=False)
print(df)