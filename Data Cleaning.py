# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 11:12:24 2022

@author: Peng
"""

import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd



df = pd.read_csv('C:/Users/lrnru/Desktop/Bentely/Bentley 2022 Fall/MA 705/individual project/Master Data Sheet.csv')

new = df["color"].str.split(",", n =1 , expand = True)

df['exterior color'] = new[0]
df['interior color'] = new[1]

df.drop(columns = ["color"], inplace = True)

new1 = df["exterior color"].str.split(" ", n=1, expand = True)
df['exterior color'] = new1[0]

new2 = df["interior color"].str.split(" ", n=1, expand = True)
new2 = new2[1].str.split(" ", n=1, expand = True)
df['interior color'] = new2[0]

new3 = df['make'].str.split(" ", n=1, expand = True)
df['make'] = new3[0]
df['model'] = new3[1]

new4 = df['miles'].str.split(" ", n=1, expand = True)
df['miles'] = new4[0]
#altering the DataFrame
df = df[['year', 'make', 'model', 'body style', 'miles', 'price', 
         'exterior color', 'interior color']]

#df['body style'] = df['model'] + " " + df['body style']

df['price'] = df['price'].str.replace("$", '')
df['price'] = df['price'].str.replace(",", '')

df = df.sort_values('year')
#df.drop(columns = ["body style"], inplace = True)

df.to_csv('C:/Users/lrnru/Desktop/Bentely/Bentley 2022 Fall/MA 705/individual project/Revised data.csv', index=False, encoding='utf-8')


