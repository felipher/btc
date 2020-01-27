#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 12:40:10 2020

@author: hernanfernandezcarne
"""

import requests 
import pandas as pd
import json
import csv
from datetime import date
import datetime as dt


#.......................................................................
#Funciones definidas para la carga

def load_json(url):
    response = requests.get(url)
    a = response.json()
    b = json.dumps(a) #convert to JSON string
    data = pd.read_json(b)
    return data

def add_newvalue(price,exchange):
    row_list =[]
    with open('../raw/btc.csv', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            row_list.append(row)   
    #Se agrega el nuevo valor de buda obtenido directamente desde la API
    b_date = today = date.today() #tomar el dia actual para generar los datos
    b_hour = dt.datetime.now().hour
    b_minute = dt.datetime.now().minute
    new_value =[b_date, price , b_hour, b_minute, exchange]
    row_list.append(new_value)   
    with open('../raw/btc.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(row_list)
#.......................................................................

    
    data_buda = load_json('https://www.buda.com/api/v2/markets/btc-clp/ticker')
    buda_price = data_buda.loc["last_price" , :].to_string() 
    buda_price = int(buda_price[11:18])
    add_newvalue(buda_price, 'buda' )  
