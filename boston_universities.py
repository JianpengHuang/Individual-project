"""
Dashboard created in lecture Week 10
"""


import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

url = 'https://raw.githubusercontent.com/JianpengHuang/Individual-project/main/Revised%20data.csv'

df = pd.read_csv(url)


stylesheet = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

### pandas dataframe to html table
def generate_table(dataframe, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])


app = dash.Dash(__name__, external_stylesheets = stylesheet)
server = app.server

fig = px.scatter(df, x = "year", y = "price", color="model")
fig.update_xaxes(range = [2014.5, 2023.5])


app.layout = html.Div([
    html.H1('TrueCar Used Sport Car Dashboard',          
            style = {'textAlign' : 'center', 'font-size' : 45})
 

if __name__ == '__main__':
   app.run_server(debug=True)
