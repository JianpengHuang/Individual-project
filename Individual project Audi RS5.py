# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 23:08:57 2022

@author: Peng
"""


from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import pandas as pd

carlist=[]
#below is 2015 - 2018 data
#page_url =' https://www.truecar.com/used-cars-for-sale/listings/audi/rs-5/year-2015-2018/location-revere-ma/?searchRadius=5000'
#below is 2019 - 2020 data
#page_url = 'https://www.truecar.com/used-cars-for-sale/listings/audi/rs-5/year-2019-2020/location-revere-ma/?searchRadius=5000'
#below is 2021 - 2023 data
page_url = 'https://www.truecar.com/used-cars-for-sale/listings/audi/rs-5/year-2021-2023/location-revere-ma/?searchRadius=5000'
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
     'price': getattr(item.find('div', {'data-test': 'vehicleCardPricingBlockPrice'}),'text', None),
     'color': item.find('div',{'data-test': 'vehicleCardColors'}).text,
     }
     carlist.append(car)
    

df = pd.DataFrame(carlist)
# to save two files

#df.to_csv('C:/Users/lrnru/Desktop/Bentely/Bentley 2022 Fall/MA 705/individual project/Audi RS5 2015-2018.csv', index=False, encoding='utf-8')
#df.to_csv('C:/Users/lrnru/Desktop/Bentely/Bentley 2022 Fall/MA 705/individual project/Audi RS5 2019-2020.csv', index=False, encoding='utf-8')
df.to_csv('C:/Users/lrnru/Desktop/Bentely/Bentley 2022 Fall/MA 705/individual project/Audi RS5 2021-2023.csv', index=False, encoding='utf-8')