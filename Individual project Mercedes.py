# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 14:19:59 2022

@author: Peng
"""

from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import pandas as pd

carlist=[]
#below is 2019~data
page_url = 'https://www.truecar.com/used-cars-for-sale/listings/mercedes-benz/c-class/year-2016-max/location-revere-ma/?searchRadius=500&trimSlug[]=amg-c-63&trimSlug[]=amg-c-63-s'
# below is for 2017 and 2018 data
#page_url = 'https://www.truecar.com/used-cars-for-sale/listings/mercedes-benz/c-class/year-2017-max/location-revere-ma/?searchRadius=500&trimSlug[]=c-63-amg&trimSlug[]=c-63-s-amg'
headers = {'User-Agent': 'Chrome'}
req = requests.get(page_url, headers = headers)
req.raise_for_status()
soup = BeautifulSoup(req.text, 'html.parser')  
  
cars = soup.find_all('li', {'class':'mt-3 flex grow col-md-6 col-xl-4'})

for item in cars:
     car = {
     'year': item.find('span', {'class': 'vehicle-card-year text-xs'}).text,
     'name': item.find('span', {'class':'truncate'}).text,
     'model': item.find('div', {'class': 'truncate text-xs'}).text,
     'miles': item.find('div',{'data-test': 'vehicleMileage'}).text,
     'price': item.find('div', {'data-test': 'vehicleCardPricingBlockPrice'}).text,
     'color': item.find('div',{'data-test': 'vehicleCardColors'}).text,
     }
     carlist.append(car)
    

df = pd.DataFrame(carlist)
# to save two files
#df.to_csv('C:/Users/lrnru/Desktop/Bentely/Bentley 2022 Fall/MA 705/individual project/Mercedes.csv', index=False, encoding='utf-8')  
df.to_csv('C:/Users/lrnru/Desktop/Bentely/Bentley 2022 Fall/MA 705/individual project/Mercedes1.csv', index=False, encoding='utf-8')