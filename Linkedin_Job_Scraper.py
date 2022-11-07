# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 11:25:09 2022

@author: Chayma elbahri
"""

import csv
import requests
from bs4 import BeautifulSoup
import pandas

url = 'https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords=Product%20Management&amp;amp;amp;amp;location=San%20Francisco%20Bay%20Area&amp;amp;amp;amp;geoId=90000084&amp;amp;amp;amp;trk=public_jobs_jobs-search-bar_search-submit&amp;amp;amp;amp;position=1&amp;amp;amp;amp;pageNum=0&amp;amp;amp;amp;start=0'
response = requests.get(url)
print(response)
soup = BeautifulSoup(response.content,'html.parser')
job_title = soup.find('h3', class_='base-search-card__title').text

def linkedin_scraper(webpage, page_number):
    next_page = webpage + str(page_number)
    print(str(next_page))
    response = requests.get(str(next_page))
    soup = BeautifulSoup(response.content,'html.parser')
    jobs = soup.find_all('div', class_='base-card relative w-full hover:no-underline focus:no-underline base-card--link base-search-card base-search-card--link job-search-card')
    for job in jobs:
        job_title = job.find('h3', class_='base-search-card__title').text.strip()
        job_company = job.find('h4', class_='base-search-card__subtitle').text.strip()
        job_location = job.find('span', class_='job-search-card__location').text.strip()
        job_link = job.find('a', class_='base-card__full-link')['href']
        writer.writerow([job_title.encode('utf-8'),job_company.encode('utf-8'),job_location.encode('utf-8'),job_link.encode('utf-8')])
    else:
            file.close()
            print('File closed')	
        
file = open('linkedin-jobs.csv', 'a')
writer = csv.writer(file)
writer.writerow(['Title', 'Company', 'Location', 'Apply'])


                       
linkedin_scraper('https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords=Product%20Management&amp;amp;amp;amp;location=San%20Francisco%20Bay%20Area&amp;amp;amp;amp;geoId=90000084&amp;amp;amp;amp;trk=public_jobs_jobs-search-bar_search-submit&amp;amp;amp;amp;position=1&amp;amp;amp;amp;pageNum=0&amp;amp;amp;amp;start=', 0)


df = pandas.read_csv('linkedin-jobs.csv')
print(df)
      