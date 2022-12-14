# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 13:22:49 2022

@author: Peng
"""

from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import pandas as pd

carlist=[]
#below is 2015 to 2017 data
#page_url = 'https://www.truecar.com/used-cars-for-sale/listings/bmw/m4/year-2015-2017/location-revere-ma/?searchRadius=500'
#below is 2018 data
#page_url = "https://www.truecar.com/used-cars-for-sale/listings/bmw/m4/year-2018/location-revere-ma/?searchRadius=500"
#below is 2019 data
#page_url = "https://www.truecar.com/used-cars-for-sale/listings/bmw/m4/year-2019/location-revere-ma/?searchRadius=500"
#below is 2020 data
#page_url = "https://www.truecar.com/used-cars-for-sale/listings/bmw/m4/year-2020/location-revere-ma/?searchRadius=500"
# below is for 2021 and 2023 data
page_url = 'https://www.truecar.com/used-cars-for-sale/listings/bmw/m4/year-2021-2023/location-revere-ma/?searchRadius=500'
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
     'miles': item.find('div', {'data-test': 'vehicleMileage'}).text,
     'price': item.find('div', {'data-qa': 'Heading'}).text,
     'color': item.find('div',{'data-test': 'vehicleCardColors'}).text,
     }
     carlist.append(car)
    

df = pd.DataFrame(carlist)
# to save two files
#df.to_csv('C:/Users/lrnru/Desktop/Bentely/Bentley 2022 Fall/MA 705/individual project/BMW M4 2015-2017.csv', index=False, encoding='utf-8')  
#df.to_csv('C:/Users/lrnru/Desktop/Bentely/Bentley 2022 Fall/MA 705/individual project/BMW M4 2018.csv', index=False, encoding='utf-8')
#df.to_csv('C:/Users/lrnru/Desktop/Bentely/Bentley 2022 Fall/MA 705/individual project/BMW M4 2019.csv', index=False, encoding='utf-8')
#df.to_csv('C:/Users/lrnru/Desktop/Bentely/Bentley 2022 Fall/MA 705/individual project/BMW M4 2020.csv', index=False, encoding='utf-8')

#df.to_csv('C:/Users/lrnru/Desktop/Bentely/Bentley 2022 Fall/MA 705/individual project/BMW M4 2021-2023.csv', index=False, encoding='utf-8')