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
from pathlib import Path

path = str(Path().absolute())
fullpath = path + str('/raw/btc.csv')

#.......................................................................
#Funciones definidas para escribir dentro del archivo

def add_newvalue(price,exchange):
    row_list =[]
    with open(fullpath, newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            row_list.append(row)   
    #Se agrega el nuevo valor de buda obtenido directamente desde la API
    b_date = today = date.today() #tomar el dia actual para generar los datos
    b_hour = dt.datetime.now().hour
    b_minute = dt.datetime.now().minute
    if b_minute < 10: b_minute = '0' + str(b_minute)
    #new_value =[b_date, price , b_hour, b_minute, exchange]
    b_hm  = str(b_hour) + ':'+ str(b_minute) + ':00'
    b_hm = str(b_date) + ' ' + str(b_hm)
    new_value =[b_date, price , b_hm , exchange]
    row_list.append(new_value)   
    with open(fullpath, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(row_list)
#.......................................................................

# <<<< Buda >>>>>>
buda_data = requests.get('https://www.buda.com/api/v2/markets/btc-clp/ticker').json()
buda_price = int(float(buda_data['ticker']['last_price'][0]))

add_newvalue(buda_price, 'buda' )  


#.......................................................................

# <<<< Bistamp >>>>>>

bitstamp_data = requests.get('https://www.bitstamp.net/api/v2/ticker/btcusd').json()
bitstamp_price_USD = float(bitstamp_data ['last'])
get_ind = requests.get('https://mindicador.cl/api').json()
price_USD = float(get_ind['dolar']['valor'])
bitstamp_price = int(price_USD*bitstamp_price_USD)

add_newvalue(bistamp_price, 'bistamp' )

#.......................................................................

# <<<< CoinDesk >>>>>>
cdesk_data = requests.get('https://api.coindesk.com/v1/bpi/currentprice/CLP.json').json()
cdesk_price = int(cdesk_data ['bpi']["CLP"]['rate_float'])

add_newvalue(cdesk_price, 'coindesk' )

#.......................................................................

# <<<< CryptoMkt >>>>>>
crypto_data = requests.get('https://api.cryptomkt.com/v1/ticker?market=BTCCLP').json()
crypto_price = crypto_data["data"][0]['last_price']
crypto_price = int(crypto_price)
add_newvalue(crypto_price, 'cryptomkt' )