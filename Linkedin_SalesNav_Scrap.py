from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
#from selenium.webdriver.common.keys import Keys
#from bs4 import BeautifulSoup
#import requests
import pandas as pd
import numpy as np
import os
os.chdir("C:/Users/Dell/Downloads/chromedriver_win32/")

driver = webdriver.Chrome("C:/Users/Dell/Downloads/chromedriver_win32/chromedriver")
driver.get('https://www.linkedin.com')

# driver.find_element_by_id('session_key')
username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='session_key']")))
username.clear()
username.send_keys('email here')#Insert your e-mail

password =  WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='session_password']")))
password.clear()
password.send_keys('password here')#Insert your password here

log_in_button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
log_in_button.click()

time.sleep(150)
#################################### INSERT URL ####################################

driver.get('https://www.linkedin.com/sales/search/people?companyIncluded=Nalys%3A1795380&companyTimeScope=CURRENT&doFetchHeroCard=false&geoIncluded=100565514&keywords=Java&logHistory=true&page=1&rsLogId=796873828&searchSessionId=2KtadMyDTh6HsrXXvjHlIQ%3D%3D')

####################################################################################
time.sleep(30)
links =[]
tab = []
number_page = 1
number_candidate = 1
path = "C:/Users/Dell/Desktop/Automation/Scraped_data"
while number_page < 2:
    time.sleep(50)
    height = 0
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    while height < driver.execute_script("return document.body.scrollHeight"):
        driver.execute_script("window.scrollTo(0, {});".format(height))
        height += 20
    names =  WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='session_key']")))
    for name in names:
        link = name.get_attribute('href')
        if 'https://www.linkedin.com/sales/people/' in link:
            if link not in links:
                links.append(link)


    number_page += 1
    next_button = driver.find_element_by_class_name("search-results__pagination-next-button")
    next_button.click()
    print(links)
    print(len(links))

for link in links:
    driver.get(link)
    time.sleep(1)
    try:
        name_contact = driver.find_element_by_xpath('/html/body/main/div[1]/div[2]/div/div[1]/div[1]/div/dl/dt/span').text

    except:
        name_contact = "élément manquant"

    try :
        location = driver.find_element_by_xpath('/html/body/main/div[1]/div[2]/div/div[1]/div[1]/div/dl/dd[3]/div[1]').text

    except:
        location = "élément manquant"

    try :
        position = driver.find_element_by_xpath('/html/body/main/div[1]/div[2]/div/div[1]/div[2]/dl/dd[1]/div/div/span/span[1]').text

    except:
        position = "élément manquant"

    try :
        company = driver.find_element_by_xpath('/html/body/main/div[1]/div[2]/div/div[1]/div[2]/dl/dd[1]/div/div/span/a').text
    except:
        try:
              company = driver.find_element_by_xpath('/html/body/main/div[1]/div[2]/div/div[1]/div[2]/dl/dd[1]/div/div[1]/span/span[2]').text
        except:
            company = "élément manquant"



    number_candidate += 1
    print("{} /".format(number_candidate) + " {}".format(len(links)))
    print("\n")
    print(name_contact)
    print(company)
    print(position)
    print(location)
    print("\n")
    print("\n")
    tab.append([name_contact, position, company, location,link])

df = pd.DataFrame(np.array(tab))
df.to_excel(r'{}/Linkedin_Scrap.xlsx'.format(path), index=False, header=True)












