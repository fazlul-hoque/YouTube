

#Author: Md.Fazlul Hoque
#Source: Stackoverflow and answered by the author
#Source link: https://stackoverflow.com/questions/74606385/cant-get-href-from-selenium-webdriver-scraping-youtube/74606782#74606782
            
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import pandas as pd
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
#All are optional
#options.add_experimental_option("detach", True)
options.add_argument("--disable-extensions")
options.add_argument("--disable-notifications")
options.add_argument("--disable-Advertisement")
options.add_argument("--disable-popup-blocking")
options.add_argument("start-maximized")

s=Service('./chromedriver')
driver= webdriver.Chrome(service=s,options=options)

driver.get('https://www.youtube.com/user/theneedledrop/videos')
time.sleep(3)

item = []
SCROLL_PAUSE_TIME = 1
last_height = driver.execute_script("return document.documentElement.scrollHeight")

item_count = 100

while item_count > len(item):
    driver.execute_script("window.scrollTo(0,document.documentElement.scrollHeight);")
    time.sleep(SCROLL_PAUSE_TIME)
    new_height = driver.execute_script("return document.documentElement.scrollHeight")

    if new_height == last_height:
        break
    last_height = new_height
    

data = []
try:
    for e in WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div#details'))):
        vurl = e.find_element(By.CSS_SELECTOR,'a#video-title-link').get_attribute('href')
        data.append({
            'video_url':vurl,
            
            })
except:
    pass
    
item = data
#print(item)
#print(len(item))
df = pd.DataFrame(item).drop_duplicates()
#print(df.to_markdown())