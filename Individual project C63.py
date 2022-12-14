# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 13:22:49 2022

@author: Peng
"""

from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import pandas as pd
#getting data from true car website
#getting M4 data
carlist=[] #list to store all the car info

def getcars():
    page_url = "https://www.truecar.com/used-cars-for-sale/listings/mercedes-benz/c-class/location-revere-ma/?searchRadius=500&trimSlug[]=c-63-amg&trimSlug[]=c-63-s-amg"
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
        }
        carlist.append(car)
    return

#for x in range(1,3):
getcars()

df = pd.DataFrame(carlist)




#df.to_csv('C:/Users/lrnru/Desktop/Bentely/Bentley 2022 Fall/MA 705/individual project/718-cayman.csv', index=False, encoding='utf-8')
#df.to_csv('C:/Users/lrnru/Desktop/Bentely/Bentley 2022 Fall/MA 705/individual project/M4.csv', index=False, encoding='utf-8')  
#df.to_csv('C:/Users/lrnru/Desktop/Bentely/Bentley 2022 Fall/MA 705/individual project/Mercedes.csv', index=False, encoding='utf-8') 
#df.to_csv('C:/Users/lrnru/Desktop/Bentely/Bentley 2022 Fall/MA 705/individual project/porsche 911.csv', index=False, encoding='utf-8') 
#df.to_csv('C:/Users/lrnru/Desktop/Bentely/Bentley 2022 Fall/MA 705/individual project/mini-hardtop-4-door.csv', index=False, encoding='utf-8') 


 