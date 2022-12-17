import time
import math
import pandas as pd
import sys
import os
import threading
import re
import rsa
import string
import smtplib
import requests
import socket
import platform
from time import sleep
from tqdm import tqdm, trange
from Historic_Crypto import HistoricalData
from Historic_Crypto import LiveCryptoData
from binance import Client
from pygame import mixer
from decimal import Decimal
from colorama import Fore, Back, Style, init
from pymongo import MongoClient
from email.message import EmailMessage
from getmac import get_mac_address as gma
from random import *
init(autoreset=True)
init()

DEMO = Fore.GREEN+"[DEMO]"

print(Fore.LIGHTRED_EX+"""

       ____     ____     __   __  ____    _____   U  ___ u  
    U /"___| U |  _"\ u  \ \ / / U|  _"\ u|_ " _|   \/"_ \/              
    \| | u    \| |_) |/   \ V /  \| |_) |/  | |     | | | |              
     | |/__    |  _ <    U_|"|_u  |  __/   /| |\.-,_| |_| |            
      \____|   |_| \_\     |_|    |_|     u |_|U \_)-\___/            __          _      ______     ____  ____  ____  
     _// \ \   //   \ \_.-,//|(_  ||>>_   _// \ \_     \ \           /_/         | |    / ____/    / __ \/ __ \/ __ )
    (__) (__) (__)   (__)\_) (__)(__)__) (__)  (__)    (__)        /_/___________/ /   / /  ______/ /_/ / / / / __  |
                                                                 < </_____/_____/>_>  / /__/_____/ _, _/ /_/ / /_/ /
                                                                 / /     (_)  _/_/    \____/    /_/ |_|\____/_____/
                                                                 \_\         /_/                                                                      
        ____     U  ___ u   ____       __     __      _             
     U |  _"\ u   \/"_ \/U | __") u    \ \   /"/u    /"|          
      \| |_) |/   | | | | \|  _ \/      \ \ / //   u | |u       
       |  _ <.- ,_| |_| |  | |_) |      /\ V /_,-.  \| |/       
       |_| \_\ \_)-\___/   |____/      U  \_/-(_/_   |_|        
       //   \ \_    \ \    _|| \ \_        //     (")_//<,-, 
      (__)   (__)   (__)  (__)  (__)    (__)     "(__)(_/   """)

print(Fore.GREEN+"""                                                                                                                                                                                                                                                                                                                                                                                                                                        
  ______ ______ ______ ______ ______ ______ ______ ______ ______ ______ ______ ______ ______ ______ ______ 
 |______|______|______|______|______|______|______|______|______|______|______|______|______|______|______|                                                                                                                                                                                                                                                                                                                                                                                                              
""")

#-------------------------------------------------------W


secret = ""
apı = ""
ROB = Client(apı,secret)


times = time.gmtime()
years = times[0]
month = times[1]
days = times[2]

ocak_max = 31
subat_max = 28
mart_max = 31
nisan_max = 30
mayıs_max = 31
haziran_max = 30
temmuz_max = 31
agustos_max = 31
eylul_max = 30
ekim_max = 31
kasım_max = 30
aralık_max = 31


btc_open = ""
btc_low = ""

solona_open = ""
solona_close = ""

etherneum_open = ""
etherneum_close = ""

dogecoin_open = ""
dogecoin_close = ""

avalance_open = ""
avalance_close = ""

enjin_open = ""
enjin_close = ""

mana_open = ""
mana_close = ""

ada_open = ""
ada_close = ""

dot_open = ""
dot_close = ""

lınk_open = ""
lınk_close = ""

ltc_open = ""
ltc_close = ""

uni_open = ""
uni_close = ""

etc_open = ""
etc_close = ""

one_week_days = days - 7
two_week_days = one_week_days - 7

def Listele_Day15():
    global etc_open, etc_close, uni_open, uni_close, avalance_close, avalance_open, dogecoin_close, dogecoin_open, etherneum_close, etherneum_open, solona_open, solona_close, btc_open, btc_close, enjin_open, enjin_close, mana_open, mana_close, ada_open, ada_close, dot_open, dot_close, lınk_open, lınk_close, ltc_open, ltc_close
    btc = HistoricalData('BTC-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, two_week_days, "00", "00")),verbose=False).retrieve_data()
    doge = HistoricalData('DOGE-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, two_week_days, "00", "00")),verbose=False).retrieve_data()
    sol = HistoricalData('SOL-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, two_week_days, "00", "00")),verbose=False).retrieve_data()
    avax = HistoricalData('AVAX-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, two_week_days, "00", "00")),verbose=False).retrieve_data()
    eth = HistoricalData('ETH-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, two_week_days, "00", "00")),verbose=False).retrieve_data()
    enj = HistoricalData('ENJ-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, two_week_days, "00", "00")),verbose=False).retrieve_data()
    mana = HistoricalData('MANA-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, two_week_days, "00", "00")),verbose=False).retrieve_data()
    ada = HistoricalData('ADA-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, two_week_days, "00", "00")),verbose=False).retrieve_data()
    dot = HistoricalData('DOT-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, two_week_days, "00", "00")),verbose=False).retrieve_data()
    lınk = HistoricalData('LINK-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, two_week_days, "00", "00")),verbose=False).retrieve_data()
    ltc = HistoricalData('LTC-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, two_week_days, "00", "00")),verbose=False).retrieve_data()
    uni = HistoricalData('UNI-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, two_week_days, "00", "00")),verbose=False).retrieve_data()
    etc = HistoricalData('ETC-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, two_week_days, "00", "00")),verbose=False).retrieve_data()
    lınk_open = lınk['open']
    lınk_close = lınk['close']

    ada_open = ada['open']
    ada_close = ada['close']

    mana_open = mana['open']
    mana_close = mana['close']

    enjin_open = enj['open']
    enjin_close = enj['close']

    btc_open = btc['open']
    btc_close = btc['close']

    dogecoin_open = doge['open']
    dogecoin_close = doge['close']

    avalance_close = avax['close']
    avalance_open = avax['open']

    dot_open = dot['open']
    dot_close = dot['close']

    etherneum_close = eth['close']
    etherneum_open = eth['open']

    solona_open = sol['open']
    solona_close = sol['close']

    ltc_open = ltc['open']
    ltc_close = ltc['close']

    uni_open = uni['open']
    uni_close = uni['close']

    etc_open = etc['open']
    etc_close = etc['close']
def Listele_Day7_Subat():
    global etc_open, etc_close, uni_open, uni_close, avalance_close, avalance_open, dogecoin_close, dogecoin_open, etherneum_close, etherneum_open, solona_open, solona_close, btc_open, btc_close, enjin_open, enjin_close, mana_open, mana_close, ada_open, ada_close, dot_open, dot_close, lınk_open, lınk_close, ltc_open, ltc_close
    btc = HistoricalData('BTC-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_subat, "00", "00")),verbose=False).retrieve_data()
    doge = HistoricalData('DOGE-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_subat, "00", "00")),verbose=False).retrieve_data()
    sol = HistoricalData('SOL-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_subat, "00", "00")),verbose=False).retrieve_data()
    avax = HistoricalData('AVAX-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_subat, "00", "00")),verbose=False).retrieve_data()
    eth = HistoricalData('ETH-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_subat, "00", "00")),verbose=False).retrieve_data()
    enj = HistoricalData('ENJ-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_subat, "00", "00")),verbose=False).retrieve_data()
    mana = HistoricalData('MANA-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_subat, "00", "00")),verbose=False).retrieve_data()
    ada = HistoricalData('ADA-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_subat, "00", "00")),verbose=False).retrieve_data()
    dot = HistoricalData('DOT-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_subat, "00", "00")),verbose=False).retrieve_data()
    lınk = HistoricalData('LINK-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_subat, "00", "00")),verbose=False).retrieve_data()
    ltc = HistoricalData('LTC-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_subat, "00", "00")),verbose=False).retrieve_data()
    uni = HistoricalData('UNI-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_subat, "00", "00")),verbose=False).retrieve_data()
    etc = HistoricalData('ETC-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_subat, "00", "00")),verbose=False).retrieve_data()

    lınk_open = lınk['open']
    lınk_close = lınk['close']

    ada_open = ada['open']
    ada_close = ada['close']

    mana_open = mana['open']
    mana_close = mana['close']

    enjin_open = enj['open']
    enjin_close = enj['close']

    btc_open = btc['open']
    btc_close = btc['close']

    dogecoin_open = doge['open']
    dogecoin_close = doge['close']

    avalance_close = avax['close']
    avalance_open = avax['open']

    dot_open = dot['open']
    dot_close = dot['close']

    etherneum_close = eth['close']
    etherneum_open = eth['open']

    solona_open = sol['open']
    solona_close = sol['close']

    ltc_open = ltc['open']
    ltc_close = ltc['close']

    uni_open = uni['open']
    uni_close = uni['close']

    etc_open = etc['open']
    etc_close = etc['close']
def Listele_Day7_Mart():
    global etc_open, etc_close, uni_open, uni_close, avalance_close, avalance_open, dogecoin_close, dogecoin_open, etherneum_close, etherneum_open, solona_open, solona_close, btc_open, btc_close, enjin_open, enjin_close, mana_open, mana_close, ada_open, ada_close, dot_open, dot_close, lınk_open, lınk_close, ltc_open, ltc_close
    btc = HistoricalData('BTC-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_mart, "00", "00")),verbose=False).retrieve_data()
    doge = HistoricalData('DOGE-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_mart, "00", "00")),verbose=False).retrieve_data()
    sol = HistoricalData('SOL-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_mart, "00", "00")),verbose=False).retrieve_data()
    avax = HistoricalData('AVAX-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_mart, "00", "00")),verbose=False).retrieve_data()
    eth = HistoricalData('ETH-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_mart, "00", "00")),verbose=False).retrieve_data()
    enj = HistoricalData('ENJ-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_mart, "00", "00")),verbose=False).retrieve_data()
    mana = HistoricalData('MANA-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_mart, "00", "00")),verbose=False).retrieve_data()
    ada = HistoricalData('ADA-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_mart, "00", "00")),verbose=False).retrieve_data()
    dot = HistoricalData('DOT-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_mart, "00", "00")),verbose=False).retrieve_data()
    lınk = HistoricalData('LINK-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_mart, "00", "00")),verbose=False).retrieve_data()
    ltc = HistoricalData('LTC-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_mart, "00", "00")),verbose=False).retrieve_data()
    uni = HistoricalData('UNI-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_mart, "00", "00")),verbose=False).retrieve_data()
    etc = HistoricalData('ETC-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_mart, "00", "00")),verbose=False).retrieve_data()

    lınk_open = lınk['open']
    lınk_close = lınk['close']

    ada_open = ada['open']
    ada_close = ada['close']

    mana_open = mana['open']
    mana_close = mana['close']

    enjin_open = enj['open']
    enjin_close = enj['close']

    btc_open = btc['open']
    btc_close = btc['close']

    dogecoin_open = doge['open']
    dogecoin_close = doge['close']

    avalance_close = avax['close']
    avalance_open = avax['open']

    dot_open = dot['open']
    dot_close = dot['close']

    etherneum_close = eth['close']
    etherneum_open = eth['open']

    solona_open = sol['open']
    solona_close = sol['close']

    ltc_open = ltc['open']
    ltc_close = ltc['close']

    uni_open = uni['open']
    uni_close = uni['close']

    etc_open = etc['open']
    etc_close = etc['close']
def Listele_Day7_Nisan():
    global etc_open, etc_close, uni_open, uni_close, avalance_close, avalance_open, dogecoin_close, dogecoin_open, etherneum_close, etherneum_open, solona_open, solona_close, btc_open, btc_close, enjin_open, enjin_close, mana_open, mana_close, ada_open, ada_close, dot_open, dot_close, lınk_open, lınk_close, ltc_open, ltc_close
    btc = HistoricalData('BTC-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_nisan, "00", "00")),verbose=False).retrieve_data()
    doge = HistoricalData('DOGE-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_nisan, "00", "00")),verbose=False).retrieve_data()
    sol = HistoricalData('SOL-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_nisan, "00", "00")),verbose=False).retrieve_data()
    avax = HistoricalData('AVAX-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_nisan, "00", "00")),verbose=False).retrieve_data()
    eth = HistoricalData('ETH-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_nisan, "00", "00")),verbose=False).retrieve_data()
    enj = HistoricalData('ENJ-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_nisan, "00", "00")),verbose=False).retrieve_data()
    mana = HistoricalData('MANA-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_nisan, "00", "00")),verbose=False).retrieve_data()
    ada = HistoricalData('ADA-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_nisan, "00", "00")),verbose=False).retrieve_data()
    dot = HistoricalData('DOT-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_nisan, "00", "00")),verbose=False).retrieve_data()
    lınk = HistoricalData('LINK-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_nisan, "00", "00")),verbose=False).retrieve_data()
    ltc = HistoricalData('LTC-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_nisan, "00", "00")),verbose=False).retrieve_data()
    uni = HistoricalData('UNI-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_nisan, "00", "00")),verbose=False).retrieve_data()
    etc = HistoricalData('ETC-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_nisan, "00", "00")),verbose=False).retrieve_data()

    lınk_open = lınk['open']
    lınk_close = lınk['close']

    ada_open = ada['open']
    ada_close = ada['close']

    mana_open = mana['open']
    mana_close = mana['close']

    enjin_open = enj['open']
    enjin_close = enj['close']

    btc_open = btc['open']
    btc_close = btc['close']

    dogecoin_open = doge['open']
    dogecoin_close = doge['close']

    avalance_close = avax['close']
    avalance_open = avax['open']

    dot_open = dot['open']
    dot_close = dot['close']

    etherneum_close = eth['close']
    etherneum_open = eth['open']

    solona_open = sol['open']
    solona_close = sol['close']

    ltc_open = ltc['open']
    ltc_close = ltc['close']

    uni_open = uni['open']
    uni_close = uni['close']

    etc_open = etc['open']
    etc_close = etc['close']
def Listele_Day7_Mayıs():
    global etc_open, etc_close, uni_open, uni_close, avalance_close, avalance_open, dogecoin_close, dogecoin_open, etherneum_close, etherneum_open, solona_open, solona_close, btc_open, btc_close, enjin_open, enjin_close, mana_open, mana_close, ada_open, ada_close, dot_open, dot_close, lınk_open, lınk_close, ltc_open, ltc_close
    btc = HistoricalData('BTC-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_mayıs, "00", "00")),verbose=False).retrieve_data()
    doge = HistoricalData('DOGE-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_mayıs, "00", "00")),verbose=False).retrieve_data()
    sol = HistoricalData('SOL-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_mayıs, "00", "00")),verbose=False).retrieve_data()
    avax = HistoricalData('AVAX-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_mayıs, "00", "00")),verbose=False).retrieve_data()
    eth = HistoricalData('ETH-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_mayıs, "00", "00")),verbose=False).retrieve_data()
    enj = HistoricalData('ENJ-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_mayıs, "00", "00")),verbose=False).retrieve_data()
    mana = HistoricalData('MANA-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_mayıs, "00", "00")),verbose=False).retrieve_data()
    ada = HistoricalData('ADA-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_mayıs, "00", "00")),verbose=False).retrieve_data()
    dot = HistoricalData('DOT-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_mayıs, "00", "00")),verbose=False).retrieve_data()
    lınk = HistoricalData('LINK-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_mayıs, "00", "00")),verbose=False).retrieve_data()
    ltc = HistoricalData('LTC-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_mayıs, "00", "00")),verbose=False).retrieve_data()
    uni = HistoricalData('UNI-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_mayıs, "00", "00")),verbose=False).retrieve_data()
    etc = HistoricalData('ETC-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_mayıs, "00", "00")),verbose=False).retrieve_data()

    lınk_open = lınk['open']
    lınk_close = lınk['close']

    ada_open = ada['open']
    ada_close = ada['close']

    mana_open = mana['open']
    mana_close = mana['close']

    enjin_open = enj['open']
    enjin_close = enj['close']

    btc_open = btc['open']
    btc_close = btc['close']

    dogecoin_open = doge['open']
    dogecoin_close = doge['close']

    avalance_close = avax['close']
    avalance_open = avax['open']

    dot_open = dot['open']
    dot_close = dot['close']

    etherneum_close = eth['close']
    etherneum_open = eth['open']

    solona_open = sol['open']
    solona_close = sol['close']

    ltc_open = ltc['open']
    ltc_close = ltc['close']

    uni_open = uni['open']
    uni_close = uni['close']

    etc_open = etc['open']
    etc_close = etc['close']
def Listele_Day7_Haziran():
    global etc_open, etc_close, uni_open, uni_close, avalance_close, avalance_open, dogecoin_close, dogecoin_open, etherneum_close, etherneum_open, solona_open, solona_close, btc_open, btc_close, enjin_open, enjin_close, mana_open, mana_close, ada_open, ada_close, dot_open, dot_close, lınk_open, lınk_close, ltc_open, ltc_close
    btc = HistoricalData('BTC-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_haziran, "00", "00")),verbose=False).retrieve_data()
    doge = HistoricalData('DOGE-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_haziran, "00", "00")),verbose=False).retrieve_data()
    sol = HistoricalData('SOL-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_haziran, "00", "00")),verbose=False).retrieve_data()
    avax = HistoricalData('AVAX-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_haziran, "00", "00")),verbose=False).retrieve_data()
    eth = HistoricalData('ETH-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_haziran, "00", "00")),verbose=False).retrieve_data()
    enj = HistoricalData('ENJ-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_haziran, "00", "00")),verbose=False).retrieve_data()
    mana = HistoricalData('MANA-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_haziran, "00", "00")),verbose=False).retrieve_data()
    ada = HistoricalData('ADA-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_haziran, "00", "00")),verbose=False).retrieve_data()
    dot = HistoricalData('DOT-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_haziran, "00", "00")),verbose=False).retrieve_data()
    lınk = HistoricalData('LINK-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_haziran, "00", "00")),verbose=False).retrieve_data()
    ltc = HistoricalData('LTC-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_haziran, "00", "00")),verbose=False).retrieve_data()
    uni = HistoricalData('UNI-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_haziran, "00", "00")),verbose=False).retrieve_data()
    etc = HistoricalData('ETC-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_haziran, "00", "00")),verbose=False).retrieve_data()

    lınk_open = lınk['open']
    lınk_close = lınk['close']

    ada_open = ada['open']
    ada_close = ada['close']

    mana_open = mana['open']
    mana_close = mana['close']

    enjin_open = enj['open']
    enjin_close = enj['close']

    btc_open = btc['open']
    btc_close = btc['close']

    dogecoin_open = doge['open']
    dogecoin_close = doge['close']

    avalance_close = avax['close']
    avalance_open = avax['open']

    dot_open = dot['open']
    dot_close = dot['close']

    etherneum_close = eth['close']
    etherneum_open = eth['open']

    solona_open = sol['open']
    solona_close = sol['close']

    ltc_open = ltc['open']
    ltc_close = ltc['close']

    uni_open = uni['open']
    uni_close = uni['close']

    etc_open = etc['open']
    etc_close = etc['close']
def Listele_Day7_Temmuz():
    global etc_open, etc_close, uni_open, uni_close, avalance_close, avalance_open, dogecoin_close, dogecoin_open, etherneum_close, etherneum_open, solona_open, solona_close, btc_open, btc_close, enjin_open, enjin_close, mana_open, mana_close, ada_open, ada_close, dot_open, dot_close, lınk_open, lınk_close, ltc_open, ltc_close
    btc = HistoricalData('BTC-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_temmuz, "00", "00")),verbose=False).retrieve_data()
    doge = HistoricalData('DOGE-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_temmuz, "00", "00")),verbose=False).retrieve_data()
    sol = HistoricalData('SOL-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_temmuz, "00", "00")),verbose=False).retrieve_data()
    avax = HistoricalData('AVAX-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_temmuz, "00", "00")),verbose=False).retrieve_data()
    eth = HistoricalData('ETH-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_temmuz, "00", "00")),verbose=False).retrieve_data()
    enj = HistoricalData('ENJ-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_temmuz, "00", "00")),verbose=False).retrieve_data()
    mana = HistoricalData('MANA-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_temmuz, "00", "00")),verbose=False).retrieve_data()
    ada = HistoricalData('ADA-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_temmuz, "00", "00")),verbose=False).retrieve_data()
    dot = HistoricalData('DOT-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_temmuz, "00", "00")),verbose=False).retrieve_data()
    lınk = HistoricalData('LINK-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_temmuz, "00", "00")),verbose=False).retrieve_data()
    ltc = HistoricalData('LTC-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_temmuz, "00", "00")),verbose=False).retrieve_data()
    uni = HistoricalData('UNI-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_temmuz, "00", "00")),verbose=False).retrieve_data()
    etc = HistoricalData('ETC-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_temmuz, "00", "00")),verbose=False).retrieve_data()

    lınk_open = lınk['open']
    lınk_close = lınk['close']

    ada_open = ada['open']
    ada_close = ada['close']

    mana_open = mana['open']
    mana_close = mana['close']

    enjin_open = enj['open']
    enjin_close = enj['close']

    btc_open = btc['open']
    btc_close = btc['close']

    dogecoin_open = doge['open']
    dogecoin_close = doge['close']

    avalance_close = avax['close']
    avalance_open = avax['open']

    dot_open = dot['open']
    dot_close = dot['close']

    etherneum_close = eth['close']
    etherneum_open = eth['open']

    solona_open = sol['open']
    solona_close = sol['close']

    ltc_open = ltc['open']
    ltc_close = ltc['close']

    uni_open = uni['open']
    uni_close = uni['close']

    etc_open = etc['open']
    etc_close = etc['close']
def Listele_Day7_Agustos():
    global etc_open, etc_close, uni_open, uni_close, avalance_close, avalance_open, dogecoin_close, dogecoin_open, etherneum_close, etherneum_open, solona_open, solona_close, btc_open, btc_close, enjin_open, enjin_close, mana_open, mana_close, ada_open, ada_close, dot_open, dot_close, lınk_open, lınk_close, ltc_open, ltc_close
    btc = HistoricalData('BTC-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_agustos, "00", "00")),verbose=False).retrieve_data()
    doge = HistoricalData('DOGE-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_agustos, "00", "00")),verbose=False).retrieve_data()
    sol = HistoricalData('SOL-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_agustos, "00", "00")),verbose=False).retrieve_data()
    avax = HistoricalData('AVAX-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_agustos, "00", "00")),verbose=False).retrieve_data()
    eth = HistoricalData('ETH-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_agustos, "00", "00")),verbose=False).retrieve_data()
    enj = HistoricalData('ENJ-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_agustos, "00", "00")),verbose=False).retrieve_data()
    mana = HistoricalData('MANA-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_agustos, "00", "00")),verbose=False).retrieve_data()
    ada = HistoricalData('ADA-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_agustos, "00", "00")),verbose=False).retrieve_data()
    dot = HistoricalData('DOT-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_agustos, "00", "00")),verbose=False).retrieve_data()
    lınk = HistoricalData('LINK-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_agustos, "00", "00")),verbose=False).retrieve_data()
    ltc = HistoricalData('LTC-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_agustos, "00", "00")),verbose=False).retrieve_data()
    uni = HistoricalData('UNI-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_agustos, "00", "00")),verbose=False).retrieve_data()
    etc = HistoricalData('ETC-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_agustos, "00", "00")),verbose=False).retrieve_data()

    lınk_open = lınk['open']
    lınk_close = lınk['close']

    ada_open = ada['open']
    ada_close = ada['close']

    mana_open = mana['open']
    mana_close = mana['close']

    enjin_open = enj['open']
    enjin_close = enj['close']

    btc_open = btc['open']
    btc_close = btc['close']

    dogecoin_open = doge['open']
    dogecoin_close = doge['close']

    avalance_close = avax['close']
    avalance_open = avax['open']

    dot_open = dot['open']
    dot_close = dot['close']

    etherneum_close = eth['close']
    etherneum_open = eth['open']

    solona_open = sol['open']
    solona_close = sol['close']

    ltc_open = ltc['open']
    ltc_close = ltc['close']

    uni_open = uni['open']
    uni_close = uni['close']

    etc_open = etc['open']
    etc_close = etc['close']
def Listele_Day7_Eylül():
    global etc_open, etc_close, uni_open, uni_close, avalance_close, avalance_open, dogecoin_close, dogecoin_open, etherneum_close, etherneum_open, solona_open, solona_close, btc_open, btc_close, enjin_open, enjin_close, mana_open, mana_close, ada_open, ada_close, dot_open, dot_close, lınk_open, lınk_close, ltc_open, ltc_close
    btc = HistoricalData('BTC-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_eylül, "00", "00")),verbose=False).retrieve_data()
    doge = HistoricalData('DOGE-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_eylül, "00", "00")),verbose=False).retrieve_data()
    sol = HistoricalData('SOL-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_eylül, "00", "00")),verbose=False).retrieve_data()
    avax = HistoricalData('AVAX-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_eylül, "00", "00")),verbose=False).retrieve_data()
    eth = HistoricalData('ETH-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_eylül, "00", "00")),verbose=False).retrieve_data()
    enj = HistoricalData('ENJ-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_eylül, "00", "00")),verbose=False).retrieve_data()
    mana = HistoricalData('MANA-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_eylül, "00", "00")),verbose=False).retrieve_data()
    ada = HistoricalData('ADA-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_eylül, "00", "00")),verbose=False).retrieve_data()
    dot = HistoricalData('DOT-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_eylül, "00", "00")),verbose=False).retrieve_data()
    lınk = HistoricalData('LINK-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_eylül, "00", "00")),verbose=False).retrieve_data()
    ltc = HistoricalData('LTC-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_eylül, "00", "00")),verbose=False).retrieve_data()
    uni = HistoricalData('UNI-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_eylül, "00", "00")),verbose=False).retrieve_data()
    etc = HistoricalData('ETC-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_eylül, "00", "00")),verbose=False).retrieve_data()

    lınk_open = lınk['open']
    lınk_close = lınk['close']

    ada_open = ada['open']
    ada_close = ada['close']

    mana_open = mana['open']
    mana_close = mana['close']

    enjin_open = enj['open']
    enjin_close = enj['close']

    btc_open = btc['open']
    btc_close = btc['close']

    dogecoin_open = doge['open']
    dogecoin_close = doge['close']

    avalance_close = avax['close']
    avalance_open = avax['open']

    dot_open = dot['open']
    dot_close = dot['close']

    etherneum_close = eth['close']
    etherneum_open = eth['open']

    solona_open = sol['open']
    solona_close = sol['close']

    ltc_open = ltc['open']
    ltc_close = ltc['close']

    uni_open = uni['open']
    uni_close = uni['close']

    etc_open = etc['open']
    etc_close = etc['close']
def Listele_Day7_Ekim():
    global etc_open, etc_close, uni_open, uni_close, avalance_close, avalance_open, dogecoin_close, dogecoin_open, etherneum_close, etherneum_open, solona_open, solona_close, btc_open, btc_close, enjin_open, enjin_close, mana_open, mana_close, ada_open, ada_close, dot_open, dot_close, lınk_open, lınk_close, ltc_open, ltc_close
    btc = HistoricalData('BTC-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_ekim, "00", "00")),verbose=False).retrieve_data()
    doge = HistoricalData('DOGE-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_ekim, "00", "00")),verbose=False).retrieve_data()
    sol = HistoricalData('SOL-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_ekim, "00", "00")),verbose=False).retrieve_data()
    avax = HistoricalData('AVAX-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_ekim, "00", "00")),verbose=False).retrieve_data()
    eth = HistoricalData('ETH-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_ekim, "00", "00")),verbose=False).retrieve_data()
    enj = HistoricalData('ENJ-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_ekim, "00", "00")),verbose=False).retrieve_data()
    mana = HistoricalData('MANA-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_ekim, "00", "00")),verbose=False).retrieve_data()
    ada = HistoricalData('ADA-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_ekim, "00", "00")),verbose=False).retrieve_data()
    dot = HistoricalData('DOT-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_ekim, "00", "00")),verbose=False).retrieve_data()
    lınk = HistoricalData('LINK-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_ekim, "00", "00")),verbose=False).retrieve_data()
    ltc = HistoricalData('LTC-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_ekim, "00", "00")),verbose=False).retrieve_data()
    uni = HistoricalData('UNI-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_ekim, "00", "00")),verbose=False).retrieve_data()
    etc = HistoricalData('ETC-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_ekim, "00", "00")),verbose=False).retrieve_data()

    lınk_open = lınk['open']
    lınk_close = lınk['close']

    ada_open = ada['open']
    ada_close = ada['close']

    mana_open = mana['open']
    mana_close = mana['close']

    enjin_open = enj['open']
    enjin_close = enj['close']

    btc_open = btc['open']
    btc_close = btc['close']

    dogecoin_open = doge['open']
    dogecoin_close = doge['close']

    avalance_close = avax['close']
    avalance_open = avax['open']

    dot_open = dot['open']
    dot_close = dot['close']

    etherneum_close = eth['close']
    etherneum_open = eth['open']

    solona_open = sol['open']
    solona_close = sol['close']

    ltc_open = ltc['open']
    ltc_close = ltc['close']

    uni_open = uni['open']
    uni_close = uni['close']

    etc_open = etc['open']
    etc_close = etc['close']
def Listele_Day7_Kasım():
    global etc_open, etc_close, uni_open, uni_close, avalance_close, avalance_open, dogecoin_close, dogecoin_open, etherneum_close, etherneum_open, solona_open, solona_close, btc_open, btc_close, enjin_open, enjin_close, mana_open, mana_close, ada_open, ada_close, dot_open, dot_close, lınk_open, lınk_close, ltc_open, ltc_close
    btc = HistoricalData('BTC-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_kasım, "00", "00")),verbose=False).retrieve_data()
    doge = HistoricalData('DOGE-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_kasım, "00", "00")),verbose=False).retrieve_data()
    sol = HistoricalData('SOL-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_kasım, "00", "00")),verbose=False).retrieve_data()
    avax = HistoricalData('AVAX-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_kasım, "00", "00")),verbose=False).retrieve_data()
    eth = HistoricalData('ETH-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_kasım, "00", "00")),verbose=False).retrieve_data()
    enj = HistoricalData('ENJ-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_kasım, "00", "00")),verbose=False).retrieve_data()
    mana = HistoricalData('MANA-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_kasım, "00", "00")),verbose=False).retrieve_data()
    ada = HistoricalData('ADA-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_kasım, "00", "00")),verbose=False).retrieve_data()
    dot = HistoricalData('DOT-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_kasım, "00", "00")),verbose=False).retrieve_data()
    lınk = HistoricalData('LINK-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_kasım, "00", "00")),verbose=False).retrieve_data()
    ltc = HistoricalData('LTC-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_kasım, "00", "00")),verbose=False).retrieve_data()
    uni = HistoricalData('UNI-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_kasım, "00", "00")),verbose=False).retrieve_data()
    etc = HistoricalData('ETC-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_kasım, "00", "00")),verbose=False).retrieve_data()

    lınk_open = lınk['open']
    lınk_close = lınk['close']

    ada_open = ada['open']
    ada_close = ada['close']

    mana_open = mana['open']
    mana_close = mana['close']

    enjin_open = enj['open']
    enjin_close = enj['close']

    btc_open = btc['open']
    btc_close = btc['close']

    dogecoin_open = doge['open']
    dogecoin_close = doge['close']

    avalance_close = avax['close']
    avalance_open = avax['open']

    dot_open = dot['open']
    dot_close = dot['close']

    etherneum_close = eth['close']
    etherneum_open = eth['open']

    solona_open = sol['open']
    solona_close = sol['close']

    ltc_open = ltc['open']
    ltc_close = ltc['close']

    uni_open = uni['open']
    uni_close = uni['close']

    etc_open = etc['open']
    etc_close = etc['close']
def Listele_Day7_Aralık():
    global etc_open, etc_close, uni_open, uni_close, avalance_close, avalance_open, dogecoin_close, dogecoin_open, etherneum_close, etherneum_open, solona_open, solona_close, btc_open, btc_close, enjin_open, enjin_close, mana_open, mana_close, ada_open, ada_close, dot_open, dot_close, lınk_open, lınk_close, ltc_open, ltc_close
    btc = HistoricalData('BTC-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_aralık, "00", "00")),verbose=False).retrieve_data()
    doge = HistoricalData('DOGE-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_aralık, "00", "00")),verbose=False).retrieve_data()
    sol = HistoricalData('SOL-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_aralık, "00", "00")),verbose=False).retrieve_data()
    avax = HistoricalData('AVAX-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_aralık, "00", "00")),verbose=False).retrieve_data()
    eth = HistoricalData('ETH-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_aralık, "00", "00")),verbose=False).retrieve_data()
    enj = HistoricalData('ENJ-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_aralık, "00", "00")),verbose=False).retrieve_data()
    mana = HistoricalData('MANA-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_aralık, "00", "00")),verbose=False).retrieve_data()
    ada = HistoricalData('ADA-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_aralık, "00", "00")),verbose=False).retrieve_data()
    dot = HistoricalData('DOT-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_aralık, "00", "00")),verbose=False).retrieve_data()
    lınk = HistoricalData('LINK-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_aralık, "00", "00")),verbose=False).retrieve_data()
    ltc = HistoricalData('LTC-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_aralık, "00", "00")),verbose=False).retrieve_data()
    uni = HistoricalData('UNI-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_aralık, "00", "00")),verbose=False).retrieve_data()
    etc = HistoricalData('ETC-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, gecici_day_aralık, "00", "00")),verbose=False).retrieve_data()

    lınk_open = lınk['open']
    lınk_close = lınk['close']

    ada_open = ada['open']
    ada_close = ada['close']

    mana_open = mana['open']
    mana_close = mana['close']

    enjin_open = enj['open']
    enjin_close = enj['close']

    btc_open = btc['open']
    btc_close = btc['close']

    dogecoin_open = doge['open']
    dogecoin_close = doge['close']

    avalance_close = avax['close']
    avalance_open = avax['open']

    dot_open = dot['open']
    dot_close = dot['close']

    etherneum_close = eth['close']
    etherneum_open = eth['open']

    solona_open = sol['open']
    solona_close = sol['close']

    ltc_open = ltc['open']
    ltc_close = ltc['close']

    uni_open = uni['open']
    uni_close = uni['close']

    etc_open = etc['open']
    etc_close = etc['close']

if days >= 15:
    Listele_Day15()
elif (days <= 7 or days >= 7) and month == 1:
    month = 12
    years -= 1
    gecici_day_aralık = aralık_max
    if days == 14:
        month += 1
        gecici_day_aralık = 1
        Listele_Day7_Aralık()
    elif days == 13:
        gecici_day_aralık = 31
        Listele_Day7_Aralık()
    elif days == 12:
        gecici_day_aralık = 30
        Listele_Day7_Aralık()
    elif days == 11:
        gecici_day_aralık = 29
        Listele_Day7_Aralık()
    elif days == 10:
        gecici_day_aralık = 28
        Listele_Day7_Aralık()
    elif days == 9:
        gecici_day_aralık = 27
        Listele_Day7_Aralık()
    elif days == 8:
        gecici_day_aralık = 26
        Listele_Day7_Aralık()
    elif days == 7:
        gecici_day_aralık = 25
        Listele_Day7_Aralık()
    elif days == 6:
        gecici_day_aralık = 24
        Listele_Day7_Aralık()
    elif days == 5:
        gecici_day_aralık = 23
        Listele_Day7_Aralık()
    elif days == 4:
        gecici_day_aralık = 22
        Listele_Day7_Aralık()
    elif days == 3:
        gecici_day_aralık = 21
        Listele_Day7_Aralık()
    elif days == 2:
        gecici_day_aralık = 20
        Listele_Day7_Aralık()
    elif days == 1:
        gecici_day_aralık = 19
        Listele_Day7_Aralık()
elif (days <= 7 or days >= 7) and month == 2:
    month -= 1
    gecici_day_ocak = ocak_max
    if days == 14:
        month += 1
        gecici_day_ocak = 1
        Listele_Day7_Ocak()
    elif days == 13:
        gecici_day_ocak = 31
        Listele_Day7_Ocak()
    elif days == 12:
        gecici_day_ocak = 30
        Listele_Day7_Ocak()
    elif days == 11:
        gecici_day_ocak = 29
        Listele_Day7_Ocak()
    elif days == 10:
        gecici_day_ocak = 28
        Listele_Day7_Ocak()
    elif days == 9:
        gecici_day_ocak = 27
        Listele_Day7_Ocak()
    elif days == 8:
        gecici_day_ocak = 26
        Listele_Day7_Ocak()
    elif days == 7:
        gecici_day_ocak = 25
        Listele_Day7_Ocak()
    elif days == 6:
        gecici_day_ocak = 24
        Listele_Day7_Ocak()
    elif days == 5:
        gecici_day_ocak = 23
        Listele_Day7_Ocak()
    elif days == 4:
        gecici_day_ocak = 22
        Listele_Day7_Ocak()
    elif days == 3:
        gecici_day_ocak = 21
        Listele_Day7_Ocak()
    elif days == 2:
        gecici_day_ocak = 20
        Listele_Day7_Ocak()
    elif days == 1:
        gecici_day_ocak = 19
        Listele_Day7_Ocak()
elif (days <= 7 or days >= 7) and month == 3:
    month -= 1
    gecici_day_subat = subat_max
    if days == 14:
        month += 1
        gecici_day_subat = 1
        Listele_Day7_Subat()
    elif days == 13:
        gecici_day_subat = 28
        Listele_Day7_Subat()
    elif days == 12:
        gecici_day_subat = 27
        Listele_Day7_Subat()
    elif days == 11:
        gecici_day_subat = 26
        Listele_Day7_Subat()
    elif days == 10:
        gecici_day_subat = 25
        Listele_Day7_Subat()
    elif days == 9:
        gecici_day_subat = 24
        Listele_Day7_Subat()
    elif days == 8:
        gecici_day_subat = 23
        Listele_Day7_Subat()
    elif days == 7:
        gecici_day_subat = 22
        Listele_Day7_Subat()
    elif days == 6:
        gecici_day_subat = 21
        Listele_Day7_Subat()
    elif days == 5:
        gecici_day_subat = 20
        Listele_Day7_Subat()
    elif days == 4:
        gecici_day_subat = 19
        Listele_Day7_Subat()
    elif days == 3:
        gecici_day_subat = 18
        Listele_Day7_Subat()
    elif days == 2:
        gecici_day_subat = 17
        Listele_Day7_Subat()
    elif days == 1:
        gecici_day_subat = 16
        Listele_Day7_Subat()
elif (days <= 7 or days >= 7) and month == 4:
    month -= 1
    gecici_day_mart = mart_max
    if days == 14:
        month += 1
        gecici_day_mart = 1
        Listele_Day7_Mart()
    elif days == 13:
        gecici_day_mart = 31
        Listele_Day7_Mart()
    elif days == 12:
        gecici_day_mart = 30
        Listele_Day7_Mart()
    elif days == 11:
        gecici_day_mart = 29
        Listele_Day7_Mart()
    elif days == 10:
        gecici_day_mart = 28
        Listele_Day7_Mart()
    elif days == 9:
        gecici_day_mart = 27
        Listele_Day7_Mart()
    elif days == 8:
        gecici_day_mart = 26
        Listele_Day7_Mart()
    elif days == 7:
        gecici_day_mart = 25
        Listele_Day7_Mart()
    elif days == 6:
        gecici_day_mart = 24
        Listele_Day7_Mart()
    elif days == 5:
        gecici_day_mart = 23
        Listele_Day7_Mart()
    elif days == 4:
        gecici_day_mart = 22
        Listele_Day7_Mart()
    elif days == 3:
        gecici_day_mart = 21
        Listele_Day7_Mart()
    elif days == 2:
        gecici_day_mart = 20
        Listele_Day7_Mart()
    elif days == 1:
        gecici_day_mart = 19
        Listele_Day7_Mart()
elif (days <= 7 or days >= 7) and month == 5:
    month -= 1
    gecici_day_nisan = nisan_max
    if days == 14:
        month += 1
        gecici_day_nisan = 1
        Listele_Day7_Nisan()
    elif days == 13:
        gecici_day_nisan = 30
        Listele_Day7_Nisan()
    elif days == 12:
        gecici_day_nisan = 29
        Listele_Day7_Nisan()
    elif days == 11:
        gecici_day_nisan = 28
        Listele_Day7_Nisan()
    elif days == 10:
        gecici_day_nisan = 27
        Listele_Day7_Nisan()
    elif days == 9:
        gecici_day_nisan = 26
        Listele_Day7_Nisan()
    elif days == 8:
        gecici_day_nisan = 25
        Listele_Day7_Nisan()
    elif days == 7:
        gecici_day_nisan = 24
        Listele_Day7_Nisan()
    elif days == 6:
        gecici_day_nisan = 23
        Listele_Day7_Nisan()
    elif days == 5:
        gecici_day_nisan = 22
        Listele_Day7_Nisan()
    elif days == 4:
        gecici_day_nisan = 21
        Listele_Day7_Nisan()
    elif days == 3:
        gecici_day_nisan = 20
        Listele_Day7_Nisan()
    elif days == 2:
        gecici_day_nisan = 19
        Listele_Day7_Nisan()
    elif days == 1:
        gecici_day_nisan = 18
        Listele_Day7_Nisan()
elif (days <= 7 or days >= 7) and month == 6:
    month -= 1
    gecici_day_mayıs = mayıs_max
    if days == 14:
        month += 1
        gecici_day_mayıs = 1
        Listele_Day7_Mayıs()
    elif days == 13:
        gecici_day_mayıs = 31
        Listele_Day7_Mayıs()
    elif days == 12:
        gecici_day_mayıs = 30
        Listele_Day7_Mayıs()
    elif days == 11:
        gecici_day_mayıs = 29
        Listele_Day7_Mayıs()
    elif days == 10:
        gecici_day_mayıs = 28
        Listele_Day7_Mayıs()
    elif days == 9:
        gecici_day_mayıs = 27
        Listele_Day7_Mayıs()
    elif days == 8:
        gecici_day_mayıs = 26
        Listele_Day7_Mayıs()
    elif days == 7:
        gecici_day_mayıs = 25
        Listele_Day7_Mayıs()
    elif days == 6:
        gecici_day_mayıs = 24
        Listele_Day7_Mayıs()
    elif days == 5:
        gecici_day_mayıs = 23
        Listele_Day7_Mayıs()
    elif days == 4:
        gecici_day_mayıs = 22
        Listele_Day7_Mayıs()
    elif days == 3:
        gecici_day_mayıs = 21
        Listele_Day7_Mayıs()
    elif days == 2:
        gecici_day_mayıs = 20
        Listele_Day7_Mayıs()
    elif days == 1:
        gecici_day_mayıs = 10
        Listele_Day7_Mayıs()
elif (days <= 7 or days >= 7) and month == 7:
    month -= 1
    gecici_day_haziran = haziran_max
    if days == 14:
        month += 1
        gecici_day_haziran = 1
        Listele_Day7_Haziran()
    elif days == 13:
        gecici_day_haziran = 30
        Listele_Day7_Haziran()
    elif days == 12:
        gecici_day_haziran = 29
        Listele_Day7_Haziran()
    elif days == 11:
        gecici_day_haziran = 28
        Listele_Day7_Haziran()
    elif days == 10:
        gecici_day_haziran = 27
        Listele_Day7_Haziran()
    elif days == 9:
        gecici_day_haziran = 26
        Listele_Day7_Haziran()
    elif days == 8:
        gecici_day_haziran = 25
        Listele_Day7_Haziran()
    elif days == 7:
        gecici_day_haziran = 24
        Listele_Day7_Haziran()
    elif days == 6:
        gecici_day_haziran = 23
        Listele_Day7_Haziran()
    elif days == 5:
        gecici_day_haziran = 22
        Listele_Day7_Haziran()
    elif days == 4:
        gecici_day_haziran = 21
        Listele_Day7_Haziran()
    elif days == 3:
        gecici_day_haziran = 20
        Listele_Day7_Haziran()
    elif days == 2:
        gecici_day_haziran = 19
        Listele_Day7_Haziran()
    elif days == 1:
        gecici_day_haziran = 18
        Listele_Day7_Haziran()
elif (days <= 7 or days >= 7) and month == 8:
    month -= 1
    gecici_day_temmuz = temmuz_max
    if days == 14:
        month += 1
        gecici_day_temmuz = 1
        Listele_Day7_Temmuz()
    elif days == 13:
        gecici_day_temmuz = 31
        Listele_Day7_Temmuz()
    elif days == 12:
        gecici_day_temmuz = 30
        Listele_Day7_Temmuz()
    elif days == 11:
        gecici_day_temmuz = 29
        Listele_Day7_Temmuz()
    elif days == 10:
        gecici_day_temmuz = 28
        Listele_Day7_Temmuz()
    elif days == 9:
        gecici_day_temmuz = 27
        Listele_Day7_Temmuz()
    elif days == 8:
        gecici_day_temmuz = 26
        Listele_Day7_Temmuz()
    elif days == 7:
        gecici_day_temmuz = 25
        Listele_Day7_Temmuz()
    elif days == 6:
        gecici_day_temmuz = 24
        Listele_Day7_Temmuz()
    elif days == 5:
        gecici_day_temmuz = 23
        Listele_Day7_Temmuz()
    elif days == 4:
        gecici_day_temmuz = 22
        Listele_Day7_Temmuz()
    elif days == 3:
        gecici_day_temmuz = 21
        Listele_Day7_Temmuz()
    elif days == 2:
        gecici_day_temmuz = 20
        Listele_Day7_Temmuz()
    elif days == 1:
        gecici_day_temmuz = 19
        Listele_Day7_Temmuz()
elif (days <= 7 or days >= 7) and month == 9:
    month -= 1
    gecici_day_agustos = agustos_max
    if days == 14:
        month += 1
        gecici_day_agustos = 1
        Listele_Day7_Agustos()
    elif days == 13:
        gecici_day_agustos = 31
        Listele_Day7_Agustos()
    elif days == 12:
        gecici_day_agustos = 30
        Listele_Day7_Agustos()
    elif days == 11:
        gecici_day_agustos = 29
        Listele_Day7_Agustos()
    elif days == 10:
        gecici_day_agustos = 28
        Listele_Day7_Agustos()
    elif days == 9:
        gecici_day_agustos = 27
        Listele_Day7_Agustos()
    elif days == 8:
        gecici_day_agustos = 26
        Listele_Day7_Agustos()
    elif days == 7:
        gecici_day_agustos = 25
        Listele_Day7_Agustos()
    elif days == 6:
        gecici_day_agustos = 24
        Listele_Day7_Agustos()
    elif days == 5:
        gecici_day_agustos = 23
        Listele_Day7_Agustos()
    elif days == 4:
        gecici_day_agustos = 22
        Listele_Day7_Agustos()
    elif days == 3:
        gecici_day_agustos = 21
        Listele_Day7_Agustos()
    elif days == 2:
        gecici_day_agustos = 20
        Listele_Day7_Agustos()
    elif days == 1:
        gecici_day_agustos = 19
        Listele_Day7_Agustos()
elif (days <= 7 or days >= 7) and month == 10:
    month -= 1
    gecici_day_eylül = eylul_max
    if days == 14:
        month += 1
        gecici_day_eylül = 1
        Listele_Day7_Eylül()
    elif days == 13:
        gecici_day_eylül = 30
        Listele_Day7_Eylül()
    elif days == 12:
        gecici_day_eylül = 29
        Listele_Day7_Eylül()
    elif days == 11:
        gecici_day_eylül = 28
        Listele_Day7_Eylül()
    elif days == 10:
        gecici_day_eylül = 27
        Listele_Day7_Eylül()
    elif days == 9:
        gecici_day_eylül = 26
        Listele_Day7_Eylül()
    elif days == 8:
        gecici_day_eylül = 25
        Listele_Day7_Eylül()
    elif days == 7:
        gecici_day_eylül = 24
        Listele_Day7_Eylül()
    elif days == 6:
        gecici_day_eylül = 23
        Listele_Day7_Eylül()
    elif days == 5:
        gecici_day_eylül = 22
        Listele_Day7_Eylül()
    elif days == 4:
        gecici_day_eylül = 21
        Listele_Day7_Eylül()
    elif days == 3:
        gecici_day_eylül = 20
        Listele_Day7_Eylül()
    elif days == 2:
        gecici_day_eylül = 19
        Listele_Day7_Eylül()
    elif days == 1:
        gecici_day_eylül = 18
        Listele_Day7_Eylül()
elif (days <= 7 or days >= 7) and month == 11:
    month -= 1
    gecici_day_ekim = ekim_max
    if days == 14:
        month += 1
        gecici_day_ekim = 1
        Listele_Day7_Ekim()
    elif days == 13:
        gecici_day_ekim = 31
        Listele_Day7_Ekim()
    elif days == 12:
        gecici_day_ekim = 30
        Listele_Day7_Ekim()
    elif days == 11:
        gecici_day_ekim = 29
        Listele_Day7_Ekim()
    elif days == 10:
        gecici_day_ekim = 28
        Listele_Day7_Ekim()
    elif days == 9:
        gecici_day_ekim = 27
        Listele_Day7_Ekim()
    elif days == 8:
        gecici_day_ekim = 26
        Listele_Day7_Ekim()
    elif days == 7:
        gecici_day_ekim = 25
        Listele_Day7_Ekim()
    elif days == 6:
        gecici_day_ekim = 24
        Listele_Day7_Ekim()
    elif days == 5:
        gecici_day_ekim = 23
        Listele_Day7_Ekim()
    elif days == 4:
        gecici_day_ekim = 22
        Listele_Day7_Ekim()
    elif days == 3:
        gecici_day_ekim = 21
        Listele_Day7_Ekim()
    elif days == 2:
        gecici_day_ekim = 20
        Listele_Day7_Ekim()
    elif days == 1:
        gecici_day_ekim = 19
        Listele_Day7_Ekim()
elif (days <= 7 or days >= 7) and month == 12:
    month -= 1
    gecici_day_kasım = kasım_max
    if days == 14:
        month += 1
        gecici_day_kasım = 1
        Listele_Day7_Kasım()
    elif days == 13:
        gecici_day_kasım = 30
        Listele_Day7_Kasım()
    elif days == 12:
        gecici_day_kasım = 29
        Listele_Day7_Kasım()
    elif days == 11:
        gecici_day_kasım = 28
        Listele_Day7_Kasım()
    elif days == 10:
        gecici_day_kasım = 27
        Listele_Day7_Kasım()
    elif days == 9:
        gecici_day_kasım = 26
        Listele_Day7_Kasım()
    elif days == 8:
        gecici_day_kasım = 25
        Listele_Day7_Kasım()
    elif days == 7:
        gecici_day_kasım = 24
        Listele_Day7_Kasım()
    elif days == 6:
        gecici_day_kasım = 23
        Listele_Day7_Kasım()
    elif days == 5:
        gecici_day_kasım = 22
        Listele_Day7_Kasım()
    elif days == 4:
        gecici_day_kasım = 21
        Listele_Day7_Kasım()
    elif days == 3:
        gecici_day_kasım = 20
        Listele_Day7_Kasım()
    elif days == 2:
        gecici_day_kasım = 19
        Listele_Day7_Kasım()
    elif days == 1:
        gecici_day_kasım = 18
        Listele_Day7_Kasım()


# --------------------------------------------------
one_day_open = int(btc_open[-1])
one_day_close = int(btc_close[-1])
two_day_open = int(btc_open[-2])
two_day_close = int(btc_close[-2])
three_day_open = int(btc_open[-3])
three_day_close = int(btc_close[-3])
four_day_open = int(btc_open[-4])
four_day_close = int(btc_close[-4])
five_day_open = int(btc_open[-5])
five_day_close = int(btc_close[-5])
six_day_open = int(btc_open[-6])
six_day_close = int(btc_close[-6])
seven_day_open = int(btc_open[-7])
seven_day_close = int(btc_close[-7])


#----------------------------------ETHERNEUM---------------------------------------
eth_one_day_open = int(etherneum_open[-1])
eth_one_day_close = int(etherneum_close[-1])
eth_two_day_open = int(etherneum_open[-2])
eth_two_day_close = int(etherneum_close[-2])
eth_three_day_open = int(etherneum_open[-3])
eth_three_day_close = int(etherneum_close[-3])
eth_four_day_open = int(etherneum_open[-4])
eth_four_day_close = int(etherneum_close[-4])
eth_five_day_open = int(etherneum_open[-5])
eth_five_day_close = int(etherneum_close[-5])
eth_six_day_open = int(etherneum_open[-6])
eth_six_day_close = int(etherneum_close[-6])
eth_seven_day_open = int(etherneum_open[-7])
eth_seven_day_close = int(etherneum_close[-7])

#----------------------------------SOLONA---------------------------------------
sol_one_day_open = int(solona_open[-1])
sol_one_day_close = int(solona_close[-1])
sol_two_day_open = int(solona_open[-2])
sol_two_day_close = int(solona_close[-2])
sol_three_day_open = int(solona_open[-3])
sol_three_day_close = int(solona_close[-3])
sol_four_day_open = int(solona_open[-4])
sol_four_day_close = int(solona_close[-4])
sol_five_day_open = int(solona_open[-5])
sol_five_day_close = int(solona_close[-5])
sol_six_day_open = int(solona_open[-6])
sol_six_day_close = int(solona_close[-6])
sol_seven_day_open = int(solona_open[-7])
sol_seven_day_close = int(solona_close[-7])

#----------------------------------DOGE---------------------------------------
doge_one_day_open = float(dogecoin_open[-1])
doge_one_day_close = float(dogecoin_close[-1])
doge_two_day_open = float(dogecoin_open[-2])
doge_two_day_close = float(dogecoin_close[-2])
doge_three_day_open = float(dogecoin_open[-3])
doge_three_day_close = float(dogecoin_close[-3])
doge_four_day_open = float(dogecoin_open[-4])
doge_four_day_close = float(dogecoin_close[-4])
doge_five_day_open = float(dogecoin_open[-5])
doge_five_day_close = float(dogecoin_close[-5])
doge_six_day_open = float(dogecoin_open[-6])
doge_six_day_close = float(dogecoin_close[-6])
doge_seven_day_open = float(dogecoin_open[-7])
doge_seven_day_close = float(dogecoin_close[-7])

#----------------------------------ENJİN---------------------------------------
enjin_one_day_open = float(enjin_open[-1])
enjin_one_day_close = float(enjin_close[-1])
enjin_two_day_open = float(enjin_open[-2])
enjin_two_day_close = float(enjin_close[-2])
enjin_three_day_open = float(enjin_open[-3])
enjin_three_day_close = float(enjin_close[-3])
enjin_four_day_open = float(enjin_open[-4])
enjin_four_day_close = float(enjin_close[-4])
enjin_five_day_open = float(enjin_open[-5])
enjin_five_day_close = float(enjin_close[-5])
enjin_six_day_open = float(enjin_open[-6])
enjin_six_day_close = float(enjin_close[-6])
enjin_seven_day_open = float(enjin_open[-7])
enjin_seven_day_close = float(enjin_close[-7])

#----------------------------------AVAX---------------------------------------
avax_one_day_open = float(avalance_open[-1])
avax_one_day_close = float(avalance_close[-1])
avax_two_day_open = float(avalance_open[-2])
avax_two_day_close = float(avalance_close[-2])
avax_three_day_open = float(avalance_open[-3])
avax_three_day_close = float(avalance_close[-3])
avax_four_day_open = float(avalance_open[-4])
avax_four_day_close = float(avalance_close[-4])
avax_five_day_open = float(avalance_open[-5])
avax_five_day_close = float(avalance_close[-5])
avax_six_day_open = float(avalance_open[-6])
avax_six_day_close = float(avalance_close[-6])
avax_seven_day_open = float(avalance_open[-7])
avax_seven_day_close = float(avalance_close[-7])

#----------------------------------MANA---------------------------------------
mana_one_day_open = float(mana_open[-1])
mana_one_day_close = float(mana_close[-1])
mana_two_day_open = float(mana_open[-2])
mana_two_day_close = float(mana_close[-2])
mana_three_day_open = float(mana_open[-3])
mana_three_day_close = float(mana_close[-3])
mana_four_day_open = float(mana_open[-4])
mana_four_day_close = float(mana_close[-4])
mana_five_day_open = float(mana_open[-5])
mana_five_day_close = float(mana_close[-5])
mana_six_day_open = float(mana_open[-6])
mana_six_day_close = float(mana_close[-6])
mana_seven_day_open = float(mana_open[-7])
mana_seven_day_close = float(mana_close[-7])

#----------------------------------ADA---------------------------------------
ada_one_day_open = float(ada_open[-1])
ada_one_day_close = float(ada_close[-1])
ada_two_day_open = float(ada_open[-2])
ada_two_day_close = float(ada_close[-2])
ada_three_day_open = float(ada_open[-3])
ada_three_day_close = float(ada_close[-3])
ada_four_day_open = float(ada_open[-4])
ada_four_day_close = float(ada_close[-4])
ada_five_day_open = float(ada_open[-5])
ada_five_day_close = float(ada_close[-5])
ada_six_day_open = float(ada_open[-6])
ada_six_day_close = float(ada_close[-6])
ada_seven_day_open = float(ada_open[-7])
ada_seven_day_close = float(ada_close[-7])

#----------------------------------DOT---------------------------------------
dot_one_day_open = float(dot_open[-1])
dot_one_day_close = float(dot_close[-1])
dot_two_day_open = float(dot_open[-2])
dot_two_day_close = float(dot_close[-2])
dot_three_day_open = float(dot_open[-3])
dot_three_day_close = float(dot_close[-3])
dot_four_day_open = float(dot_open[-4])
dot_four_day_close = float(dot_close[-4])
dot_five_day_open = float(dot_open[-5])
dot_five_day_close = float(dot_close[-5])
dot_six_day_open = float(dot_open[-6])
dot_six_day_close = float(dot_close[-6])
dot_seven_day_open = float(dot_open[-7])
dot_seven_day_close = float(dot_close[-7])

#----------------------------------LINK---------------------------------------
lınk_one_day_open = float(lınk_open[-1])
lınk_one_day_close = float(lınk_close[-1])
lınk_two_day_open = float(lınk_open[-2])
lınk_two_day_close = float(lınk_close[-2])
lınk_three_day_open = float(lınk_open[-3])
lınk_three_day_close = float(lınk_close[-3])
lınk_four_day_open = float(lınk_open[-4])
lınk_four_day_close = float(lınk_close[-4])
lınk_five_day_open = float(lınk_open[-5])
lınk_five_day_close = float(lınk_close[-5])
lınk_six_day_open = float(lınk_open[-6])
lınk_six_day_close = float(lınk_close[-6])
lınk_seven_day_open = float(lınk_open[-7])
lınk_seven_day_close = float(lınk_close[-7])

#----------------------------------LTC---------------------------------------
ltc_one_day_open = float(lınk_open[-1])
ltc_one_day_close = float(lınk_close[-1])
ltc_two_day_open = float(lınk_open[-2])
ltc_two_day_close = float(lınk_close[-2])
ltc_three_day_open = float(lınk_open[-3])
ltc_three_day_close = float(lınk_close[-3])
ltc_four_day_open = float(lınk_open[-4])
ltc_four_day_close = float(lınk_close[-4])
ltc_five_day_open = float(lınk_open[-5])
ltc_five_day_close = float(lınk_close[-5])
ltc_six_day_open = float(lınk_open[-6])
ltc_six_day_close = float(lınk_close[-6])
ltc_seven_day_open = float(lınk_open[-7])
ltc_seven_day_close = float(lınk_close[-7])

#----------------------------------UNI---------------------------------------
uni_one_day_open = float(lınk_open[-1])
uni_one_day_close = float(lınk_close[-1])
uni_two_day_open = float(lınk_open[-2])
uni_two_day_close = float(lınk_close[-2])
uni_three_day_open = float(lınk_open[-3])
uni_three_day_close = float(lınk_close[-3])
uni_four_day_open = float(lınk_open[-4])
uni_four_day_close = float(lınk_close[-4])
uni_five_day_open = float(lınk_open[-5])
uni_five_day_close = float(lınk_close[-5])
uni_six_day_open = float(lınk_open[-6])
uni_six_day_close = float(lınk_close[-6])
uni_seven_day_open = float(lınk_open[-7])
uni_seven_day_close = float(lınk_close[-7])

#----------------------------------ETC---------------------------------------
etc_one_day_open = float(lınk_open[-1])
etc_one_day_close = float(lınk_close[-1])
etc_two_day_open = float(lınk_open[-2])
etc_two_day_close = float(lınk_close[-2])
etc_three_day_open = float(lınk_open[-3])
etc_three_day_close = float(lınk_close[-3])
etc_four_day_open = float(lınk_open[-4])
etc_four_day_close = float(lınk_close[-4])
etc_five_day_open = float(lınk_open[-5])
etc_five_day_close = float(lınk_close[-5])
etc_six_day_open = float(lınk_open[-6])
etc_six_day_close = float(lınk_close[-6])
etc_seven_day_open = float(lınk_open[-7])
etc_seven_day_close = float(lınk_close[-7])


# PROPOSAL
class Piyasa():
    def __init__(self):
        self.BİTCOİN = float

        self.ONE_DAY_YUZDE = 0
        self.TWO_DAY_YUZDE = 0
        self.THREE_DAY_YUZDE = 0
        self.FOUR_DAY_YUZDE = 0
        self.FİVE_DAY_YUZDE = 0
        self.SİX_DAY_YUZDE = 0
        self.SEVEN_DAY_YUZDE = 0


        self.ONE_DAY_CLOSE = one_day_close
        self.TWO_DAY_CLOSE = two_day_close
        self.THREE_DAY_CLOSE = three_day_close
        self.FOUR_DAY_CLOSE = four_day_close
        self.FİVE_DAY_CLOSE = five_day_close
        self.SİX_DAY_CLOSE = six_day_close
        self.SEVEN_DAY_CLOSE = seven_day_close


        self.ONE_DAY_OPEN = one_day_open
        self.TWO_DAY_OPEN = two_day_open
        self.THREE_DAY_OPEN = three_day_open
        self.FOUR_DAY_OPEN = four_day_open
        self.FİVE_DAY_OPEN = five_day_open
        self.SİX_DAY_OPEN = six_day_open
        self.SEVEN_DAY_OPEN = seven_day_open


        self.BTC_POZİTİF_ONE()
        self.BTC_POZİTİF_TWO()
        self.BTC_POZİTİF_THREE()
        self.BTC_POZİTİF_FOUR()
        self.BTC_POZİTİF_FİVE()
        self.BTC_POZİTİF_SİX()
        self.BTC_POZİTİF_SEVEN()

        self.BTC_NEGATİF_ONE()
        self.BTC_NEGATİF_TWO()
        self.BTC_NEGATİF_THREE()
        self.BTC_NEGATİF_FOUR()
        self.BTC_NEGATİF_FİVE()
        self.BTC_NEGATİF_SİX()
        self.BTC_NEGATİF_SEVEN()
        self.NET_BİTCOİN()
    def NET_BİTCOİN(self):
        BİTCOİN_NET = self.ONE_DAY_YUZDE + self.TWO_DAY_YUZDE + \
                      self.THREE_DAY_YUZDE + self.FOUR_DAY_YUZDE + self.FİVE_DAY_YUZDE + \
                      self.SİX_DAY_YUZDE + self.SEVEN_DAY_YUZDE

        self.BİTCOİN = BİTCOİN_NET
    def BTC_NEGATİF_ONE(self):
        ekle = 0.0
        close = self.ONE_DAY_CLOSE
        open = self.ONE_DAY_OPEN
        while True:
            value = (close * (ekle)) / 100
            if (int(close) + float(value)) >= int(open):
                self.ONE_DAY_YUZDE -= float(ekle)
                break
            else:
                ekle += 0.005
    def BTC_NEGATİF_TWO(self):
        ekle = 0.0
        close = self.TWO_DAY_CLOSE
        open = self.TWO_DAY_OPEN
        while True:
            value = (close * (ekle)) / 100
            if (int(close) + float(value)) >= int(open):
                self.TWO_DAY_YUZDE -= float(ekle)
                break
            else:
                ekle += 0.005
    def BTC_NEGATİF_THREE(self):
        ekle = 0.0
        close = self.THREE_DAY_CLOSE
        open = self.THREE_DAY_OPEN
        while True:
            value = (close * (ekle)) / 100
            if (int(close) + float(value)) >= int(open):
                self.THREE_DAY_YUZDE -= float(ekle)
                break
            else:
                ekle += 0.005
    def BTC_NEGATİF_FOUR(self):
        ekle = 0.0
        close = self.FOUR_DAY_CLOSE
        open = self.FOUR_DAY_OPEN
        while True:
            value = (close * (ekle)) / 100
            if (int(close) + float(value)) >= int(open):
                self.FOUR_DAY_YUZDE -= float(ekle)
                break
            else:
                ekle += 0.005
    def BTC_NEGATİF_FİVE(self):
        ekle = 0.0
        close = self.FİVE_DAY_CLOSE
        open = self.FİVE_DAY_OPEN
        while True:
            value = (close * (ekle)) / 100
            if (int(close) + float(value)) >= int(open):
                self.FİVE_DAY_YUZDE -= float(ekle)
                break
            else:
                ekle += 0.005
    def BTC_NEGATİF_SİX(self):
        ekle = 0.0
        close = self.SİX_DAY_CLOSE
        open = self.SİX_DAY_OPEN
        while True:
            value = (close * (ekle)) / 100
            if (int(close) + float(value)) >= int(open):
                self.SİX_DAY_YUZDE -= float(ekle)
                break
            else:
                ekle += 0.005
    def BTC_NEGATİF_SEVEN(self):
        ekle = 0.0
        close = self.SEVEN_DAY_CLOSE
        open = self.SEVEN_DAY_OPEN
        while True:
            value = (close * (ekle)) / 100
            if (int(close) + float(value)) >= int(open):
                self.SEVEN_DAY_YUZDE -= float(ekle)
                break
            else:
                ekle += 0.005
    def BTC_POZİTİF_ONE(self):
        ekle = 0.0
        close = self.ONE_DAY_CLOSE
        open = self.ONE_DAY_OPEN
        while True:
            value = (open * (ekle)) / 100
            if (int(open) + float(value)) >= int(close):
                self.ONE_DAY_YUZDE += float(ekle)
                break
            else:
                ekle += 0.005
    def BTC_POZİTİF_TWO(self):
        ekle = 0.0
        close = self.TWO_DAY_CLOSE
        open = self.TWO_DAY_OPEN
        while True:
            value = (open * (ekle)) / 100
            if (int(open) + float(value)) >= int(close):
                self.TWO_DAY_YUZDE += float(ekle)
                break
            else:
                ekle += 0.005
    def BTC_POZİTİF_THREE(self):
        ekle = 0.0
        close = self.THREE_DAY_CLOSE
        open = self.THREE_DAY_OPEN
        while True:
            value = (open * (ekle)) / 100
            if (int(open) + float(value)) >= int(close):
                self.THREE_DAY_YUZDE += float(ekle)
                break
            else:
                ekle += 0.005
    def BTC_POZİTİF_FOUR(self):
        ekle = 0.0
        close = self.FOUR_DAY_CLOSE
        open = self.FOUR_DAY_OPEN
        while True:
            value = (open * (ekle)) / 100
            if (int(open) + float(value)) >= int(close):
                self.FOUR_DAY_YUZDE += float(ekle)
                break
            else:
                ekle += 0.005
    def BTC_POZİTİF_FİVE(self):
        ekle = 0.0
        close = self.FİVE_DAY_CLOSE
        open = self.FİVE_DAY_OPEN
        while True:
            value = (open * (ekle)) / 100
            if (int(open) + float(value)) >= int(close):
                self.FİVE_DAY_YUZDE += float(ekle)
                break
            else:
                ekle += 0.005
    def BTC_POZİTİF_SİX(self):
        ekle = 0.0
        close = self.SİX_DAY_CLOSE
        open = self.SİX_DAY_OPEN
        while True:
            value = (open * (ekle)) / 100
            if (int(open) + float(value)) >= int(close):
                self.SİX_DAY_YUZDE += float(ekle)
                break
            else:
                ekle += 0.005
    def BTC_POZİTİF_SEVEN(self):
        ekle = 0.0
        close = self.SEVEN_DAY_CLOSE
        open = self.SEVEN_DAY_OPEN
        while True:
            value = (open * (ekle)) / 100
            if (int(open) + float(value)) >= int(close):
                self.SEVEN_DAY_YUZDE += float(ekle)
                break
            else:
                ekle += 0.005
class Proposal(Piyasa):
    def __init__(self):
        super().__init__()
        self.Market_STR = str
        self.Market_INT = int
        self.Market_Analysis()
    def __str__(self):
        print("\n\n")
        print("Crypto ROB Demo Core Versiyon !")
        print("-----------------------------------------------------")
        print(self.Market_STR)
        print("-----------------------------------------------------")
        print("Crypto ROB The Best Trading !")
    def Market_Analysis(self):
        print("Piyasa Durumu : ",round(self.BİTCOİN,2),end="%")
        if 10.5 <= self.BİTCOİN:
            self.Market_INT = 1
            self.Market_STR = "Mega Boğa Piyasası"
        elif 9 <= self.BİTCOİN:
            self.Market_INT = 2
            self.Market_STR = "Mega Boğa Piyasası"
        elif 7.5 <= self.BİTCOİN:
            self.Market_INT = 3
            self.Market_STR = "Büyük Boğa Piyasası"
        elif 6 <= self.BİTCOİN:
            self.Market_INT = 4
            self.Market_STR = "Büyük Boğa Piyasası"
        elif 4.5 <= self.BİTCOİN:
            self.Market_INT = 5
            self.Market_STR = "Normal Boğa Piyasası"
        elif 3 <= self.BİTCOİN:
            self.Market_INT = 6
            self.Market_STR = "Normal Boğa Piyasası"
        elif 1.5 <= self.BİTCOİN:
            self.Market_INT = 7
            self.Market_STR = "Normal Yükseliş Piyasası"

        elif -10.5 >= self.BİTCOİN:
            self.Market_INT = -1
            self.Market_STR = "Mega Ayı Piyasası"
        elif -9 >= self.BİTCOİN:
            self.Market_INT = -2
            self.Market_STR = "Mega Ayı Piyasası"
        elif -7.5 >= self.BİTCOİN:
            self.Market_INT = -3
            self.Market_STR = "Büyük Ayı Piyasası"
        elif -6 >= self.BİTCOİN:
            self.Market_INT = -4
            self.Market_STR = "Büyük Ayı Piyasası"
        elif -4.5 >= self.BİTCOİN:
            self.Market_INT = -5
            self.Market_STR = "Normal Ayı Piyasası"
        elif -3 >= self.BİTCOİN:
            self.Market_INT = -6
            self.Market_STR = "Normal Ayı Piyasası"
        elif -1.5 >= self.BİTCOİN:
            self.Market_INT = -7
            self.Market_STR = "Normal Düşüş Piyasası"

        else:
            self.Market_STR = "Nötr Piyasa"
Proposal = Proposal()
Proposal.__str__()

Coinler = dict()
class Bitcoin():
    def __init__(self):
        self.BİTCOİN = float

        self.ONE_DAY_YUZDE = 0
        self.TWO_DAY_YUZDE = 0
        self.THREE_DAY_YUZDE = 0
        self.FOUR_DAY_YUZDE = 0
        self.FİVE_DAY_YUZDE = 0
        self.SİX_DAY_YUZDE = 0
        self.SEVEN_DAY_YUZDE = 0


        self.ONE_DAY_CLOSE = one_day_close
        self.TWO_DAY_CLOSE = two_day_close
        self.THREE_DAY_CLOSE = three_day_close
        self.FOUR_DAY_CLOSE = four_day_close
        self.FİVE_DAY_CLOSE = five_day_close
        self.SİX_DAY_CLOSE = six_day_close
        self.SEVEN_DAY_CLOSE = seven_day_close


        self.ONE_DAY_OPEN = one_day_open
        self.TWO_DAY_OPEN = two_day_open
        self.THREE_DAY_OPEN = three_day_open
        self.FOUR_DAY_OPEN = four_day_open
        self.FİVE_DAY_OPEN = five_day_open
        self.SİX_DAY_OPEN = six_day_open
        self.SEVEN_DAY_OPEN = seven_day_open

        self.BTC_POZİTİF_ONE()
        self.BTC_POZİTİF_TWO()
        self.BTC_POZİTİF_THREE()
        self.BTC_POZİTİF_FOUR()
        self.BTC_POZİTİF_FİVE()
        self.BTC_POZİTİF_SİX()
        self.BTC_POZİTİF_SEVEN()

        self.BTC_NEGATİF_ONE()
        self.BTC_NEGATİF_TWO()
        self.BTC_NEGATİF_THREE()
        self.BTC_NEGATİF_FOUR()
        self.BTC_NEGATİF_FİVE()
        self.BTC_NEGATİF_SİX()
        self.BTC_NEGATİF_SEVEN()
        self.NET_BİTCOİN()

    def NET_BİTCOİN(self):
        BİTCOİN_NET = self.ONE_DAY_YUZDE + self.TWO_DAY_YUZDE + \
                      self.THREE_DAY_YUZDE + self.FOUR_DAY_YUZDE + self.FİVE_DAY_YUZDE + \
                      self.SİX_DAY_YUZDE + self.SEVEN_DAY_YUZDE

        self.BİTCOİN = BİTCOİN_NET

    def BTC_NEGATİF_ONE(self):
        ekle = 0.0
        close = self.ONE_DAY_CLOSE
        open = self.ONE_DAY_OPEN
        while True:
            value = (close * (ekle)) / 100
            if (int(close) + float(value)) >= int(open):
                self.ONE_DAY_YUZDE -= float(ekle)
                break
            else:
                ekle += 0.005

    def BTC_NEGATİF_TWO(self):
        ekle = 0.0
        close = self.TWO_DAY_CLOSE
        open = self.TWO_DAY_OPEN
        while True:
            value = (close * (ekle)) / 100
            if (int(close) + float(value)) >= int(open):
                self.TWO_DAY_YUZDE -= float(ekle)
                break
            else:
                ekle += 0.005

    def BTC_NEGATİF_THREE(self):
        ekle = 0.0
        close = self.THREE_DAY_CLOSE
        open = self.THREE_DAY_OPEN
        while True:
            value = (close * (ekle)) / 100
            if (int(close) + float(value)) >= int(open):
                self.THREE_DAY_YUZDE -= float(ekle)
                break
            else:
                ekle += 0.005

    def BTC_NEGATİF_FOUR(self):
        ekle = 0.0
        close = self.FOUR_DAY_CLOSE
        open = self.FOUR_DAY_OPEN
        while True:
            value = (close * (ekle)) / 100
            if (int(close) + float(value)) >= int(open):
                self.FOUR_DAY_YUZDE -= float(ekle)
                break
            else:
                ekle += 0.005

    def BTC_NEGATİF_FİVE(self):
        ekle = 0.0
        close = self.FİVE_DAY_CLOSE
        open = self.FİVE_DAY_OPEN
        while True:
            value = (close * (ekle)) / 100
            if (int(close) + float(value)) >= int(open):
                self.FİVE_DAY_YUZDE -= float(ekle)
                break
            else:
                ekle += 0.005

    def BTC_NEGATİF_SİX(self):
        ekle = 0.0
        close = self.SİX_DAY_CLOSE
        open = self.SİX_DAY_OPEN
        while True:
            value = (close * (ekle)) / 100
            if (int(close) + float(value)) >= int(open):
                self.SİX_DAY_YUZDE -= float(ekle)
                break
            else:
                ekle += 0.005

    def BTC_NEGATİF_SEVEN(self):
        ekle = 0.0
        close = self.SEVEN_DAY_CLOSE
        open = self.SEVEN_DAY_OPEN
        while True:
            value = (close * (ekle)) / 100
            if (int(close) + float(value)) >= int(open):
                self.SEVEN_DAY_YUZDE -= float(ekle)
                break
            else:
                ekle += 0.005

    def BTC_POZİTİF_ONE(self):
        ekle = 0.0
        close = self.ONE_DAY_CLOSE
        open = self.ONE_DAY_OPEN
        while True:
            value = (open * (ekle)) / 100
            if (int(open) + float(value)) >= int(close):
                self.ONE_DAY_YUZDE += float(ekle)
                break
            else:
                ekle += 0.005

    def BTC_POZİTİF_TWO(self):
        ekle = 0.0
        close = self.TWO_DAY_CLOSE
        open = self.TWO_DAY_OPEN
        while True:
            value = (open * (ekle)) / 100
            if (int(open) + float(value)) >= int(close):
                self.TWO_DAY_YUZDE += float(ekle)
                break
            else:
                ekle += 0.005

    def BTC_POZİTİF_THREE(self):
        ekle = 0.0
        close = self.THREE_DAY_CLOSE
        open = self.THREE_DAY_OPEN
        while True:
            value = (open * (ekle)) / 100
            if (int(open) + float(value)) >= int(close):
                self.THREE_DAY_YUZDE += float(ekle)
                break
            else:
                ekle += 0.005

    def BTC_POZİTİF_FOUR(self):
        ekle = 0.0
        close = self.FOUR_DAY_CLOSE
        open = self.FOUR_DAY_OPEN
        while True:
            value = (open * (ekle)) / 100
            if (int(open) + float(value)) >= int(close):
                self.FOUR_DAY_YUZDE += float(ekle)
                break
            else:
                ekle += 0.005

    def BTC_POZİTİF_FİVE(self):
        ekle = 0.0
        close = self.FİVE_DAY_CLOSE
        open = self.FİVE_DAY_OPEN
        while True:
            value = (open * (ekle)) / 100
            if (int(open) + float(value)) >= int(close):
                self.FİVE_DAY_YUZDE += float(ekle)
                break
            else:
                ekle += 0.005

    def BTC_POZİTİF_SİX(self):
        ekle = 0.0
        close = self.SİX_DAY_CLOSE
        open = self.SİX_DAY_OPEN
        while True:
            value = (open * (ekle)) / 100
            if (int(open) + float(value)) >= int(close):
                self.SİX_DAY_YUZDE += float(ekle)
                break
            else:
                ekle += 0.005

    def BTC_POZİTİF_SEVEN(self):
        ekle = 0.0
        close = self.SEVEN_DAY_CLOSE
        open = self.SEVEN_DAY_OPEN
        while True:
            value = (open * (ekle)) / 100
            if (int(open) + float(value)) >= int(close):
                self.SEVEN_DAY_YUZDE += float(ekle)
                break
            else:
                ekle += 0.005
class Etherneum():
    def __init__(self):
        self.ETHERNEUM = float

        self.ONE_DAY_YUZDE = 0
        self.TWO_DAY_YUZDE = 0
        self.THREE_DAY_YUZDE = 0
        self.FOUR_DAY_YUZDE = 0
        self.FİVE_DAY_YUZDE = 0
        self.SİX_DAY_YUZDE = 0
        self.SEVEN_DAY_YUZDE = 0

        self.ONE_DAY_CLOSE = eth_one_day_close
        self.TWO_DAY_CLOSE = eth_two_day_close
        self.THREE_DAY_CLOSE = eth_three_day_close
        self.FOUR_DAY_CLOSE = eth_four_day_close
        self.FİVE_DAY_CLOSE = eth_five_day_close
        self.SİX_DAY_CLOSE = eth_six_day_close
        self.SEVEN_DAY_CLOSE = eth_seven_day_close

        self.ONE_DAY_OPEN = eth_one_day_open
        self.TWO_DAY_OPEN = eth_two_day_open
        self.THREE_DAY_OPEN = eth_three_day_open
        self.FOUR_DAY_OPEN = eth_four_day_open
        self.FİVE_DAY_OPEN = eth_five_day_open
        self.SİX_DAY_OPEN = eth_six_day_open
        self.SEVEN_DAY_OPEN = eth_seven_day_open


        self.ETH_POZİTİF_ONE()
        self.ETH_POZİTİF_TWO()
        self.ETH_POZİTİF_THREE()
        self.ETH_POZİTİF_FOUR()
        self.ETH_POZİTİF_FİVE()
        self.ETH_POZİTİF_SİX()
        self.ETH_POZİTİF_SEVEN()

        self.ETH_NEGATİF_ONE()
        self.ETH_NEGATİF_TWO()
        self.ETH_NEGATİF_THREE()
        self.ETH_NEGATİF_FOUR()
        self.ETH_NEGATİF_FİVE()
        self.ETH_NEGATİF_SİX()
        self.ETH_NEGATİF_SEVEN()

        self.NET_ETHERNEUM()
        self.Ekle()
    def Ekle(self):
        Coinler["ETHBUSD "] = round(float(self.ETHERNEUM),1)
    def NET_ETHERNEUM(self):
        ETHERNEUM_NET = self.ONE_DAY_YUZDE + self.TWO_DAY_YUZDE + self.THREE_DAY_YUZDE + \
            self.FOUR_DAY_YUZDE + self.FİVE_DAY_YUZDE + self.SİX_DAY_YUZDE + \
            self.SEVEN_DAY_YUZDE

        self.ETHERNEUM = ETHERNEUM_NET
    def ETH_NEGATİF_ONE(self):
        ekle = 0.0
        close = self.ONE_DAY_CLOSE
        open = self.ONE_DAY_OPEN
        while True:
            value = (close * (ekle)) / 100
            if (int(close) + float(value)) >= int(open):
                self.ONE_DAY_YUZDE -= float(ekle)
                break
            else:
                ekle += 0.005
    def ETH_NEGATİF_TWO(self):
        ekle = 0.0
        close = self.TWO_DAY_CLOSE
        open = self.TWO_DAY_OPEN
        while True:
            value = (close * (ekle)) / 100
            if (int(close) + float(value)) >= int(open):
                self.TWO_DAY_YUZDE -= float(ekle)
                break
            else:
                ekle += 0.005
    def ETH_NEGATİF_THREE(self):
        ekle = 0.0
        close = self.THREE_DAY_CLOSE
        open = self.THREE_DAY_OPEN
        while True:
            value = (close * (ekle)) / 100
            if (int(close) + float(value)) >= int(open):
                self.THREE_DAY_YUZDE -= float(ekle)
                break
            else:
                ekle += 0.005
    def ETH_NEGATİF_FOUR(self):
        ekle = 0.0
        close = self.FOUR_DAY_CLOSE
        open = self.FOUR_DAY_OPEN
        while True:
            value = (close * (ekle)) / 100
            if (int(close) + float(value)) >= int(open):
                self.FOUR_DAY_YUZDE -= float(ekle)
                break
            else:
                ekle += 0.005
    def ETH_NEGATİF_FİVE(self):
        ekle = 0.0
        close = self.FİVE_DAY_CLOSE
        open = self.FİVE_DAY_OPEN
        while True:
            value = (close * (ekle)) / 100
            if (int(close) + float(value)) >= int(open):
                self.FİVE_DAY_YUZDE -= float(ekle)
                break
            else:
                ekle += 0.005
    def ETH_NEGATİF_SİX(self):
        ekle = 0.0
        close = self.SİX_DAY_CLOSE
        open = self.SİX_DAY_OPEN
        while True:
            value = (close * (ekle)) / 100
            if (int(close) + float(value)) >= int(open):
                self.SİX_DAY_YUZDE -= float(ekle)
                break
            else:
                ekle += 0.005
    def ETH_NEGATİF_SEVEN(self):
        ekle = 0.0
        close = self.SEVEN_DAY_CLOSE
        open = self.SEVEN_DAY_OPEN
        while True:
            value = (close * (ekle)) / 100
            if (int(close) + float(value)) >= int(open):
                self.SEVEN_DAY_YUZDE -= float(ekle)
                break
            else:
                ekle += 0.005

    def ETH_POZİTİF_ONE(self):
        ekle = 0.0
        close = self.ONE_DAY_CLOSE
        open = self.ONE_DAY_OPEN
        while True:
            value = (open * (ekle)) / 100
            if (int(open) + float(value)) >= int(close):
                self.ONE_DAY_YUZDE += float(ekle)
                break
            else:
                ekle += 0.005
    def ETH_POZİTİF_TWO(self):
        ekle = 0.0
        close = self.TWO_DAY_CLOSE
        open = self.TWO_DAY_OPEN
        while True:
            value = (open * (ekle)) / 100
            if (int(open) + float(value)) >= int(close):
                self.TWO_DAY_YUZDE += float(ekle)
                break
            else:
                ekle += 0.005
    def ETH_POZİTİF_THREE(self):
        ekle = 0.0
        close = self.THREE_DAY_CLOSE
        open = self.THREE_DAY_OPEN
        while True:
            value = (open * (ekle)) / 100
            if (int(open) + float(value)) >= int(close):
                self.THREE_DAY_YUZDE += float(ekle)
                break
            else:
                ekle += 0.005
    def ETH_POZİTİF_FOUR(self):
        ekle = 0.0
        close = self.FOUR_DAY_CLOSE
        open = self.FOUR_DAY_OPEN
        while True:
            value = (open * (ekle)) / 100
            if (int(open) + float(value)) >= int(close):
                self.FOUR_DAY_YUZDE += float(ekle)
                break
            else:
                ekle += 0.005
    def ETH_POZİTİF_FİVE(self):
        ekle = 0.0
        close = self.FİVE_DAY_CLOSE
        open = self.FİVE_DAY_OPEN
        while True:
            value = (open * (ekle)) / 100
            if (int(open) + float(value)) >= int(close):
                self.FİVE_DAY_YUZDE += float(ekle)
                break
            else:
                ekle += 0.005
    def ETH_POZİTİF_SİX(self):
        ekle = 0.0
        close = self.SİX_DAY_CLOSE
        open = self.SİX_DAY_OPEN
        while True:
            value = (open * (ekle)) / 100
            if (int(open) + float(value)) >= int(close):
                self.SİX_DAY_YUZDE += float(ekle)
                break
            else:
                ekle += 0.005
    def ETH_POZİTİF_SEVEN(self):
        ekle = 0.0
        close = self.SEVEN_DAY_CLOSE
        open = self.SEVEN_DAY_OPEN
        while True:
            value = (open * (ekle)) / 100
            if (int(open) + float(value)) >= int(close):
                self.SEVEN_DAY_YUZDE += float(ekle)
                break
            else:
                ekle += 0.005
class Solona():
    def __init__(self):
        self.SOLONA = float

        self.ONE_DAY_YUZDE = 0
        self.TWO_DAY_YUZDE = 0
        self.THREE_DAY_YUZDE = 0
        self.FOUR_DAY_YUZDE = 0
        self.FİVE_DAY_YUZDE = 0
        self.SİX_DAY_YUZDE = 0
        self.SEVEN_DAY_YUZDE = 0

        self.ONE_DAY_CLOSE = sol_one_day_close
        self.TWO_DAY_CLOSE = sol_two_day_close
        self.THREE_DAY_CLOSE = sol_three_day_close
        self.FOUR_DAY_CLOSE = sol_four_day_close
        self.FİVE_DAY_CLOSE = sol_five_day_close
        self.SİX_DAY_CLOSE = sol_six_day_close
        self.SEVEN_DAY_CLOSE = sol_seven_day_close


        self.ONE_DAY_OPEN = sol_one_day_open
        self.TWO_DAY_OPEN = sol_two_day_open
        self.THREE_DAY_OPEN = sol_three_day_open
        self.FOUR_DAY_OPEN = sol_four_day_open
        self.FİVE_DAY_OPEN = sol_five_day_open
        self.SİX_DAY_OPEN = sol_six_day_open
        self.SEVEN_DAY_OPEN = sol_seven_day_open

        self.SOL_POZİTİF_ONE()
        self.SOL_POZİTİF_TWO()
        self.SOL_POZİTİF_THREE()
        self.SOL_POZİTİF_FOUR()
        self.SOL_POZİTİF_FİVE()
        self.SOL_POZİTİF_SİX()
        self.SOL_POZİTİF_SEVEN()

        self.SOL_NEGATİF_ONE()
        self.SOL_NEGATİF_TWO()
        self.SOL_NEGATİF_THREE()
        self.SOL_NEGATİF_FOUR()
        self.SOL_NEGATİF_FİVE()
        self.SOL_NEGATİF_SİX()
        self.SOL_NEGATİF_SEVEN()
        self.NET_SOLONA()
        self.Ekle()
    def Ekle(self):
        Coinler["SOLBUSD "] = round(float(self.SOLONA),1)
    def NET_SOLONA(self):
        SOLONA_NET = self.ONE_DAY_YUZDE + self.TWO_DAY_YUZDE + self.THREE_DAY_YUZDE + \
            self.FOUR_DAY_YUZDE + self.FİVE_DAY_YUZDE + self.SİX_DAY_YUZDE + \
            self.SEVEN_DAY_YUZDE
        self.SOLONA = SOLONA_NET
    def SOL_NEGATİF_ONE(self):
        ekle = 0.0
        close = self.ONE_DAY_CLOSE
        open = self.ONE_DAY_OPEN
        while True:
            value = (close * (ekle)) / 100
            if (float(close) + float(value)) >= float(open):
                self.ONE_DAY_YUZDE -= float(ekle)
                break
            else:
                ekle += 0.005
    def SOL_NEGATİF_TWO(self):
        ekle = 0.0
        close = self.TWO_DAY_CLOSE
        open = self.TWO_DAY_OPEN
        while True:
            value = (close * (ekle)) / 100
            if (float(close) + float(value)) >= float(open):
                self.TWO_DAY_YUZDE -= float(ekle)
                break
            else:
                ekle += 0.005
    def SOL_NEGATİF_THREE(self):
        ekle = 0.0
        close = self.THREE_DAY_CLOSE
        open = self.THREE_DAY_OPEN
        while True:
            value = (close * (ekle)) / 100
            if (float(close) + float(value)) >= float(open):
                self.THREE_DAY_YUZDE -= float(ekle)
                break
            else:
                ekle += 0.005
    def SOL_NEGATİF_FOUR(self):
        ekle = 0.0
        close = self.FOUR_DAY_CLOSE
        open = self.FOUR_DAY_OPEN
        while True:
            value = (close * (ekle)) / 100
            if (float(close) + float(value)) >= float(open):
                self.FOUR_DAY_YUZDE -= float(ekle)
                break
            else:
                ekle += 0.005
    def SOL_NEGATİF_FİVE(self):
        ekle = 0.0
        close = self.FİVE_DAY_CLOSE
        open = self.FİVE_DAY_OPEN
        while True:
            value = (close * (ekle)) / 100
            if (float(close) + float(value)) >= float(open):
                self.FİVE_DAY_YUZDE -= float(ekle)
                break
            else:
                ekle += 0.005
    def SOL_NEGATİF_SİX(self):
        ekle = 0.0
        close = self.SİX_DAY_CLOSE
        open = self.SİX_DAY_OPEN
        while True:
            value = (close * (ekle)) / 100
            if (float(close) + float(value)) >= float(open):
                self.SİX_DAY_YUZDE -= float(ekle)
                break
            else:
                ekle += 0.005
    def SOL_NEGATİF_SEVEN(self):
        ekle = 0.0
        close = self.SEVEN_DAY_CLOSE
        open = self.SEVEN_DAY_OPEN
        while True:
            value = (close * (ekle)) / 100
            if (float(close) + float(value)) >= float(open):
                self.SEVEN_DAY_YUZDE -= float(ekle)
                break
            else:
                ekle += 0.005


    def SOL_POZİTİF_ONE(self):
        ekle = 0.0
        close = self.ONE_DAY_CLOSE
        open = self.ONE_DAY_OPEN
        while True:
            value = (open * (ekle)) / 100
            if (float(open) + float(value)) >= float(close):
                self.ONE_DAY_YUZDE += float(ekle)
                break
            else:
                ekle += 0.005
    def SOL_POZİTİF_TWO(self):
        ekle = 0.0
        close = self.TWO_DAY_CLOSE
        open = self.TWO_DAY_OPEN
        while True:
            value = (open * (ekle)) / 100
            if (float(open) + float(value)) >= float(close):
                self.TWO_DAY_YUZDE += float(ekle)
                break
            else:
                ekle += 0.005
    def SOL_POZİTİF_THREE(self):
        ekle = 0.0
        close = self.THREE_DAY_CLOSE
        open = self.THREE_DAY_OPEN
        while True:
            value = (open * (ekle)) / 100
            if (float(open) + float(value)) >= float(close):
                self.THREE_DAY_YUZDE += float(ekle)
                break
            else:
                ekle += 0.005
    def SOL_POZİTİF_FOUR(self):
        ekle = 0.0
        close = self.FOUR_DAY_CLOSE
        open = self.FOUR_DAY_OPEN
        while True:
            value = (open * (ekle)) / 100
            if (float(open) + float(value)) >= float(close):
                self.FOUR_DAY_YUZDE += float(ekle)
                break
            else:
                ekle += 0.005
    def SOL_POZİTİF_FİVE(self):
        ekle = 0.0
        close = self.FİVE_DAY_CLOSE
        open = self.FİVE_DAY_OPEN
        while True:
            value = (open * (ekle)) / 100
            if (float(open) + float(value)) >= float(close):
                self.FİVE_DAY_YUZDE += float(ekle)
                break
            else:
                ekle += 0.005
    def SOL_POZİTİF_SİX(self):
        ekle = 0.0
        close = self.SİX_DAY_CLOSE
        open = self.SİX_DAY_OPEN
        while True:
            value = (open * (ekle)) / 100
            if (float(open) + float(value)) >= float(close):
                self.SİX_DAY_YUZDE += float(ekle)
                break
            else:
                ekle += 0.005
    def SOL_POZİTİF_SEVEN(self):
        ekle = 0.0
        close = self.SEVEN_DAY_CLOSE
        open = self.SEVEN_DAY_OPEN
        while True:
            value = (open * (ekle)) / 100
            if (float(open) + float(value)) >= float(close):
                self.SEVEN_DAY_YUZDE += float(ekle)
                break
            else:
                ekle += 0.005
class Link():
    def __init__(self):
        self.LINK = float

        self.ONE_DAY_YUZDE = 0
        self.TWO_DAY_YUZDE = 0
        self.THREE_DAY_YUZDE = 0
        self.FOUR_DAY_YUZDE = 0
        self.FİVE_DAY_YUZDE = 0
        self.SİX_DAY_YUZDE = 0
        self.SEVEN_DAY_YUZDE = 0

        self.ONE_DAY_CLOSE = lınk_one_day_close
        self.TWO_DAY_CLOSE = lınk_two_day_close
        self.THREE_DAY_CLOSE = lınk_three_day_close
        self.FOUR_DAY_CLOSE = lınk_four_day_close
        self.FİVE_DAY_CLOSE = lınk_five_day_close
        self.SİX_DAY_CLOSE = lınk_six_day_close
        self.SEVEN_DAY_CLOSE = lınk_seven_day_close

        self.ONE_DAY_OPEN = lınk_one_day_open
        self.TWO_DAY_OPEN = lınk_two_day_open
        self.THREE_DAY_OPEN = lınk_three_day_open
        self.FOUR_DAY_OPEN = lınk_four_day_open
        self.FİVE_DAY_OPEN = lınk_five_day_open
        self.SİX_DAY_OPEN = lınk_six_day_open
        self.SEVEN_DAY_OPEN = lınk_seven_day_open

        self.LINK_POZİTİF_ONE()
        self.LINK_POZİTİF_TWO()
        self.LINK_POZİTİF_THREE()
        self.LINK_POZİTİF_FOUR()
        self.LINK_POZİTİF_FİVE()
        self.LINK_POZİTİF_SİX()
        self.LINK_POZİTİF_SEVEN()

        self.LINK_NEGATİF_ONE()
        self.LINK_NEGATİF_TWO()
        self.LINK_NEGATİF_THREE()
        self.LINK_NEGATİF_FOUR()
        self.LINK_NEGATİF_FİVE()
        self.LINK_NEGATİF_SİX()
        self.LINK_NEGATİF_SEVEN()
        self.NET_LINK()
        self.Ekle()
    def Ekle(self):
        Coinler["LINKBUSD "] = round(float(self.LINK),1)
    def NET_LINK(self):
        LINK_NET = self.ONE_DAY_YUZDE + self.TWO_DAY_YUZDE + self.THREE_DAY_YUZDE + \
            self.FOUR_DAY_YUZDE + self.FİVE_DAY_YUZDE + self.SİX_DAY_YUZDE + \
            self.SEVEN_DAY_YUZDE
        self.LINK = LINK_NET
    def LINK_NEGATİF_ONE(self):
        ekle = 0.0
        close = self.ONE_DAY_CLOSE
        open = self.ONE_DAY_OPEN
        while True:
            value = (close * (ekle)) / 100
            if (int(close) + float(value)) >= int(open):
                self.ONE_DAY_YUZDE -= float(ekle)
                break
            else:
                ekle += 0.005
    def LINK_NEGATİF_TWO(self):
        ekle = 0.0
        close = self.TWO_DAY_CLOSE
        open = self.TWO_DAY_OPEN
        while True:
            value = (close * (ekle)) / 100
            if (int(close) + float(value)) >= int(open):
                self.TWO_DAY_YUZDE -= float(ekle)
                break
            else:
                ekle += 0.005
    def LINK_NEGATİF_THREE(self):
        ekle = 0.0
        close = self.THREE_DAY_CLOSE
        open = self.THREE_DAY_OPEN
        while True:
            value = (close * (ekle)) / 100
            if (int(close) + float(value)) >= int(open):
                self.THREE_DAY_YUZDE -= float(ekle)
                break
            else:
                ekle += 0.005
    def LINK_NEGATİF_FOUR(self):
        ekle = 0.0
        close = self.FOUR_DAY_CLOSE
        open = self.FOUR_DAY_OPEN
        while True:
            value = (close * (ekle)) / 100
            if (int(close) + float(value)) >= int(open):
                self.FOUR_DAY_YUZDE -= float(ekle)
                break
            else:
                ekle += 0.005
    def LINK_NEGATİF_FİVE(self):
        ekle = 0.0
        close = self.FİVE_DAY_CLOSE
        open = self.FİVE_DAY_OPEN
        while True:
            value = (close * (ekle)) / 100
            if (int(close) + float(value)) >= int(open):
                self.FİVE_DAY_YUZDE -= float(ekle)
                break
            else:
                ekle += 0.005
    def LINK_NEGATİF_SİX(self):
        ekle = 0.0
        close = self.SİX_DAY_CLOSE
        open = self.SİX_DAY_OPEN
        while True:
            value = (close * (ekle)) / 100
            if (int(close) + float(value)) >= int(open):
                self.SİX_DAY_YUZDE -= float(ekle)
                break
            else:
                ekle += 0.005
    def LINK_NEGATİF_SEVEN(self):
        ekle = 0.0
        close = self.SEVEN_DAY_CLOSE
        open = self.SEVEN_DAY_OPEN
        while True:
            value = (close * (ekle)) / 100
            if (int(close) + float(value)) >= int(open):
                self.SEVEN_DAY_YUZDE -= float(ekle)
                break
            else:
                ekle += 0.005


    def LINK_POZİTİF_ONE(self):
        ekle = 0.0
        close = self.ONE_DAY_CLOSE
        open = self.ONE_DAY_OPEN
        while True:
            value = (open * (ekle)) / 100
            if (int(open) + float(value)) >= int(close):
                self.ONE_DAY_YUZDE += float(ekle)
                break
            else:
                ekle += 0.005
    def LINK_POZİTİF_TWO(self):
        ekle = 0.0
        close = self.TWO_DAY_CLOSE
        open = self.TWO_DAY_OPEN
        while True:
            value = (open * (ekle)) / 100
            if (int(open) + float(value)) >= int(close):
                self.TWO_DAY_YUZDE += float(ekle)
                break
            else:
                ekle += 0.005
    def LINK_POZİTİF_THREE(self):
        ekle = 0.0
        close = self.THREE_DAY_CLOSE
        open = self.THREE_DAY_OPEN
        while True:
            value = (open * (ekle)) / 100
            if (int(open) + float(value)) >= int(close):
                self.THREE_DAY_YUZDE += float(ekle)
                break
            else:
                ekle += 0.005
    def LINK_POZİTİF_FOUR(self):
        ekle = 0.0
        close = self.FOUR_DAY_CLOSE
        open = self.FOUR_DAY_OPEN
        while True:
            value = (open * (ekle)) / 100
            if (int(open) + float(value)) >= int(close):
                self.FOUR_DAY_YUZDE += float(ekle)
                break
            else:
                ekle += 0.005
    def LINK_POZİTİF_FİVE(self):
        ekle = 0.0
        close = self.FİVE_DAY_CLOSE
        open = self.FİVE_DAY_OPEN
        while True:
            value = (open * (ekle)) / 100
            if (int(open) + float(value)) >= int(close):
                self.FİVE_DAY_YUZDE += float(ekle)
                break
            else:
                ekle += 0.005
    def LINK_POZİTİF_SİX(self):
        ekle = 0.0
        close = self.SİX_DAY_CLOSE
        open = self.SİX_DAY_OPEN
        while True:
            value = (open * (ekle)) / 100
            if (int(open) + float(value)) >= int(close):
                self.SİX_DAY_YUZDE += float(ekle)
                break
            else:
                ekle += 0.005
    def LINK_POZİTİF_SEVEN(self):
        ekle = 0.0
        close = self.SEVEN_DAY_CLOSE
        open = self.SEVEN_DAY_OPEN
        while True:
            value = (open * (ekle)) / 100
            if (int(open) + float(value)) >= int(close):
                self.SEVEN_DAY_YUZDE += float(ekle)
                break
            else:
                ekle += 0.005
class Dot():
    def __init__(self):
        self.DOT = float

        self.ONE_DAY_YUZDE = 0
        self.TWO_DAY_YUZDE = 0
        self.THREE_DAY_YUZDE = 0
        self.FOUR_DAY_YUZDE = 0
        self.FİVE_DAY_YUZDE = 0
        self.SİX_DAY_YUZDE = 0
        self.SEVEN_DAY_YUZDE = 0

        self.ONE_DAY_CLOSE = dot_one_day_close
        self.TWO_DAY_CLOSE = dot_two_day_close
        self.THREE_DAY_CLOSE = dot_three_day_close
        self.FOUR_DAY_CLOSE = dot_four_day_close
        self.FİVE_DAY_CLOSE = dot_five_day_close
        self.SİX_DAY_CLOSE = dot_six_day_close
        self.SEVEN_DAY_CLOSE = dot_seven_day_close

        self.ONE_DAY_OPEN = dot_one_day_open
        self.TWO_DAY_OPEN = dot_two_day_open
        self.THREE_DAY_OPEN = dot_three_day_open
        self.FOUR_DAY_OPEN = dot_four_day_open
        self.FİVE_DAY_OPEN = dot_five_day_open
        self.SİX_DAY_OPEN = dot_six_day_open
        self.SEVEN_DAY_OPEN = dot_seven_day_open

        self.DOT_POZİTİF_ONE()
        self.DOT_POZİTİF_TWO()
        self.DOT_POZİTİF_THREE()
        self.DOT_POZİTİF_FOUR()
        self.DOT_POZİTİF_FİVE()
        self.DOT_POZİTİF_SİX()
        self.DOT_POZİTİF_SEVEN()

        self.DOT_NEGATİF_ONE()
        self.DOT_NEGATİF_TWO()
        self.DOT_NEGATİF_THREE()
        self.DOT_NEGATİF_FOUR()
        self.DOT_NEGATİF_FİVE()
        self.DOT_NEGATİF_SİX()
        self.DOT_NEGATİF_SEVEN()
        self.NET_DOT()
        self.Ekle()
    def Ekle(self):
        Coinler["DOTBUSD "] = round(float(self.DOT),1)
    def NET_DOT(self):
        DOT_NET = self.ONE_DAY_YUZDE + self.TWO_DAY_YUZDE + self.THREE_DAY_YUZDE + \
            self.FOUR_DAY_YUZDE + self.FİVE_DAY_YUZDE + self.SİX_DAY_YUZDE + \
            self.SEVEN_DAY_YUZDE
        self.DOT = DOT_NET
    def DOT_NEGATİF_ONE(self):
        ekle = 0.0
        close = self.ONE_DAY_CLOSE
        open = self.ONE_DAY_OPEN
        while True:
            value = (close * (ekle)) / 100
            if (int(close) + float(value)) >= int(open):
                self.ONE_DAY_YUZDE -= float(ekle)
                break
            else:
                ekle += 0.005
    def DOT_NEGATİF_TWO(self):
        ekle = 0.0
        close = self.TWO_DAY_CLOSE
        open = self.TWO_DAY_OPEN
        while True:
            value = (close * (ekle)) / 100
            if (int(close) + float(value)) >= int(open):
                self.TWO_DAY_YUZDE -= float(ekle)
                break
            else:
                ekle += 0.005
    def DOT_NEGATİF_THREE(self):
        ekle = 0.0
        close = self.THREE_DAY_CLOSE
        open = self.THREE_DAY_OPEN
        while True:
            value = (close * (ekle)) / 100
            if (int(close) + float(value)) >= int(open):
                self.THREE_DAY_YUZDE -= float(ekle)
                break
            else:
                ekle += 0.005
    def DOT_NEGATİF_FOUR(self):
        ekle = 0.0
        close = self.FOUR_DAY_CLOSE
        open = self.FOUR_DAY_OPEN
        while True:
            value = (close * (ekle)) / 100
            if (int(close) + float(value)) >= int(open):
                self.FOUR_DAY_YUZDE -= float(ekle)
                break
            else:
                ekle += 0.005
    def DOT_NEGATİF_FİVE(self):
        ekle = 0.0
        close = self.FİVE_DAY_CLOSE
        open = self.FİVE_DAY_OPEN
        while True:
            value = (close * (ekle)) / 100
            if (int(close) + float(value)) >= int(open):
                self.FİVE_DAY_YUZDE -= float(ekle)
                break
            else:
                ekle += 0.005
    def DOT_NEGATİF_SİX(self):
        ekle = 0.0
        close = self.SİX_DAY_CLOSE
        open = self.SİX_DAY_OPEN
        while True:
            value = (close * (ekle)) / 100
            if (int(close) + float(value)) >= int(open):
                self.SİX_DAY_YUZDE -= float(ekle)
                break
            else:
                ekle += 0.005
    def DOT_NEGATİF_SEVEN(self):
        ekle = 0.0
        close = self.SEVEN_DAY_CLOSE
        open = self.SEVEN_DAY_OPEN
        while True:
            value = (close * (ekle)) / 100
            if (int(close) + float(value)) >= int(open):
                self.SEVEN_DAY_YUZDE -= float(ekle)
                break
            else:
                ekle += 0.005

    def DOT_POZİTİF_ONE(self):
        ekle = 0.0
        close = self.ONE_DAY_CLOSE
        open = self.ONE_DAY_OPEN
        while True:
            value = (open * (ekle)) / 100
            if (int(open) + float(value)) >= int(close):
                self.ONE_DAY_YUZDE += float(ekle)
                break
            else:
                ekle += 0.005
    def DOT_POZİTİF_TWO(self):
        ekle = 0.0
        close = self.TWO_DAY_CLOSE
        open = self.TWO_DAY_OPEN
        while True:
            value = (open * (ekle)) / 100
            if (int(open) + float(value)) >= int(close):
                self.TWO_DAY_YUZDE += float(ekle)
                break
            else:
                ekle += 0.005
    def DOT_POZİTİF_THREE(self):
        ekle = 0.0
        close = self.THREE_DAY_CLOSE
        open = self.THREE_DAY_OPEN
        while True:
            value = (open * (ekle)) / 100
            if (int(open) + float(value)) >= int(close):
                self.THREE_DAY_YUZDE += float(ekle)
                break
            else:
                ekle += 0.005
    def DOT_POZİTİF_FOUR(self):
        ekle = 0.0
        close = self.FOUR_DAY_CLOSE
        open = self.FOUR_DAY_OPEN
        while True:
            value = (open * (ekle)) / 100
            if (int(open) + float(value)) >= int(close):
                self.FOUR_DAY_YUZDE += float(ekle)
                break
            else:
                ekle += 0.005
    def DOT_POZİTİF_FİVE(self):
        ekle = 0.0
        close = self.FİVE_DAY_CLOSE
        open = self.FİVE_DAY_OPEN
        while True:
            value = (open * (ekle)) / 100
            if (int(open) + float(value)) >= int(close):
                self.FİVE_DAY_YUZDE += float(ekle)
                break
            else:
                ekle += 0.005
    def DOT_POZİTİF_SİX(self):
        ekle = 0.0
        close = self.SİX_DAY_CLOSE
        open = self.SİX_DAY_OPEN
        while True:
            value = (open * (ekle)) / 100
            if (int(open) + float(value)) >= int(close):
                self.SİX_DAY_YUZDE += float(ekle)
                break
            else:
                ekle += 0.005
    def DOT_POZİTİF_SEVEN(self):
        ekle = 0.0
        close = self.SEVEN_DAY_CLOSE
        open = self.SEVEN_DAY_OPEN
        while True:
            value = (open * (ekle)) / 100
            if (int(open) + float(value)) >= int(close):
                self.SEVEN_DAY_YUZDE += float(ekle)
                break
            else:
                ekle += 0.005
class Ada():
    def __init__(self):
        self.ADA = float

        self.ONE_DAY_YUZDE = 0
        self.TWO_DAY_YUZDE = 0
        self.THREE_DAY_YUZDE = 0
        self.FOUR_DAY_YUZDE = 0
        self.FİVE_DAY_YUZDE = 0
        self.SİX_DAY_YUZDE = 0
        self.SEVEN_DAY_YUZDE = 0

        self.ONE_DAY_CLOSE = ada_one_day_close
        self.TWO_DAY_CLOSE = ada_two_day_close
        self.THREE_DAY_CLOSE = ada_three_day_close
        self.FOUR_DAY_CLOSE = ada_four_day_close
        self.FİVE_DAY_CLOSE = ada_five_day_close
        self.SİX_DAY_CLOSE = ada_six_day_close
        self.SEVEN_DAY_CLOSE = ada_seven_day_close

        self.ONE_DAY_OPEN = ada_one_day_open
        self.TWO_DAY_OPEN = ada_two_day_open
        self.THREE_DAY_OPEN = ada_three_day_open
        self.FOUR_DAY_OPEN = ada_four_day_open
        self.FİVE_DAY_OPEN = ada_five_day_open
        self.SİX_DAY_OPEN = ada_six_day_open
        self.SEVEN_DAY_OPEN = ada_seven_day_open

        self.ADA_POZİTİF_ONE()
        self.ADA_POZİTİF_TWO()
        self.ADA_POZİTİF_THREE()
        self.ADA_POZİTİF_FOUR()
        self.ADA_POZİTİF_FİVE()
        self.ADA_POZİTİF_SİX()
        self.ADA_POZİTİF_SEVEN()

        self.ADA_NEGATİF_ONE()
        self.ADA_NEGATİF_TWO()
        self.ADA_NEGATİF_THREE()
        self.ADA_NEGATİF_FOUR()
        self.ADA_NEGATİF_FİVE()
        self.ADA_NEGATİF_SİX()
        self.ADA_NEGATİF_SEVEN()
        self.NET_ADA()
        self.Ekle()
    def Ekle(self):
        Coinler["ADABUSD "] = round(float(self.ADA),1)
    def NET_ADA(self):
        ADA_NET = self.ONE_DAY_YUZDE + self.TWO_DAY_YUZDE + self.THREE_DAY_YUZDE + \
            self.FOUR_DAY_YUZDE + self.FİVE_DAY_YUZDE + self.SİX_DAY_YUZDE + \
            self.SEVEN_DAY_YUZDE
        self.ADA = ADA_NET
    def ADA_NEGATİF_ONE(self):
        ekle = 0.0
        close = self.ONE_DAY_CLOSE
        open = self.ONE_DAY_OPEN
        while True:
            value = (close * (ekle)) / 100
            if (float(close) + float(value)) >= float(open):
                self.ONE_DAY_YUZDE -= float(ekle)
                break
            else:
                ekle += 0.005
    def ADA_NEGATİF_TWO(self):
        ekle = 0.0
        close = self.TWO_DAY_CLOSE
        open = self.TWO_DAY_OPEN
        while True:
            value = (close * (ekle)) / 100
            if (float(close) + float(value)) >= float(open):
                self.TWO_DAY_YUZDE -= float(ekle)
                break
            else:
                ekle += 0.005
    def ADA_NEGATİF_THREE(self):
        ekle = 0.0
        close = self.THREE_DAY_CLOSE
        open = self.THREE_DAY_OPEN
        while True:
            value = (close * (ekle)) / 100
            if (float(close) + float(value)) >= float(open):
                self.THREE_DAY_YUZDE -= float(ekle)
                break
            else:
                ekle += 0.005
    def ADA_NEGATİF_FOUR(self):
        ekle = 0.0
        close = self.FOUR_DAY_CLOSE
        open = self.FOUR_DAY_OPEN
        while True:
            value = (close * (ekle)) / 100
            if (float(close) + float(value)) >= float(open):
                self.FOUR_DAY_YUZDE -= float(ekle)
                break
            else:
                ekle += 0.005
    def ADA_NEGATİF_FİVE(self):
        ekle = 0.0
        close = self.FİVE_DAY_CLOSE
        open = self.FİVE_DAY_OPEN
        while True:
            value = (close * (ekle)) / 100
            if (float(close) + float(value)) >= float(open):
                self.FİVE_DAY_YUZDE -= float(ekle)
                break
            else:
                ekle += 0.005
    def ADA_NEGATİF_SİX(self):
        ekle = 0.0
        close = self.SİX_DAY_CLOSE
        open = self.SİX_DAY_OPEN
        while True:
            value = (close * (ekle)) / 100
            if (float(close) + float(value)) >= float(open):
                self.SİX_DAY_YUZDE -= float(ekle)
                break
            else:
                ekle += 0.005
    def ADA_NEGATİF_SEVEN(self):
        ekle = 0.0
        close = self.SEVEN_DAY_CLOSE
        open = self.SEVEN_DAY_OPEN
        while True:
            value = (close * (ekle)) / 100
            if (float(close) + float(value)) >= float(open):
                self.SEVEN_DAY_YUZDE -= float(ekle)
                break
            else:
                ekle += 0.005
    def ADA_POZİTİF_ONE(self):
        ekle = 0.0
        close = self.ONE_DAY_CLOSE
        open = self.ONE_DAY_OPEN
        while True:
            value = (open * (ekle)) / 100
            if (float(open) + float(value)) >= float(close):
                self.ONE_DAY_YUZDE += float(ekle)
                break
            else:
                ekle += 0.005
    def ADA_POZİTİF_TWO(self):
        ekle = 0.0
        close = self.TWO_DAY_CLOSE
        open = self.TWO_DAY_OPEN
        while True:
            value = (open * (ekle)) / 100
            if (float(open) + float(value)) >= float(close):
                self.TWO_DAY_YUZDE += float(ekle)
                break
            else:
                ekle += 0.005
    def ADA_POZİTİF_THREE(self):
        ekle = 0.0
        close = self.THREE_DAY_CLOSE
        open = self.THREE_DAY_OPEN
        while True:
            value = (open * (ekle)) / 100
            if (float(open) + float(value)) >= float(close):
                self.THREE_DAY_YUZDE += float(ekle)
                break
            else:
                ekle += 0.005
    def ADA_POZİTİF_FOUR(self):
        ekle = 0.0
        close = self.FOUR_DAY_CLOSE
        open = self.FOUR_DAY_OPEN
        while True:
            value = (open * (ekle)) / 100
            if (float(open) + float(value)) >= float(close):
                self.FOUR_DAY_YUZDE += float(ekle)
                break
            else:
                ekle += 0.005
    def ADA_POZİTİF_FİVE(self):
        ekle = 0.0
        close = self.FİVE_DAY_CLOSE
        open = self.FİVE_DAY_OPEN
        while True:
            value = (open * (ekle)) / 100
            if (float(open) + float(value)) >= float(close):
                self.FİVE_DAY_YUZDE += float(ekle)
                break
            else:
                ekle += 0.005
    def ADA_POZİTİF_SİX(self):
        ekle = 0.0
        close = self.SİX_DAY_CLOSE
        open = self.SİX_DAY_OPEN
        while True:
            value = (open * (ekle)) / 100
            if (float(open) + float(value)) >= float(close):
                self.SİX_DAY_YUZDE += float(ekle)
                break
            else:
                ekle += 0.005
    def ADA_POZİTİF_SEVEN(self):
        ekle = 0.0
        close = self.SEVEN_DAY_CLOSE
        open = self.SEVEN_DAY_OPEN
        while True:
            value = (open * (ekle)) / 100
            if (float(open) + float(value)) >= float(close):
                self.SEVEN_DAY_YUZDE += float(ekle)
                break
            else:
                ekle += 0.005
class Mana():
    def __init__(self):
        self.MANA = float

        self.ONE_DAY_YUZDE = 0
        self.TWO_DAY_YUZDE = 0
        self.THREE_DAY_YUZDE = 0
        self.FOUR_DAY_YUZDE = 0
        self.FİVE_DAY_YUZDE = 0
        self.SİX_DAY_YUZDE = 0
        self.SEVEN_DAY_YUZDE = 0

        self.ONE_DAY_CLOSE = mana_one_day_close
        self.TWO_DAY_CLOSE = mana_two_day_close
        self.THREE_DAY_CLOSE = mana_three_day_close
        self.FOUR_DAY_CLOSE = mana_four_day_close
        self.FİVE_DAY_CLOSE = mana_five_day_close
        self.SİX_DAY_CLOSE = mana_six_day_close
        self.SEVEN_DAY_CLOSE = mana_seven_day_close

        self.ONE_DAY_OPEN = mana_one_day_open
        self.TWO_DAY_OPEN = mana_two_day_open
        self.THREE_DAY_OPEN = mana_three_day_open
        self.FOUR_DAY_OPEN = mana_four_day_open
        self.FİVE_DAY_OPEN = mana_five_day_open
        self.SİX_DAY_OPEN = mana_six_day_open
        self.SEVEN_DAY_OPEN = mana_seven_day_open

        self.MANA_POZİTİF_ONE()
        self.MANA_POZİTİF_TWO()
        self.MANA_POZİTİF_THREE()
        self.MANA_POZİTİF_FOUR()
        self.MANA_POZİTİF_FİVE()
        self.MANA_POZİTİF_SİX()
        self.MANA_POZİTİF_SEVEN()

        self.MANA_NEGATİF_ONE()
        self.MANA_NEGATİF_TWO()
        self.MANA_NEGATİF_THREE()
        self.MANA_NEGATİF_FOUR()
        self.MANA_NEGATİF_FİVE()
        self.MANA_NEGATİF_SİX()
        self.MANA_NEGATİF_SEVEN()
        self.NET_MANA()
        self.Ekle()
    def Ekle(self):
        Coinler["MANABUSD "] = round(float(self.MANA),1)
    def NET_MANA(self):
        MANA_NET = self.ONE_DAY_YUZDE + self.TWO_DAY_YUZDE + self.THREE_DAY_YUZDE + \
            self.FOUR_DAY_YUZDE + self.FİVE_DAY_YUZDE + self.SİX_DAY_YUZDE + \
            self.SEVEN_DAY_YUZDE
        self.MANA = MANA_NET
    def MANA_NEGATİF_ONE(self):
        ekle = 0.0
        close = self.ONE_DAY_CLOSE
        open = self.ONE_DAY_OPEN
        while True:
            value = (close * (ekle)) / 100
            if (int(close) + float(value)) >= int(open):
                self.ONE_DAY_YUZDE -= float(ekle)
                break
            else:
                ekle += 0.005
    def MANA_NEGATİF_TWO(self):
        ekle = 0.0
        close = self.TWO_DAY_CLOSE
        open = self.TWO_DAY_OPEN
        while True:
            value = (close * (ekle)) / 100
            if (int(close) + float(value)) >= int(open):
                self.TWO_DAY_YUZDE -= float(ekle)
                break
            else:
                ekle += 0.005
    def MANA_NEGATİF_THREE(self):
        ekle = 0.0
        close = self.THREE_DAY_CLOSE
        open = self.THREE_DAY_OPEN
        while True:
            value = (close * (ekle)) / 100
            if (int(close) + float(value)) >= int(open):
                self.THREE_DAY_YUZDE -= float(ekle)
                break
            else:
                ekle += 0.005
    def MANA_NEGATİF_FOUR(self):
        ekle = 0.0
        close = self.FOUR_DAY_CLOSE
        open = self.FOUR_DAY_OPEN
        while True:
            value = (close * (ekle)) / 100
            if (int(close) + float(value)) >= int(open):
                self.FOUR_DAY_YUZDE -= float(ekle)
                break
            else:
                ekle += 0.005
    def MANA_NEGATİF_FİVE(self):
        ekle = 0.0
        close = self.FİVE_DAY_CLOSE
        open = self.FİVE_DAY_OPEN
        while True:
            value = (close * (ekle)) / 100
            if (int(close) + float(value)) >= int(open):
                self.FİVE_DAY_YUZDE -= float(ekle)
                break
            else:
                ekle += 0.005
    def MANA_NEGATİF_SİX(self):
        ekle = 0.0
        close = self.SİX_DAY_CLOSE
        open = self.SİX_DAY_OPEN
        while True:
            value = (close * (ekle)) / 100
            if (int(close) + float(value)) >= int(open):
                self.SİX_DAY_YUZDE -= float(ekle)
                break
            else:
                ekle += 0.005
    def MANA_NEGATİF_SEVEN(self):
        ekle = 0.0
        close = self.SEVEN_DAY_CLOSE
        open = self.SEVEN_DAY_OPEN
        while True:
            value = (close * (ekle)) / 100
            if (int(close) + float(value)) >= int(open):
                self.SEVEN_DAY_YUZDE -= float(ekle)
                break
            else:
                ekle += 0.005

    def MANA_POZİTİF_ONE(self):
        ekle = 0.0
        close = self.ONE_DAY_CLOSE
        open = self.ONE_DAY_OPEN
        while True:
            value = (open * (ekle)) / 100
            if (int(open) + float(value)) >= int(close):
                self.ONE_DAY_YUZDE += float(ekle)
                break
            else:
                ekle += 0.005
    def MANA_POZİTİF_TWO(self):
        ekle = 0.0
        close = self.TWO_DAY_CLOSE
        open = self.TWO_DAY_OPEN
        while True:
            value = (open * (ekle)) / 100
            if (int(open) + float(value)) >= int(close):
                self.TWO_DAY_YUZDE += float(ekle)
                break
            else:
                ekle += 0.005
    def MANA_POZİTİF_THREE(self):
        ekle = 0.0
        close = self.THREE_DAY_CLOSE
        open = self.THREE_DAY_OPEN
        while True:
            value = (open * (ekle)) / 100
            if (int(open) + float(value)) >= int(close):
                self.THREE_DAY_YUZDE += float(ekle)
                break
            else:
                ekle += 0.005
    def MANA_POZİTİF_FOUR(self):
        ekle = 0.0
        close = self.FOUR_DAY_CLOSE
        open = self.FOUR_DAY_OPEN
        while True:
            value = (open * (ekle)) / 100
            if (int(open) + float(value)) >= int(close):
                self.FOUR_DAY_YUZDE += float(ekle)
                break
            else:
                ekle += 0.005
    def MANA_POZİTİF_FİVE(self):
        ekle = 0.0
        close = self.FİVE_DAY_CLOSE
        open = self.FİVE_DAY_OPEN
        while True:
            value = (open * (ekle)) / 100
            if (int(open) + float(value)) >= int(close):
                self.FİVE_DAY_YUZDE += float(ekle)
                break
            else:
                ekle += 0.005
    def MANA_POZİTİF_SİX(self):
        ekle = 0.0
        close = self.SİX_DAY_CLOSE
        open = self.SİX_DAY_OPEN
        while True:
            value = (open * (ekle)) / 100
            if (int(open) + float(value)) >= int(close):
                self.SİX_DAY_YUZDE += float(ekle)
                break
            else:
                ekle += 0.005
    def MANA_POZİTİF_SEVEN(self):
        ekle = 0.0
        close = self.SEVEN_DAY_CLOSE
        open = self.SEVEN_DAY_OPEN
        while True:
            value = (open * (ekle)) / 100
            if (int(open) + float(value)) >= int(close):
                self.SEVEN_DAY_YUZDE += float(ekle)
                break
            else:
                ekle += 0.005
class Enjin():
    def __init__(self):
        self.ENJIN = float

        self.ONE_DAY_YUZDE = 0
        self.TWO_DAY_YUZDE = 0
        self.THREE_DAY_YUZDE = 0
        self.FOUR_DAY_YUZDE = 0
        self.FİVE_DAY_YUZDE = 0
        self.SİX_DAY_YUZDE = 0
        self.SEVEN_DAY_YUZDE = 0

        self.ONE_DAY_CLOSE = enjin_one_day_close
        self.TWO_DAY_CLOSE = enjin_two_day_close
        self.THREE_DAY_CLOSE = enjin_three_day_close
        self.FOUR_DAY_CLOSE = enjin_four_day_close
        self.FİVE_DAY_CLOSE = enjin_five_day_close
        self.SİX_DAY_CLOSE = enjin_six_day_close
        self.SEVEN_DAY_CLOSE = enjin_seven_day_close

        self.ONE_DAY_OPEN = enjin_one_day_open
        self.TWO_DAY_OPEN = enjin_two_day_open
        self.THREE_DAY_OPEN = enjin_three_day_open
        self.FOUR_DAY_OPEN = enjin_four_day_open
        self.FİVE_DAY_OPEN = enjin_five_day_open
        self.SİX_DAY_OPEN = enjin_six_day_open
        self.SEVEN_DAY_OPEN = enjin_seven_day_open

        self.ENJIN_POZİTİF_ONE()
        self.ENJIN_POZİTİF_TWO()
        self.ENJIN_POZİTİF_THREE()
        self.ENJIN_POZİTİF_FOUR()
        self.ENJIN_POZİTİF_FİVE()
        self.ENJIN_POZİTİF_SİX()
        self.ENJIN_POZİTİF_SEVEN()

        self.ENJIN_NEGATİF_ONE()
        self.ENJIN_NEGATİF_TWO()
        self.ENJIN_NEGATİF_THREE()
        self.ENJIN_NEGATİF_FOUR()
        self.ENJIN_NEGATİF_FİVE()
        self.ENJIN_NEGATİF_SİX()
        self.ENJIN_NEGATİF_SEVEN()
        self.NET_ENJIN()
        self.Ekle()
    def Ekle(self):
        Coinler["ENJBUSD "] = round(float(self.ENJIN),1)
    def NET_ENJIN(self):
        ENJIN_NET = self.ONE_DAY_YUZDE + self.TWO_DAY_YUZDE + self.THREE_DAY_YUZDE + \
            self.FOUR_DAY_YUZDE + self.FİVE_DAY_YUZDE + self.SİX_DAY_YUZDE + \
            self.SEVEN_DAY_YUZDE
        self.ENJIN = ENJIN_NET
    def ENJIN_NEGATİF_ONE(self):
        ekle = 0.0
        close = self.ONE_DAY_CLOSE
        open = self.ONE_DAY_OPEN
        while True:
            value = (close * (ekle)) / 100
            if (int(close) + float(value)) >= int(open):
                self.ONE_DAY_YUZDE -= float(ekle)
                break
            else:
                ekle += 0.005
    def ENJIN_NEGATİF_TWO(self):
        ekle = 0.0
        close = self.TWO_DAY_CLOSE
        open = self.TWO_DAY_OPEN
        while True:
            value = (close * (ekle)) / 100
            if (int(close) + float(value)) >= int(open):
                self.TWO_DAY_YUZDE -= float(ekle)
                break
            else:
                ekle += 0.005
    def ENJIN_NEGATİF_THREE(self):
        ekle = 0.0
        close = self.THREE_DAY_CLOSE
        open = self.THREE_DAY_OPEN
        while True:
            value = (close * (ekle)) / 100
            if (int(close) + float(value)) >= int(open):
                self.THREE_DAY_YUZDE -= float(ekle)
                break
            else:
                ekle += 0.005
    def ENJIN_NEGATİF_FOUR(self):
        ekle = 0.0
        close = self.FOUR_DAY_CLOSE
        open = self.FOUR_DAY_OPEN
        while True:
            value = (close * (ekle)) / 100
            if (int(close) + float(value)) >= int(open):
                self.FOUR_DAY_YUZDE -= float(ekle)
                break
            else:
                ekle += 0.005
    def ENJIN_NEGATİF_FİVE(self):
        ekle = 0.0
        close = self.FİVE_DAY_CLOSE
        open = self.FİVE_DAY_OPEN
        while True:
            value = (close * (ekle)) / 100
            if (int(close) + float(value)) >= int(open):
                self.FİVE_DAY_YUZDE -= float(ekle)
                break
            else:
                ekle += 0.005
    def ENJIN_NEGATİF_SİX(self):
        ekle = 0.0
        close = self.SİX_DAY_CLOSE
        open = self.SİX_DAY_OPEN
        while True:
            value = (close * (ekle)) / 100
            if (int(close) + float(value)) >= int(open):
                self.SİX_DAY_YUZDE -= float(ekle)
                break
            else:
                ekle += 0.005
    def ENJIN_NEGATİF_SEVEN(self):
        ekle = 0.0
        close = self.SEVEN_DAY_CLOSE
        open = self.SEVEN_DAY_OPEN
        while True:
            value = (close * (ekle)) / 100
            if (int(close) + float(value)) >= int(open):
                self.SEVEN_DAY_YUZDE -= float(ekle)
                break
            else:
                ekle += 0.005

    def ENJIN_POZİTİF_ONE(self):
        ekle = 0.0
        close = self.ONE_DAY_CLOSE
        open = self.ONE_DAY_OPEN
        while True:
            value = (open * (ekle)) / 100
            if (int(open) + float(value)) >= int(close):
                self.ONE_DAY_YUZDE += float(ekle)
                break
            else:
                ekle += 0.005
    def ENJIN_POZİTİF_TWO(self):
        ekle = 0.0
        close = self.TWO_DAY_CLOSE
        open = self.TWO_DAY_OPEN
        while True:
            value = (open * (ekle)) / 100
            if (int(open) + float(value)) >= int(close):
                self.TWO_DAY_YUZDE += float(ekle)
                break
            else:
                ekle += 0.005
    def ENJIN_POZİTİF_THREE(self):
        ekle = 0.0
        close = self.THREE_DAY_CLOSE
        open = self.THREE_DAY_OPEN
        while True:
            value = (open * (ekle)) / 100
            if (int(open) + float(value)) >= int(close):
                self.THREE_DAY_YUZDE += float(ekle)
                break
            else:
                ekle += 0.005
    def ENJIN_POZİTİF_FOUR(self):
        ekle = 0.0
        close = self.FOUR_DAY_CLOSE
        open = self.FOUR_DAY_OPEN
        while True:
            value = (open * (ekle)) / 100
            if (int(open) + float(value)) >= int(close):
                self.FOUR_DAY_YUZDE += float(ekle)
                break
            else:
                ekle += 0.005
    def ENJIN_POZİTİF_FİVE(self):
        ekle = 0.0
        close = self.FİVE_DAY_CLOSE
        open = self.FİVE_DAY_OPEN
        while True:
            value = (open * (ekle)) / 100
            if (int(open) + float(value)) >= int(close):
                self.FİVE_DAY_YUZDE += float(ekle)
                break
            else:
                ekle += 0.005
    def ENJIN_POZİTİF_SİX(self):
        ekle = 0.0
        close = self.SİX_DAY_CLOSE
        open = self.SİX_DAY_OPEN
        while True:
            value = (open * (ekle)) / 100
            if (int(open) + float(value)) >= int(close):
                self.SİX_DAY_YUZDE += float(ekle)
                break
            else:
                ekle += 0.005
    def ENJIN_POZİTİF_SEVEN(self):
        ekle = 0.0
        close = self.SEVEN_DAY_CLOSE
        open = self.SEVEN_DAY_OPEN
        while True:
            value = (open * (ekle)) / 100
            if (int(open) + float(value)) >= int(close):
                self.SEVEN_DAY_YUZDE += float(ekle)
                break
            else:
                ekle += 0.005
class Avax():
    def __init__(self):
        self.AVAX = float

        self.ONE_DAY_YUZDE = 0
        self.TWO_DAY_YUZDE = 0
        self.THREE_DAY_YUZDE = 0
        self.FOUR_DAY_YUZDE = 0
        self.FİVE_DAY_YUZDE = 0
        self.SİX_DAY_YUZDE = 0
        self.SEVEN_DAY_YUZDE = 0

        self.ONE_DAY_CLOSE = avax_one_day_close
        self.TWO_DAY_CLOSE = avax_two_day_close
        self.THREE_DAY_CLOSE = avax_three_day_close
        self.FOUR_DAY_CLOSE = avax_four_day_close
        self.FİVE_DAY_CLOSE = avax_five_day_close
        self.SİX_DAY_CLOSE = avax_six_day_close
        self.SEVEN_DAY_CLOSE = avax_seven_day_close

        self.ONE_DAY_OPEN = avax_one_day_open
        self.TWO_DAY_OPEN = avax_two_day_open
        self.THREE_DAY_OPEN = avax_three_day_open
        self.FOUR_DAY_OPEN = avax_four_day_open
        self.FİVE_DAY_OPEN = avax_five_day_open
        self.SİX_DAY_OPEN = avax_six_day_open
        self.SEVEN_DAY_OPEN = avax_seven_day_open

        self.AVAX_POZİTİF_ONE()
        self.AVAX_POZİTİF_TWO()
        self.AVAX_POZİTİF_THREE()
        self.AVAX_POZİTİF_FOUR()
        self.AVAX_POZİTİF_FİVE()
        self.AVAX_POZİTİF_SİX()
        self.AVAX_POZİTİF_SEVEN()

        self.AVAX_NEGATİF_ONE()
        self.AVAX_NEGATİF_TWO()
        self.AVAX_NEGATİF_THREE()
        self.AVAX_NEGATİF_FOUR()
        self.AVAX_NEGATİF_FİVE()
        self.AVAX_NEGATİF_SİX()
        self.AVAX_NEGATİF_SEVEN()
        self.NET_AVAX()
        self.Ekle()
    def Ekle(self):
        Coinler["AVAXBUSD "] = round(float(self.AVAX),1)
    def NET_AVAX(self):
        AVAX_NET = self.ONE_DAY_YUZDE + self.TWO_DAY_YUZDE + self.THREE_DAY_YUZDE + \
            self.FOUR_DAY_YUZDE + self.FİVE_DAY_YUZDE + self.SİX_DAY_YUZDE + \
            self.SEVEN_DAY_YUZDE
        self.AVAX = AVAX_NET
    def AVAX_NEGATİF_ONE(self):
        ekle = 0.0
        close = self.ONE_DAY_CLOSE
        open = self.ONE_DAY_OPEN
        while True:
            value = (close * (ekle)) / 100
            if (int(close) + float(value)) >= int(open):
                self.ONE_DAY_YUZDE -= float(ekle)
                break
            else:
                ekle += 0.005
    def AVAX_NEGATİF_TWO(self):
        ekle = 0.0
        close = self.TWO_DAY_CLOSE
        open = self.TWO_DAY_OPEN
        while True:
            value = (close * (ekle)) / 100
            if (int(close) + float(value)) >= int(open):
                self.TWO_DAY_YUZDE -= float(ekle)
                break
            else:
                ekle += 0.005
    def AVAX_NEGATİF_THREE(self):
        ekle = 0.0
        close = self.THREE_DAY_CLOSE
        open = self.THREE_DAY_OPEN
        while True:
            value = (close * (ekle)) / 100
            if (int(close) + float(value)) >= int(open):
                self.THREE_DAY_YUZDE -= float(ekle)
                break
            else:
                ekle += 0.005
    def AVAX_NEGATİF_FOUR(self):
        ekle = 0.0
        close = self.FOUR_DAY_CLOSE
        open = self.FOUR_DAY_OPEN
        while True:
            value = (close * (ekle)) / 100
            if (int(close) + float(value)) >= int(open):
                self.FOUR_DAY_YUZDE -= float(ekle)
                break
            else:
                ekle += 0.005
    def AVAX_NEGATİF_FİVE(self):
        ekle = 0.0
        close = self.FİVE_DAY_CLOSE
        open = self.FİVE_DAY_OPEN
        while True:
            value = (close * (ekle)) / 100
            if (int(close) + float(value)) >= int(open):
                self.FİVE_DAY_YUZDE -= float(ekle)
                break
            else:
                ekle += 0.005
    def AVAX_NEGATİF_SİX(self):
        ekle = 0.0
        close = self.SİX_DAY_CLOSE
        open = self.SİX_DAY_OPEN
        while True:
            value = (close * (ekle)) / 100
            if (int(close) + float(value)) >= int(open):
                self.SİX_DAY_YUZDE -= float(ekle)
                break
            else:
                ekle += 0.005
    def AVAX_NEGATİF_SEVEN(self):
        ekle = 0.0
        close = self.SEVEN_DAY_CLOSE
        open = self.SEVEN_DAY_OPEN
        while True:
            value = (close * (ekle)) / 100
            if (int(close) + float(value)) >= int(open):
                self.SEVEN_DAY_YUZDE -= float(ekle)
                break
            else:
                ekle += 0.005

    def AVAX_POZİTİF_ONE(self):
        ekle = 0.0
        close = self.ONE_DAY_CLOSE
        open = self.ONE_DAY_OPEN
        while True:
            value = (open * (ekle)) / 100
            if (int(open) + float(value)) >= int(close):
                self.ONE_DAY_YUZDE += float(ekle)
                break
            else:
                ekle += 0.005
    def AVAX_POZİTİF_TWO(self):
        ekle = 0.0
        close = self.TWO_DAY_CLOSE
        open = self.TWO_DAY_OPEN
        while True:
            value = (open * (ekle)) / 100
            if (int(open) + float(value)) >= int(close):
                self.TWO_DAY_YUZDE += float(ekle)
                break
            else:
                ekle += 0.005
    def AVAX_POZİTİF_THREE(self):
        ekle = 0.0
        close = self.THREE_DAY_CLOSE
        open = self.THREE_DAY_OPEN
        while True:
            value = (open * (ekle)) / 100
            if (int(open) + float(value)) >= int(close):
                self.THREE_DAY_YUZDE += float(ekle)
                break
            else:
                ekle += 0.005
    def AVAX_POZİTİF_FOUR(self):
        ekle = 0.0
        close = self.FOUR_DAY_CLOSE
        open = self.FOUR_DAY_OPEN
        while True:
            value = (open * (ekle)) / 100
            if (int(open) + float(value)) >= int(close):
                self.FOUR_DAY_YUZDE += float(ekle)
                break
            else:
                ekle += 0.005
    def AVAX_POZİTİF_FİVE(self):
        ekle = 0.0
        close = self.FİVE_DAY_CLOSE
        open = self.FİVE_DAY_OPEN
        while True:
            value = (open * (ekle)) / 100
            if (int(open) + float(value)) >= int(close):
                self.FİVE_DAY_YUZDE += float(ekle)
                break
            else:
                ekle += 0.005
    def AVAX_POZİTİF_SİX(self):
        ekle = 0.0
        close = self.SİX_DAY_CLOSE
        open = self.SİX_DAY_OPEN
        while True:
            value = (open * (ekle)) / 100
            if (int(open) + float(value)) >= int(close):
                self.SİX_DAY_YUZDE += float(ekle)
                break
            else:
                ekle += 0.005
    def AVAX_POZİTİF_SEVEN(self):
        ekle = 0.0
        close = self.SEVEN_DAY_CLOSE
        open = self.SEVEN_DAY_OPEN
        while True:
            value = (open * (ekle)) / 100
            if (int(open) + float(value)) >= int(close):
                self.SEVEN_DAY_YUZDE += float(ekle)
                break
            else:
                ekle += 0.005
class Doge():
    def __init__(self):
        self.DOGE = float

        self.ONE_DAY_YUZDE = 0
        self.TWO_DAY_YUZDE = 0
        self.THREE_DAY_YUZDE = 0
        self.FOUR_DAY_YUZDE = 0
        self.FİVE_DAY_YUZDE = 0
        self.SİX_DAY_YUZDE = 0
        self.SEVEN_DAY_YUZDE = 0

        self.ONE_DAY_CLOSE = doge_one_day_close
        self.TWO_DAY_CLOSE = doge_two_day_close
        self.THREE_DAY_CLOSE = doge_three_day_close
        self.FOUR_DAY_CLOSE = doge_four_day_close
        self.FİVE_DAY_CLOSE = doge_five_day_close
        self.SİX_DAY_CLOSE = doge_six_day_close
        self.SEVEN_DAY_CLOSE = doge_seven_day_close

        self.ONE_DAY_OPEN = doge_one_day_open
        self.TWO_DAY_OPEN = doge_two_day_open
        self.THREE_DAY_OPEN = doge_three_day_open
        self.FOUR_DAY_OPEN = doge_four_day_open
        self.FİVE_DAY_OPEN = doge_five_day_open
        self.SİX_DAY_OPEN = doge_six_day_open
        self.SEVEN_DAY_OPEN = doge_seven_day_open

        self.DOGE_POZİTİF_ONE()
        self.DOGE_POZİTİF_TWO()
        self.DOGE_POZİTİF_THREE()
        self.DOGE_POZİTİF_FOUR()
        self.DOGE_POZİTİF_FİVE()
        self.DOGE_POZİTİF_SİX()
        self.DOGE_POZİTİF_SEVEN()

        self.DOGE_NEGATİF_ONE()
        self.DOGE_NEGATİF_TWO()
        self.DOGE_NEGATİF_THREE()
        self.DOGE_NEGATİF_FOUR()
        self.DOGE_NEGATİF_FİVE()
        self.DOGE_NEGATİF_SİX()
        self.DOGE_NEGATİF_SEVEN()
        self.NET_DOGE()
        self.Ekle()
    def Ekle(self):
        Coinler["DOGEBUSD "] = round(float(self.DOGE),1)
    def NET_DOGE(self):
        DOGE_NET = self.ONE_DAY_YUZDE + self.TWO_DAY_YUZDE + self.THREE_DAY_YUZDE + \
            self.FOUR_DAY_YUZDE + self.FİVE_DAY_YUZDE + self.SİX_DAY_YUZDE + \
            self.SEVEN_DAY_YUZDE
        self.DOGE = DOGE_NET
    def DOGE_NEGATİF_ONE(self):
        ekle = 0.0
        close = self.ONE_DAY_CLOSE
        open = self.ONE_DAY_OPEN
        while True:
            value = (close * (ekle)) / 100
            if (float(close) + float(value)) >= float(open):
                self.ONE_DAY_YUZDE -= float(ekle)
                break
            else:
                ekle += 0.005
    def DOGE_NEGATİF_TWO(self):
        ekle = 0.0
        close = self.TWO_DAY_CLOSE
        open = self.TWO_DAY_OPEN
        while True:
            value = (close * (ekle)) / 100
            if (float(close) + float(value)) >= float(open):
                self.TWO_DAY_YUZDE -= float(ekle)
                break
            else:
                ekle += 0.005
    def DOGE_NEGATİF_THREE(self):
        ekle = 0.0
        close = self.THREE_DAY_CLOSE
        open = self.THREE_DAY_OPEN
        while True:
            value = (close * (ekle)) / 100
            if (float(close) + float(value)) >= float(open):
                self.THREE_DAY_YUZDE -= float(ekle)
                break
            else:
                ekle += 0.005
    def DOGE_NEGATİF_FOUR(self):
        ekle = 0.0
        close = self.FOUR_DAY_CLOSE
        open = self.FOUR_DAY_OPEN
        while True:
            value = (close * (ekle)) / 100
            if (float(close) + float(value)) >= float(open):
                self.FOUR_DAY_YUZDE -= float(ekle)
                break
            else:
                ekle += 0.0005
    def DOGE_NEGATİF_FİVE(self):
        ekle = 0.0
        close = self.FİVE_DAY_CLOSE
        open = self.FİVE_DAY_OPEN
        while True:
            value = (close * (ekle)) / 100
            if (float(close) + float(value)) >= float(open):
                self.FİVE_DAY_YUZDE -= float(ekle)
                break
            else:
                ekle += 0.005
    def DOGE_NEGATİF_SİX(self):
        ekle = 0.0
        close = self.SİX_DAY_CLOSE
        open = self.SİX_DAY_OPEN
        while True:
            value = (close * (ekle)) / 100
            if (float(close) + float(value)) >= float(open):
                self.SİX_DAY_YUZDE -= float(ekle)
                break
            else:
                ekle += 0.005
    def DOGE_NEGATİF_SEVEN(self):
        ekle = 0.0
        close = self.SEVEN_DAY_CLOSE
        open = self.SEVEN_DAY_OPEN
        while True:
            value = (close * (ekle)) / 100
            if (float(close) + float(value)) >= float(open):
                self.SEVEN_DAY_YUZDE -= float(ekle)
                break
            else:
                ekle += 0.005

    def DOGE_POZİTİF_ONE(self):
        ekle = 0.0
        close = self.ONE_DAY_CLOSE
        open = self.ONE_DAY_OPEN
        while True:
            value = (open * (ekle)) / 100
            if (float(open) + float(value)) >= float(close):
                self.ONE_DAY_YUZDE += float(ekle)
                break
            else:
                ekle += 0.005
    def DOGE_POZİTİF_TWO(self):
        ekle = 0.0
        close = self.TWO_DAY_CLOSE
        open = self.TWO_DAY_OPEN
        while True:
            value = (open * (ekle)) / 100
            if (float(open) + float(value)) >= float(close):
                self.TWO_DAY_YUZDE += float(ekle)
                break
            else:
                ekle += 0.005
    def DOGE_POZİTİF_THREE(self):
        ekle = 0.0
        close = self.THREE_DAY_CLOSE
        open = self.THREE_DAY_OPEN
        while True:
            value = (open * (ekle)) / 100
            if (float(open) + float(value)) >= float(close):
                self.THREE_DAY_YUZDE += float(ekle)
                break
            else:
                ekle += 0.005
    def DOGE_POZİTİF_FOUR(self):
        ekle = 0.0
        close = self.FOUR_DAY_CLOSE
        open = self.FOUR_DAY_OPEN
        while True:
            value = (open * (ekle)) / 100
            if (float(open) + float(value)) >= float(close):
                self.FOUR_DAY_YUZDE += float(ekle)
                break
            else:
                ekle += 0.005
    def DOGE_POZİTİF_FİVE(self):
        ekle = 0.0
        close = self.FİVE_DAY_CLOSE
        open = self.FİVE_DAY_OPEN
        while True:
            value = (open * (ekle)) / 100
            if (float(open) + float(value)) >= float(close):
                self.FİVE_DAY_YUZDE += float(ekle)
                break
            else:
                ekle += 0.005
    def DOGE_POZİTİF_SİX(self):
        ekle = 0.0
        close = self.SİX_DAY_CLOSE
        open = self.SİX_DAY_OPEN
        while True:
            value = (open * (ekle)) / 100
            if (float(open) + float(value)) >= float(close):
                self.SİX_DAY_YUZDE += float(ekle)
                break
            else:
                ekle += 0.005
    def DOGE_POZİTİF_SEVEN(self):
        ekle = 0.0
        close = self.SEVEN_DAY_CLOSE
        open = self.SEVEN_DAY_OPEN
        while True:
            value = (open * (ekle)) / 100
            if (float(open) + float(value)) >= float(close):
                self.SEVEN_DAY_YUZDE += float(ekle)
                break
            else:
                ekle += 0.005
class Ltc():
    def __init__(self):
        self.LTC = float

        self.ONE_DAY_YUZDE = 0
        self.TWO_DAY_YUZDE = 0
        self.THREE_DAY_YUZDE = 0
        self.FOUR_DAY_YUZDE = 0
        self.FİVE_DAY_YUZDE = 0
        self.SİX_DAY_YUZDE = 0
        self.SEVEN_DAY_YUZDE = 0

        self.ONE_DAY_CLOSE = ltc_one_day_close
        self.TWO_DAY_CLOSE = ltc_two_day_close
        self.THREE_DAY_CLOSE = ltc_three_day_close
        self.FOUR_DAY_CLOSE = ltc_four_day_close
        self.FİVE_DAY_CLOSE = ltc_five_day_close
        self.SİX_DAY_CLOSE = ltc_six_day_close
        self.SEVEN_DAY_CLOSE = ltc_seven_day_close

        self.ONE_DAY_OPEN = ltc_one_day_open
        self.TWO_DAY_OPEN = ltc_two_day_open
        self.THREE_DAY_OPEN = ltc_three_day_open
        self.FOUR_DAY_OPEN = ltc_four_day_open
        self.FİVE_DAY_OPEN = ltc_five_day_open
        self.SİX_DAY_OPEN = ltc_six_day_open
        self.SEVEN_DAY_OPEN = ltc_seven_day_open

        self.LTC_POZİTİF_ONE()
        self.LTC_POZİTİF_TWO()
        self.LTC_POZİTİF_THREE()
        self.LTC_POZİTİF_FOUR()
        self.LTC_POZİTİF_FİVE()
        self.LTC_POZİTİF_SİX()
        self.LTC_POZİTİF_SEVEN()

        self.LTC_NEGATİF_ONE()
        self.LTC_NEGATİF_TWO()
        self.LTC_NEGATİF_THREE()
        self.LTC_NEGATİF_FOUR()
        self.LTC_NEGATİF_FİVE()
        self.LTC_NEGATİF_SİX()
        self.LTC_NEGATİF_SEVEN()
        self.NET_LTC()
        self.Ekle()
    def Ekle(self):
        Coinler["LTCBUSD "] = round(float(self.LTC),1)
    def NET_LTC(self):
        LTC_NET = self.ONE_DAY_YUZDE + self.TWO_DAY_YUZDE + self.THREE_DAY_YUZDE + \
            self.FOUR_DAY_YUZDE + self.FİVE_DAY_YUZDE + self.SİX_DAY_YUZDE + \
            self.SEVEN_DAY_YUZDE
        self.LTC = LTC_NET
    def LTC_NEGATİF_ONE(self):
        ekle = 0.0
        close = self.ONE_DAY_CLOSE
        open = self.ONE_DAY_OPEN
        while True:
            value = (close * (ekle)) / 100
            if (float(close) + float(value)) >= float(open):
                self.ONE_DAY_YUZDE -= float(ekle)
                break
            else:
                ekle += 0.005
    def LTC_NEGATİF_TWO(self):
        ekle = 0.0
        close = self.TWO_DAY_CLOSE
        open = self.TWO_DAY_OPEN
        while True:
            value = (close * (ekle)) / 100
            if (float(close) + float(value)) >= float(open):
                self.TWO_DAY_YUZDE -= float(ekle)
                break
            else:
                ekle += 0.005
    def LTC_NEGATİF_THREE(self):
        ekle = 0.0
        close = self.THREE_DAY_CLOSE
        open = self.THREE_DAY_OPEN
        while True:
            value = (close * (ekle)) / 100
            if (float(close) + float(value)) >= float(open):
                self.THREE_DAY_YUZDE -= float(ekle)
                break
            else:
                ekle += 0.005
    def LTC_NEGATİF_FOUR(self):
        ekle = 0.0
        close = self.FOUR_DAY_CLOSE
        open = self.FOUR_DAY_OPEN
        while True:
            value = (close * (ekle)) / 100
            if (float(close) + float(value)) >= float(open):
                self.FOUR_DAY_YUZDE -= float(ekle)
                break
            else:
                ekle += 0.0005
    def LTC_NEGATİF_FİVE(self):
        ekle = 0.0
        close = self.FİVE_DAY_CLOSE
        open = self.FİVE_DAY_OPEN
        while True:
            value = (close * (ekle)) / 100
            if (float(close) + float(value)) >= float(open):
                self.FİVE_DAY_YUZDE -= float(ekle)
                break
            else:
                ekle += 0.005
    def LTC_NEGATİF_SİX(self):
        ekle = 0.0
        close = self.SİX_DAY_CLOSE
        open = self.SİX_DAY_OPEN
        while True:
            value = (close * (ekle)) / 100
            if (float(close) + float(value)) >= float(open):
                self.SİX_DAY_YUZDE -= float(ekle)
                break
            else:
                ekle += 0.005
    def LTC_NEGATİF_SEVEN(self):
        ekle = 0.0
        close = self.SEVEN_DAY_CLOSE
        open = self.SEVEN_DAY_OPEN
        while True:
            value = (close * (ekle)) / 100
            if (float(close) + float(value)) >= float(open):
                self.SEVEN_DAY_YUZDE -= float(ekle)
                break
            else:
                ekle += 0.005

    def LTC_POZİTİF_ONE(self):
        ekle = 0.0
        close = self.ONE_DAY_CLOSE
        open = self.ONE_DAY_OPEN
        while True:
            value = (open * (ekle)) / 100
            if (float(open) + float(value)) >= float(close):
                self.ONE_DAY_YUZDE += float(ekle)
                break
            else:
                ekle += 0.005
    def LTC_POZİTİF_TWO(self):
        ekle = 0.0
        close = self.TWO_DAY_CLOSE
        open = self.TWO_DAY_OPEN
        while True:
            value = (open * (ekle)) / 100
            if (float(open) + float(value)) >= float(close):
                self.TWO_DAY_YUZDE += float(ekle)
                break
            else:
                ekle += 0.005
    def LTC_POZİTİF_THREE(self):
        ekle = 0.0
        close = self.THREE_DAY_CLOSE
        open = self.THREE_DAY_OPEN
        while True:
            value = (open * (ekle)) / 100
            if (float(open) + float(value)) >= float(close):
                self.THREE_DAY_YUZDE += float(ekle)
                break
            else:
                ekle += 0.005
    def LTC_POZİTİF_FOUR(self):
        ekle = 0.0
        close = self.FOUR_DAY_CLOSE
        open = self.FOUR_DAY_OPEN
        while True:
            value = (open * (ekle)) / 100
            if (float(open) + float(value)) >= float(close):
                self.FOUR_DAY_YUZDE += float(ekle)
                break
            else:
                ekle += 0.005
    def LTC_POZİTİF_FİVE(self):
        ekle = 0.0
        close = self.FİVE_DAY_CLOSE
        open = self.FİVE_DAY_OPEN
        while True:
            value = (open * (ekle)) / 100
            if (float(open) + float(value)) >= float(close):
                self.FİVE_DAY_YUZDE += float(ekle)
                break
            else:
                ekle += 0.005
    def LTC_POZİTİF_SİX(self):
        ekle = 0.0
        close = self.SİX_DAY_CLOSE
        open = self.SİX_DAY_OPEN
        while True:
            value = (open * (ekle)) / 100
            if (float(open) + float(value)) >= float(close):
                self.SİX_DAY_YUZDE += float(ekle)
                break
            else:
                ekle += 0.005
    def LTC_POZİTİF_SEVEN(self):
        ekle = 0.0
        close = self.SEVEN_DAY_CLOSE
        open = self.SEVEN_DAY_OPEN
        while True:
            value = (open * (ekle)) / 100
            if (float(open) + float(value)) >= float(close):
                self.SEVEN_DAY_YUZDE += float(ekle)
                break
            else:
                ekle += 0.005
class Uni():
    def __init__(self):
        self.UNI = float

        self.ONE_DAY_YUZDE = 0
        self.TWO_DAY_YUZDE = 0
        self.THREE_DAY_YUZDE = 0
        self.FOUR_DAY_YUZDE = 0
        self.FİVE_DAY_YUZDE = 0
        self.SİX_DAY_YUZDE = 0
        self.SEVEN_DAY_YUZDE = 0

        self.ONE_DAY_CLOSE = uni_one_day_close
        self.TWO_DAY_CLOSE = uni_two_day_close
        self.THREE_DAY_CLOSE = uni_three_day_close
        self.FOUR_DAY_CLOSE = uni_four_day_close
        self.FİVE_DAY_CLOSE = uni_five_day_close
        self.SİX_DAY_CLOSE = uni_six_day_close
        self.SEVEN_DAY_CLOSE = uni_seven_day_close

        self.ONE_DAY_OPEN = uni_one_day_open
        self.TWO_DAY_OPEN = uni_two_day_open
        self.THREE_DAY_OPEN = uni_three_day_open
        self.FOUR_DAY_OPEN = uni_four_day_open
        self.FİVE_DAY_OPEN = uni_five_day_open
        self.SİX_DAY_OPEN = uni_six_day_open
        self.SEVEN_DAY_OPEN = uni_seven_day_open

        self.UNI_POZİTİF_ONE()
        self.UNI_POZİTİF_TWO()
        self.UNI_POZİTİF_THREE()
        self.UNI_POZİTİF_FOUR()
        self.UNI_POZİTİF_FİVE()
        self.UNI_POZİTİF_SİX()
        self.UNI_POZİTİF_SEVEN()

        self.UNI_NEGATİF_ONE()
        self.UNI_NEGATİF_TWO()
        self.UNI_NEGATİF_THREE()
        self.UNI_NEGATİF_FOUR()
        self.UNI_NEGATİF_FİVE()
        self.UNI_NEGATİF_SİX()
        self.UNI_NEGATİF_SEVEN()
        self.NET_UNI()
        self.Ekle()
    def Ekle(self):
        Coinler["UNIBUSD "] = round(float(self.UNI),1)
    def NET_UNI(self):
        UNI_NET = self.ONE_DAY_YUZDE + self.TWO_DAY_YUZDE + self.THREE_DAY_YUZDE + \
            self.FOUR_DAY_YUZDE + self.FİVE_DAY_YUZDE + self.SİX_DAY_YUZDE + \
            self.SEVEN_DAY_YUZDE
        self.UNI = UNI_NET
    def UNI_NEGATİF_ONE(self):
        ekle = 0.0
        close = self.ONE_DAY_CLOSE
        open = self.ONE_DAY_OPEN
        while True:
            value = (close * (ekle)) / 100
            if (float(close) + float(value)) >= float(open):
                self.ONE_DAY_YUZDE -= float(ekle)
                break
            else:
                ekle += 0.005
    def UNI_NEGATİF_TWO(self):
        ekle = 0.0
        close = self.TWO_DAY_CLOSE
        open = self.TWO_DAY_OPEN
        while True:
            value = (close * (ekle)) / 100
            if (float(close) + float(value)) >= float(open):
                self.TWO_DAY_YUZDE -= float(ekle)
                break
            else:
                ekle += 0.005
    def UNI_NEGATİF_THREE(self):
        ekle = 0.0
        close = self.THREE_DAY_CLOSE
        open = self.THREE_DAY_OPEN
        while True:
            value = (close * (ekle)) / 100
            if (float(close) + float(value)) >= float(open):
                self.THREE_DAY_YUZDE -= float(ekle)
                break
            else:
                ekle += 0.005
    def UNI_NEGATİF_FOUR(self):
        ekle = 0.0
        close = self.FOUR_DAY_CLOSE
        open = self.FOUR_DAY_OPEN
        while True:
            value = (close * (ekle)) / 100
            if (float(close) + float(value)) >= float(open):
                self.FOUR_DAY_YUZDE -= float(ekle)
                break
            else:
                ekle += 0.0005
    def UNI_NEGATİF_FİVE(self):
        ekle = 0.0
        close = self.FİVE_DAY_CLOSE
        open = self.FİVE_DAY_OPEN
        while True:
            value = (close * (ekle)) / 100
            if (float(close) + float(value)) >= float(open):
                self.FİVE_DAY_YUZDE -= float(ekle)
                break
            else:
                ekle += 0.005
    def UNI_NEGATİF_SİX(self):
        ekle = 0.0
        close = self.SİX_DAY_CLOSE
        open = self.SİX_DAY_OPEN
        while True:
            value = (close * (ekle)) / 100
            if (float(close) + float(value)) >= float(open):
                self.SİX_DAY_YUZDE -= float(ekle)
                break
            else:
                ekle += 0.005
    def UNI_NEGATİF_SEVEN(self):
        ekle = 0.0
        close = self.SEVEN_DAY_CLOSE
        open = self.SEVEN_DAY_OPEN
        while True:
            value = (close * (ekle)) / 100
            if (float(close) + float(value)) >= float(open):
                self.SEVEN_DAY_YUZDE -= float(ekle)
                break
            else:
                ekle += 0.005

    def UNI_POZİTİF_ONE(self):
        ekle = 0.0
        close = self.ONE_DAY_CLOSE
        open = self.ONE_DAY_OPEN
        while True:
            value = (open * (ekle)) / 100
            if (float(open) + float(value)) >= float(close):
                self.ONE_DAY_YUZDE += float(ekle)
                break
            else:
                ekle += 0.005
    def UNI_POZİTİF_TWO(self):
        ekle = 0.0
        close = self.TWO_DAY_CLOSE
        open = self.TWO_DAY_OPEN
        while True:
            value = (open * (ekle)) / 100
            if (float(open) + float(value)) >= float(close):
                self.TWO_DAY_YUZDE += float(ekle)
                break
            else:
                ekle += 0.005
    def UNI_POZİTİF_THREE(self):
        ekle = 0.0
        close = self.THREE_DAY_CLOSE
        open = self.THREE_DAY_OPEN
        while True:
            value = (open * (ekle)) / 100
            if (float(open) + float(value)) >= float(close):
                self.THREE_DAY_YUZDE += float(ekle)
                break
            else:
                ekle += 0.005
    def UNI_POZİTİF_FOUR(self):
        ekle = 0.0
        close = self.FOUR_DAY_CLOSE
        open = self.FOUR_DAY_OPEN
        while True:
            value = (open * (ekle)) / 100
            if (float(open) + float(value)) >= float(close):
                self.FOUR_DAY_YUZDE += float(ekle)
                break
            else:
                ekle += 0.005
    def UNI_POZİTİF_FİVE(self):
        ekle = 0.0
        close = self.FİVE_DAY_CLOSE
        open = self.FİVE_DAY_OPEN
        while True:
            value = (open * (ekle)) / 100
            if (float(open) + float(value)) >= float(close):
                self.FİVE_DAY_YUZDE += float(ekle)
                break
            else:
                ekle += 0.005
    def UNI_POZİTİF_SİX(self):
        ekle = 0.0
        close = self.SİX_DAY_CLOSE
        open = self.SİX_DAY_OPEN
        while True:
            value = (open * (ekle)) / 100
            if (float(open) + float(value)) >= float(close):
                self.SİX_DAY_YUZDE += float(ekle)
                break
            else:
                ekle += 0.005
    def UNI_POZİTİF_SEVEN(self):
        ekle = 0.0
        close = self.SEVEN_DAY_CLOSE
        open = self.SEVEN_DAY_OPEN
        while True:
            value = (open * (ekle)) / 100
            if (float(open) + float(value)) >= float(close):
                self.SEVEN_DAY_YUZDE += float(ekle)
                break
            else:
                ekle += 0.005
class Etc():
    def __init__(self):
        self.ETC = float

        self.ONE_DAY_YUZDE = 0
        self.TWO_DAY_YUZDE = 0
        self.THREE_DAY_YUZDE = 0
        self.FOUR_DAY_YUZDE = 0
        self.FİVE_DAY_YUZDE = 0
        self.SİX_DAY_YUZDE = 0
        self.SEVEN_DAY_YUZDE = 0

        self.ONE_DAY_CLOSE = etc_one_day_close
        self.TWO_DAY_CLOSE = etc_two_day_close
        self.THREE_DAY_CLOSE = etc_three_day_close
        self.FOUR_DAY_CLOSE = etc_four_day_close
        self.FİVE_DAY_CLOSE = etc_five_day_close
        self.SİX_DAY_CLOSE = etc_six_day_close
        self.SEVEN_DAY_CLOSE = etc_seven_day_close

        self.ONE_DAY_OPEN = etc_one_day_open
        self.TWO_DAY_OPEN = etc_two_day_open
        self.THREE_DAY_OPEN = etc_three_day_open
        self.FOUR_DAY_OPEN = etc_four_day_open
        self.FİVE_DAY_OPEN = etc_five_day_open
        self.SİX_DAY_OPEN = etc_six_day_open
        self.SEVEN_DAY_OPEN = etc_seven_day_open

        self.ETC_POZİTİF_ONE()
        self.ETC_POZİTİF_TWO()
        self.ETC_POZİTİF_THREE()
        self.ETC_POZİTİF_FOUR()
        self.ETC_POZİTİF_FİVE()
        self.ETC_POZİTİF_SİX()
        self.ETC_POZİTİF_SEVEN()

        self.ETC_NEGATİF_ONE()
        self.ETC_NEGATİF_TWO()
        self.ETC_NEGATİF_THREE()
        self.ETC_NEGATİF_FOUR()
        self.ETC_NEGATİF_FİVE()
        self.ETC_NEGATİF_SİX()
        self.ETC_NEGATİF_SEVEN()
        self.NET_ETC()
        self.Ekle()
    def Ekle(self):
        Coinler["ETCBUSD "] = round(float(self.ETC),1)
    def NET_ETC(self):
        ETC_NET = self.ONE_DAY_YUZDE + self.TWO_DAY_YUZDE + self.THREE_DAY_YUZDE + \
            self.FOUR_DAY_YUZDE + self.FİVE_DAY_YUZDE + self.SİX_DAY_YUZDE + \
            self.SEVEN_DAY_YUZDE
        self.ETC = ETC_NET
    def ETC_NEGATİF_ONE(self):
        ekle = 0.0
        close = self.ONE_DAY_CLOSE
        open = self.ONE_DAY_OPEN
        while True:
            value = (close * (ekle)) / 100
            if (float(close) + float(value)) >= float(open):
                self.ONE_DAY_YUZDE -= float(ekle)
                break
            else:
                ekle += 0.005
    def ETC_NEGATİF_TWO(self):
        ekle = 0.0
        close = self.TWO_DAY_CLOSE
        open = self.TWO_DAY_OPEN
        while True:
            value = (close * (ekle)) / 100
            if (float(close) + float(value)) >= float(open):
                self.TWO_DAY_YUZDE -= float(ekle)
                break
            else:
                ekle += 0.005
    def ETC_NEGATİF_THREE(self):
        ekle = 0.0
        close = self.THREE_DAY_CLOSE
        open = self.THREE_DAY_OPEN
        while True:
            value = (close * (ekle)) / 100
            if (float(close) + float(value)) >= float(open):
                self.THREE_DAY_YUZDE -= float(ekle)
                break
            else:
                ekle += 0.005
    def ETC_NEGATİF_FOUR(self):
        ekle = 0.0
        close = self.FOUR_DAY_CLOSE
        open = self.FOUR_DAY_OPEN
        while True:
            value = (close * (ekle)) / 100
            if (float(close) + float(value)) >= float(open):
                self.FOUR_DAY_YUZDE -= float(ekle)
                break
            else:
                ekle += 0.0005
    def ETC_NEGATİF_FİVE(self):
        ekle = 0.0
        close = self.FİVE_DAY_CLOSE
        open = self.FİVE_DAY_OPEN
        while True:
            value = (close * (ekle)) / 100
            if (float(close) + float(value)) >= float(open):
                self.FİVE_DAY_YUZDE -= float(ekle)
                break
            else:
                ekle += 0.005
    def ETC_NEGATİF_SİX(self):
        ekle = 0.0
        close = self.SİX_DAY_CLOSE
        open = self.SİX_DAY_OPEN
        while True:
            value = (close * (ekle)) / 100
            if (float(close) + float(value)) >= float(open):
                self.SİX_DAY_YUZDE -= float(ekle)
                break
            else:
                ekle += 0.005
    def ETC_NEGATİF_SEVEN(self):
        ekle = 0.0
        close = self.SEVEN_DAY_CLOSE
        open = self.SEVEN_DAY_OPEN
        while True:
            value = (close * (ekle)) / 100
            if (float(close) + float(value)) >= float(open):
                self.SEVEN_DAY_YUZDE -= float(ekle)
                break
            else:
                ekle += 0.005

    def ETC_POZİTİF_ONE(self):
        ekle = 0.0
        close = self.ONE_DAY_CLOSE
        open = self.ONE_DAY_OPEN
        while True:
            value = (open * (ekle)) / 100
            if (float(open) + float(value)) >= float(close):
                self.ONE_DAY_YUZDE += float(ekle)
                break
            else:
                ekle += 0.005
    def ETC_POZİTİF_TWO(self):
        ekle = 0.0
        close = self.TWO_DAY_CLOSE
        open = self.TWO_DAY_OPEN
        while True:
            value = (open * (ekle)) / 100
            if (float(open) + float(value)) >= float(close):
                self.TWO_DAY_YUZDE += float(ekle)
                break
            else:
                ekle += 0.005
    def ETC_POZİTİF_THREE(self):
        ekle = 0.0
        close = self.THREE_DAY_CLOSE
        open = self.THREE_DAY_OPEN
        while True:
            value = (open * (ekle)) / 100
            if (float(open) + float(value)) >= float(close):
                self.THREE_DAY_YUZDE += float(ekle)
                break
            else:
                ekle += 0.005
    def ETC_POZİTİF_FOUR(self):
        ekle = 0.0
        close = self.FOUR_DAY_CLOSE
        open = self.FOUR_DAY_OPEN
        while True:
            value = (open * (ekle)) / 100
            if (float(open) + float(value)) >= float(close):
                self.FOUR_DAY_YUZDE += float(ekle)
                break
            else:
                ekle += 0.005
    def ETC_POZİTİF_FİVE(self):
        ekle = 0.0
        close = self.FİVE_DAY_CLOSE
        open = self.FİVE_DAY_OPEN
        while True:
            value = (open * (ekle)) / 100
            if (float(open) + float(value)) >= float(close):
                self.FİVE_DAY_YUZDE += float(ekle)
                break
            else:
                ekle += 0.005
    def ETC_POZİTİF_SİX(self):
        ekle = 0.0
        close = self.SİX_DAY_CLOSE
        open = self.SİX_DAY_OPEN
        while True:
            value = (open * (ekle)) / 100
            if (float(open) + float(value)) >= float(close):
                self.SİX_DAY_YUZDE += float(ekle)
                break
            else:
                ekle += 0.005
    def ETC_POZİTİF_SEVEN(self):
        ekle = 0.0
        close = self.SEVEN_DAY_CLOSE
        open = self.SEVEN_DAY_OPEN
        while True:
            value = (open * (ekle)) / 100
            if (float(open) + float(value)) >= float(close):
                self.SEVEN_DAY_YUZDE += float(ekle)
                break
            else:
                ekle += 0.005
bitcoin = Bitcoin()
etherneum = Etherneum()
solona = Solona()
dot = Dot()
ada = Ada()
mana = Mana()
enjin = Enjin()
avax = Avax()
doge = Doge()
link = Link()
ltc = Ltc()
uni = Uni()
etc = Etc()


class Intelence():
    # ROB EMİR FONKSİYONLARI
    def ROB_CANCEL(symbol, orderID):
        result = ROB.cancel_order(
            symbol=symbol,
            orderId=orderID)
        print("Cancel Order")
        print("Coin : ", symbol)

    def ROB_BUY_LİMİT(symbol, quantity, price):
        order = ROB.order_limit_buy(
            symbol=str(symbol),
            quantity=float(quantity),
            price=str(price))
        print("Order Successful !")
        print("Coin : ", symbol, "\nQuantity : ", quantity, "\nPrice : ", price)

    def ROB_SELL_LİMİT(symbol, quantity, price):
        order = ROB.order_limit_sell(
            symbol=str(symbol),
            quantity=float(quantity),
            price=str(price))
        print("Order Successful !")
        print("Coin : ", symbol, "\nQuantity : ", quantity, "\nPrice : ", price)

    def ROB_BUY_MARKET(symbol, quantity):
        order = ROB.order_market_buy(
            symbol=str(symbol),
            quantity=float(quantity))
        print("Market Order Successful !")
        print("Coin : ", symbol, "\nQuantity : ", quantity)

    def ROB_SELL_MARKET(symbol, quantity):
        order = ROB.order_market_sell(
            symbol=str(symbol),
            quantity=float(quantity))
        print("Market Order Successful !")
        print("Coin : ", symbol, "\nQuantity : ", quantity)

    # ACCOUNT FONKSİYONLARI
    def ROB_ACCOUNT_GET_BALANCE(symbol):
        balance = ROB.get_asset_balance(asset=symbol)
        balance_free = balance["free"]
        return balance_free

    def ROB_ACCOUNT_GET_TRADES_HİSTORY(symbol):
        trades = ROB.get_my_trades(symbol=symbol)
        for i in trades:
            print(i["qty"])

    def ROB_ACCOUNT_STATUS():
        status = ROB.get_account_status()
        return status["data"]

    def ROB_ACCOUNT_SNAPSHOT(params):  # TYPE = SPOT / MARGIN / FUTURES
        snapshot = ROB.get_account_snapshot(type=params)
        return snapshot

    # MARKET FONKSİYONLARI
    def ROB_SPOT_ORDER_BOOK(symbol):
        depth = ROB.get_order_book(symbol=symbol)
        indexing = 0
        history = list()
        order = list()
        amount = list()
        for i in depth.get('bids'):
            indexing += 1
            if indexing == 11:
                break
            else:
                history.append(i)

        for i in history:
            order.append(i[0])
            amount.append(i[1])
        return order, amount

    def ROB_SPOT_HİSTORY_BOOK(symbol):
        price = list()
        amount = list()
        trades = ROB.get_recent_trades(symbol=symbol)
        for i in trades:
            price.append(i["price"])
            amount.append(i["qty"])
        price.reverse()
        amount.reverse()
        return price, amount
class Constructor():
    def __init__(self):
        self.Coinler = Coinler
        self.ACTİVE = list()

        self.Coin_Return()
        self.Coin_Analysis()

    def __str__(self):
        print("\n\n\n")
        time.sleep(1)
        for i in tqdm(range(15), unit="Seçiliyor", colour="#ff4040"):
            sleep(0.1)
        for i in tqdm(range(15), unit="Yapılandırılıyor", colour="#ff4040"):
            sleep(0.1)
        print("Crypto ROB Demo Version :", self.ACTİVE)
        print("\n\n\n")

    def Coin_Analysis(self):
        Coin, Value = self.Coin_Return()
        Coin_ACTİVE = list()
        İndex = 1
        try:
            for i in range(1, len(Value)):
                if Value[0] + 2 >= Value[İndex] >= Value[0] - 2:
                    Coin_ACTİVE.append(Coin[İndex])
                İndex += 1
            print("Filter Successful")
        except:
            print("Filter Not Successful")
        self.ACTİVE = Coin_ACTİVE

    def Coin_Return(self):
        Coinler = ""
        Eklenicek_Değer = ""
        Değerleri_list = list()
        Coinler_list = list()
        for i in self.Coinler.items():
            for Coin in i[0]:
                Coinler += Coin
                if Coin == " ":
                    Değerleri_list.append(i[1])
        for i in Coinler:
            if i == " ":
                Coinler_list.append(Eklenicek_Değer)
                Eklenicek_Değer = ""
                continue
            Eklenicek_Değer += i
        Data = list(zip(Coinler_list, Değerleri_list))
        Coins_Values = list()
        Coins = list()
        for i, j in Data:
            Coins_Values.append(j)
            Coins.append(i)
        return Coins, Coins_Values
class Transpitor():
    def __init__(self):
        self.Transpitor = Constructor.ACTİVE
        self.Transpitor.clear()
        self.Transpitor.append('BTCBUSD')

        # -------------------------------------
        # GEÇMİŞ HAFTALAR
        # -------------------------------------
        self.Bitcoin_PRİCE = 0
        self.Bitcoin_BUY = 0
        self.Bitcoin_SELL = 0
        self.Bitcoin_HİGHT = 0
        self.Bitcoin_LOW = 0
        self.Bitcoin_OPEN = 0
        self.Bitcoin_CLOSE = 0

        # ------------------------------------
        # ŞUANKİ ZAMAN
        # ------------------------------------
        self.NOW_Bitcoin_PRİCE = 0
        self.NOW_Bitcoin_BUY = 0
        self.NOW_Bitcoin_SELL = 0
        self.NOW_Bitcoin_HİGHT = 0
        self.NOW_Bitcoin_LOW = 0
        self.NOW_Bitcoin_OPEN = 0
        self.NOW_Bitcoin_CLOSE = 0

        # ------------------------------------
        # Enginner
        # ------------------------------------
        self.MultiChain_INT = 0
        self.Piyasa_DURUMU = 0

        # KULLANILACAK DEĞERLER
        self.BTC_KARMA_BUY = 0
        self.BTC_KARMA_SELL = 0

        self.OLD_Coins_PRİCE()
        self.OLD_Coins_RETURNS()
        self.OLD_GENEL_PİYASA_DURUMU()
        self.OLD_COİNS_WEEK()
        self.OLD_COİNS_DAY()

        self.NOW_Coins_PRİCE()
        self.NOW_Coins_RETURNS()
        self.NOW_GENEL_PİYASA_DURUMU()
        self.NOW_Coins_HOUR()

        self.KARMALA()
        self.ANLIK_PİYASA_DURUMU()

    def __copy__(self):
        for i in self.Transpitor:
            self.MultiChain_INT += 1

    def __str__(self):
        return self.Piyasa_DURUMU

    def KARMALA(self):
        for i in self.Transpitor:
            if i == "BTCBUSD":
                self.BTC_KARMA_SELL += ((self.NOW_Bitcoin_SELL * 75) / 100) + (self.Bitcoin_SELL * 65) / 100
                self.BTC_KARMA_BUY += ((self.NOW_Bitcoin_BUY * 75) / 100) + (self.Bitcoin_BUY * 65) / 100

    def ANLIK_PİYASA_DURUMU(self):
        for i in self.Transpitor:
            if i == "BTCBUSD":
                def Yuzde_Return(params):
                    return (self.Bitcoin_PRİCE * params) / 100

                times = time.gmtime()
                years = times[0]
                month = times[1]
                days = times[2]
                hour = times[3] - 1
                minutes = times[4]

                # PİYASA ÇEŞİTLERİ
                # -------------------------------------------------------

                NOTR = list()
                YUKSEK_NOTR = list()

                DALGA = list()
                YUKSEK_DALGA = list()

                DUMP = list()
                YUKSEK_DUMP = list()

                PUMP = list()
                YUKSEK_PUMP = list()

                STARTİNG_ROB_DUMP_SOL_LİST = list()
                STARTİNG_ROB_PUMP_SOL_LİST = list()

                # -------------------------------------------------------
                one_low = 0
                one_hight = 0
                one_open = 0
                one_close = 0

                two_low = 0
                two_hight = 0
                two_open = 0
                two_close = 0

                three_low = 0
                three_hight = 0
                three_open = 0
                three_close = 0

                four_low = 0
                four_hight = 0
                four_open = 0
                four_close = 0

                five_low = 0
                five_hight = 0
                five_open = 0
                five_close = 0

                try:
                    if 0 <= minutes <= 15:
                        btc = HistoricalData('BTC-USD', 900, ("{}-{}-{}-{}-{}".format(years, month, days, hour, "00")), verbose=False).retrieve_data()
                        five_low += btc['low'][-5]
                        five_open += btc['open'][-5]
                        five_close += btc['close'][-5]
                        five_hight += btc['high'][-5]

                        four_low += btc['low'][-4]
                        four_open += btc['open'][-4]
                        four_close += btc['close'][-4]
                        four_hight += btc['high'][-4]

                        three_low += btc['low'][-3]
                        three_open += btc['open'][-3]
                        three_close += btc['close'][-3]
                        three_hight += btc['high'][-3]

                        two_low += btc['low'][-2]
                        two_open += btc['open'][-2]
                        two_close += btc['close'][-2]
                        two_hight += btc['high'][-2]

                        one_low += btc['low'][-1]
                        one_open += btc['open'][-1]
                        one_close += btc['close'][-1]
                        one_hight += btc['high'][-1]
                    elif 15 <= minutes <= 30:
                        btc = HistoricalData('BTC-USD', 900, ("{}-{}-{}-{}-{}".format(years, month, days, hour, "00")), verbose=False).retrieve_data()
                        five_low += btc['low'][-5]
                        five_open += btc['open'][-5]
                        five_close += btc['close'][-5]
                        five_hight += btc['high'][-5]

                        four_low += btc['low'][-4]
                        four_open += btc['open'][-4]
                        four_close += btc['close'][-4]
                        four_hight += btc['high'][-4]

                        three_low += btc['low'][-3]
                        three_open += btc['open'][-3]
                        three_close += btc['close'][-3]
                        three_hight += btc['high'][-3]

                        two_low += btc['low'][-2]
                        two_open += btc['open'][-2]
                        two_close += btc['close'][-2]
                        two_hight += btc['high'][-2]

                        one_low += btc['low'][-1]
                        one_open += btc['open'][-1]
                        one_close += btc['close'][-1]
                        one_hight += btc['high'][-1]
                    elif 30 <= minutes <= 45:
                        btc = HistoricalData('BTC-USD', 900, ("{}-{}-{}-{}-{}".format(years, month, days, hour, "00")), verbose=False).retrieve_data()
                        five_low += btc['low'][-5]
                        five_open += btc['open'][-5]
                        five_close += btc['close'][-5]
                        five_hight += btc['high'][-5]

                        four_low += btc['low'][-4]
                        four_open += btc['open'][-4]
                        four_close += btc['close'][-4]
                        four_hight += btc['high'][-4]

                        three_low += btc['low'][-3]
                        three_open += btc['open'][-3]
                        three_close += btc['close'][-3]
                        three_hight += btc['high'][-3]

                        two_low += btc['low'][-2]
                        two_open += btc['open'][-2]
                        two_close += btc['close'][-2]
                        two_hight += btc['high'][-2]

                        one_low += btc['low'][-1]
                        one_open += btc['open'][-1]
                        one_close += btc['close'][-1]
                        one_hight += btc['high'][-1]
                    elif 45 <= minutes <= 60:
                        btc = HistoricalData('BTC-USD', 900, ("{}-{}-{}-{}-{}".format(years, month, days, hour, "00")), verbose=False).retrieve_data()
                        five_low += btc['low'][-5]
                        five_open += btc['open'][-5]
                        five_close += btc['close'][-5]
                        five_hight += btc['high'][-5]

                        four_low += btc['low'][-4]
                        four_open += btc['open'][-4]
                        four_close += btc['close'][-4]
                        four_hight += btc['high'][-4]

                        three_low += btc['low'][-3]
                        three_open += btc['open'][-3]
                        three_close += btc['close'][-3]
                        three_hight += btc['high'][-3]

                        two_low += btc['low'][-2]
                        two_open += btc['open'][-2]
                        two_close += btc['close'][-2]
                        two_hight += btc['high'][-2]

                        one_low += btc['low'][-1]
                        one_open += btc['open'][-1]
                        one_close += btc['close'][-1]
                        one_hight += btc['high'][-1]
                except:
                    pass

                def Enginner_NEG(Close, Open):
                    RETURNS_DATA = 0
                    ekle = 0.0
                    close = Close
                    open = Open
                    while True:
                        value = (close * (ekle)) / 100
                        if (int(close) + float(value)) >= int(open):
                            RETURNS_DATA -= float(ekle)
                            break
                        else:
                            ekle += 0.005
                    return RETURNS_DATA

                def Enginner_POZ(Close, Open):
                    RETURNS_DATA = 0
                    ekle = 0.0
                    close = Close
                    open = Open
                    while True:
                        value = (open * (ekle)) / 100
                        if (int(open) + float(value)) >= int(close):
                            RETURNS_DATA += float(ekle)
                            break
                        else:
                            ekle += 0.005
                    return RETURNS_DATA

                class Piyasa_Analysis():
                    def __init__(self):
                        self.YUKSEK_NOTR()
                        self.NOTR()

                        self.DALGA()
                        self.YUKSEK_DALGA()

                        self.DUMP()
                        self.YUKSEK_DUMP()

                        self.PUMP()
                        self.YUKSEK_PUMP()

                        self.Starting_ROB_DUMP()
                        self.Starting_ROB_PUMP()

                    def YUKSEK_NOTR(self):
                        if (Yuzde_Return(params=0.15) >= Enginner_POZ(Close=one_close, Open=one_open) * Yuzde_Return(params=100)) or -Yuzde_Return(params=0.15) <= (Enginner_NEG(Close=one_close, Open=one_open) * Yuzde_Return(params=100)):
                            YUKSEK_NOTR.append(True)
                        if (Yuzde_Return(params=0.15) >= Enginner_POZ(Close=one_close, Open=one_open) * Yuzde_Return(params=100)) or -Yuzde_Return(params=0.15) <= (Enginner_NEG(Close=two_close, Open=two_open) * Yuzde_Return(params=100)):
                            YUKSEK_NOTR.append(True)
                        if (Yuzde_Return(params=0.15) >= Enginner_POZ(Close=one_close, Open=one_open) * Yuzde_Return(params=100)) or -Yuzde_Return(params=0.15) <= (Enginner_NEG(Close=three_close, Open=three_open) * Yuzde_Return(params=100)):
                            YUKSEK_NOTR.append(True)
                        if (Yuzde_Return(params=0.15) >= Enginner_POZ(Close=one_close, Open=one_open) * Yuzde_Return(params=100)) or -Yuzde_Return(params=0.15) <= (Enginner_NEG(Close=four_close, Open=four_open) * Yuzde_Return(params=100)):
                            YUKSEK_NOTR.append(True)
                        if (Yuzde_Return(params=0.15) >= Enginner_POZ(Close=one_close, Open=one_open) * Yuzde_Return(params=100)) or -Yuzde_Return(params=0.15) <= (Enginner_NEG(Close=five_close, Open=one_open) * Yuzde_Return(params=100)):
                            YUKSEK_NOTR.append(True)

                    def NOTR(self):
                        if (Yuzde_Return(params=0.30) >= Enginner_POZ(Close=one_close, Open=one_open) * Yuzde_Return(params=100)) or -Yuzde_Return(params=0.30) <= (Enginner_NEG(Close=one_close, Open=one_open) * Yuzde_Return(params=100)):
                            NOTR.append(True)
                        if (Yuzde_Return(params=0.30) >= Enginner_POZ(Close=two_close, Open=two_open) * Yuzde_Return(params=100)) or -Yuzde_Return(params=0.30) <= (Enginner_NEG(Close=two_close, Open=two_open) * Yuzde_Return(params=100)):
                            NOTR.append(True)
                        if (Yuzde_Return(params=0.30) >= Enginner_POZ(Close=three_close, Open=three_open) * Yuzde_Return(params=100)) or -Yuzde_Return(params=0.30) <= (Enginner_NEG(Close=three_close, Open=three_open) * Yuzde_Return(params=100)):
                            NOTR.append(True)
                        if (Yuzde_Return(params=0.30) >= Enginner_POZ(Close=four_close, Open=four_open) * Yuzde_Return(params=100)) or -Yuzde_Return(params=0.30) <= (Enginner_NEG(Close=four_close, Open=four_open) * Yuzde_Return(params=100)):
                            NOTR.append(True)
                        if (Yuzde_Return(params=0.30) >= Enginner_POZ(Close=five_close, Open=five_open) * Yuzde_Return(params=100)) or -Yuzde_Return(params=0.30) <= (Enginner_NEG(Close=five_close, Open=five_open) * Yuzde_Return(params=100)):
                            NOTR.append(True)

                    def DALGA(self):
                        if Yuzde_Return(params=0.30) <= one_hight - one_low:
                            DALGA.append(True)
                        if Yuzde_Return(params=0.30) <= two_hight - two_low:
                            DALGA.append(True)
                        if Yuzde_Return(params=0.30) <= three_hight - three_low:
                            DALGA.append(True)
                        if Yuzde_Return(params=0.30) <= four_hight - four_low:
                            DALGA.append(True)
                        if Yuzde_Return(params=0.30) <= five_hight - five_low:
                            DALGA.append(True)

                    def YUKSEK_DALGA(self):
                        if Yuzde_Return(params=0.4) <= one_hight - one_low:
                            YUKSEK_DALGA.append(True)
                        if Yuzde_Return(params=0.4) <= two_hight - two_low:
                            YUKSEK_DALGA.append(True)
                        if Yuzde_Return(params=0.4) <= three_hight - three_low:
                            YUKSEK_DALGA.append(True)
                        if Yuzde_Return(params=0.4) <= four_hight - four_low:
                            YUKSEK_DALGA.append(True)
                        if Yuzde_Return(params=0.4) <= five_hight - five_low:
                            YUKSEK_DALGA.append(True)

                    def DUMP(self):
                        if four_open - four_close >= Yuzde_Return(params=0.25):
                            DUMP.append(True)
                        if three_open - three_close >= Yuzde_Return(params=0.25):
                            DUMP.append(True)
                        if two_open - two_close >= Yuzde_Return(params=0.25):
                            DUMP.append(True)
                        if one_open - one_close >= Yuzde_Return(params=0.25):
                            DUMP.append(True)

                    def YUKSEK_DUMP(self):
                        if four_open - four_close >= Yuzde_Return(params=0.35):
                            YUKSEK_DUMP.append(True)
                        if three_open - three_close >= Yuzde_Return(params=0.35):
                            YUKSEK_DUMP.append(True)
                        if two_open - two_close >= Yuzde_Return(params=0.35):
                            YUKSEK_DUMP.append(True)
                        if one_open - one_close >= Yuzde_Return(params=0.35):
                            YUKSEK_DUMP.append(True)

                    def PUMP(self):
                        if four_close - four_open >= Yuzde_Return(params=0.15):
                            PUMP.append(True)
                        if three_close - three_open >= Yuzde_Return(params=0.15):
                            PUMP.append(True)
                        if two_close - two_open >= Yuzde_Return(params=0.15):
                            PUMP.append(True)
                        if one_close - one_open >= Yuzde_Return(params=0.15):
                            PUMP.append(True)

                    def YUKSEK_PUMP(self):
                        if four_close - four_open >= Yuzde_Return(params=0.25):
                            YUKSEK_PUMP.append(True)
                        if three_close - three_open >= Yuzde_Return(params=0.25):
                            YUKSEK_PUMP.append(True)
                        if two_close - two_open >= Yuzde_Return(params=0.25):
                            YUKSEK_PUMP.append(True)
                        if one_close - one_open >= Yuzde_Return(params=0.25):
                            YUKSEK_PUMP.append(True)

                    def Starting_ROB_DUMP(self):
                        if one_open - one_close >= Yuzde_Return(params=0.25):
                            STARTİNG_ROB_DUMP_SOL_LİST.append(True)

                    def Starting_ROB_PUMP(self):
                        if one_close - one_open >= Yuzde_Return(params=0.25):
                            STARTİNG_ROB_PUMP_SOL_LİST.append(True)

                Piyasalar = Piyasa_Analysis()
                NOTR_SENSOR = 0
                YUKSEK_NOTR_SENSOR = 0

                DALGA_SENSOR = 0
                YUKSEK_DALGA_SENSOR = 0

                DUMP_SENSOR = 0
                YUKSEK_DUMP_SENSOR = 0

                PUMP_SENSOR = 0
                YUKSEK_PUMP_SENSOR = 0

                STARTİNG_ROB_DUMP_SOL = 0
                STARTİNG_ROB_PUMP_SOL = 0

                for i in STARTİNG_ROB_DUMP_SOL_LİST:
                    if i == True:
                        STARTİNG_ROB_DUMP_SOL += 1
                for i in STARTİNG_ROB_PUMP_SOL_LİST:
                    if i == True:
                        STARTİNG_ROB_PUMP_SOL += 1

                for i in YUKSEK_NOTR:
                    if i == True:
                        YUKSEK_NOTR_SENSOR += 1
                for i in NOTR:
                    if i == True:
                        NOTR_SENSOR += 1

                for i in DALGA:
                    if i == True:
                        DALGA_SENSOR += 1
                for i in YUKSEK_DALGA:
                    if i == True:
                        YUKSEK_DALGA_SENSOR += 1

                for i in DUMP:
                    if i == True:
                        DUMP_SENSOR += 1
                for i in YUKSEK_DUMP:
                    if i == True:
                        YUKSEK_DUMP_SENSOR += 1

                for i in PUMP:
                    if i == True:
                        PUMP_SENSOR += 1
                for i in YUKSEK_PUMP:
                    if i == True:
                        YUKSEK_PUMP_SENSOR += 1

                if STARTİNG_ROB_PUMP_SOL == 1:
                    print("\n\n")
                    print("Crypto ROB Demo Core Versiyon !")
                    print("-----------------------------------------------------")
                    print("Acil PUMP Piyasa Yapılandırılıyor")
                    print("Bitcoin")
                    print("-----------------------------------------------------")
                    print("\n\n")
                    # self.BTC_KARMA_SELL += (self.BTC_KARMA_SELL * 40) / 100
                    self.BTC_KARMA_BUY += (self.BTC_KARMA_BUY * 40) / 100
                    self.Piyasa_DURUMU = 6
                elif STARTİNG_ROB_DUMP_SOL == 1:
                    print("\n\n")
                    print("Crypto ROB Private Core Versiyon !")
                    print("-----------------------------------------------------")
                    print("Acil Dump Piyasa Yapılandırılıyor")
                    print("Bitcoin")
                    print("-----------------------------------------------------")
                    print("\n\n")
                    self.BTC_KARMA_BUY += (self.BTC_KARMA_BUY * 40) / 100
                    # self.BTC_KARMA_SELL -= (self.BTC_KARMA_SELL * 40) / 100
                    self.Piyasa_DURUMU = 8
                elif YUKSEK_DUMP_SENSOR == 3 or YUKSEK_DUMP_SENSOR == 4:
                    print("\n\n")
                    print("Crypto ROB Private Core Versiyon !")
                    print("-----------------------------------------------------")
                    print("Mega Dump Piyasa Yapılandırılıyor")
                    print("Bitcoin")
                    print("-----------------------------------------------------")
                    print("\n\n")
                    self.BTC_KARMA_BUY += (self.BTC_KARMA_BUY * 50) / 100
                    # self.BTC_KARMA_SELL -= (self.BTC_KARMA_SELL * 50) / 100
                    self.Piyasa_DURUMU = 8
                elif DUMP_SENSOR == 3 or DUMP_SENSOR == 4:
                    print("\n\n")
                    print("Crypto ROB Private Core Versiyon !")
                    print("-----------------------------------------------------")
                    print("Dump Piyasa Yapılandırılıyor")
                    print("Bitcoin")
                    print("-----------------------------------------------------")
                    print("\n\n")
                    self.BTC_KARMA_BUY += (self.BTC_KARMA_BUY * 30) / 100
                    # self.BTC_KARMA_SELL -= (self.BTC_KARMA_SELL * 30) / 100
                    self.Piyasa_DURUMU = 7
                elif YUKSEK_DALGA_SENSOR == 3 or YUKSEK_DALGA_SENSOR == 4:
                    print("\n\n")
                    print("Crypto ROB Private Core Versiyon !")
                    print("-----------------------------------------------------")
                    print("Mega Dalga Piyasa Yapılandırılıyor")
                    print("Bitcoin")
                    print("-----------------------------------------------------")
                    print("\n\n")
                    self.BTC_KARMA_BUY += (self.BTC_KARMA_BUY * 40) / 100
                    self.BTC_KARMA_SELL += (self.BTC_KARMA_SELL * 40) / 100
                    self.Piyasa_DURUMU = 2
                elif DALGA_SENSOR == 4 or DALGA_SENSOR == 5:
                    print("\n\n")
                    print("Crypto ROB Private Core Versiyon !")
                    print("-----------------------------------------------------")
                    print("Dalga Piyasa Yapılandırılıyor.")
                    print("Bitcoin")
                    print("-----------------------------------------------------")
                    print("\n\n")
                    self.BTC_KARMA_BUY += (self.BTC_KARMA_BUY * 20) / 100
                    self.BTC_KARMA_SELL += (self.BTC_KARMA_SELL * 20) / 100
                    self.Piyasa_DURUMU = 1
                elif YUKSEK_PUMP_SENSOR == 3 or YUKSEK_PUMP_SENSOR == 4:
                    print("\n\n")
                    print("Crypto ROB Private Core Versiyon !")
                    print("-----------------------------------------------------")
                    print("Mega Pump Piyasa Yapılandırılıyor")
                    print("Bitcoin")
                    print("-----------------------------------------------------")
                    print("\n\n")
                    # self.BTC_KARMA_SELL -= (self.BTC_KARMA_SELL * 50) / 100
                    self.BTC_KARMA_BUY += (self.BTC_KARMA_BUY * 50) / 100
                    self.Piyasa_DURUMU = 6
                elif PUMP_SENSOR == 3 or PUMP_SENSOR == 4:
                    print("\n\n")
                    print("Crypto ROB Private Core Versiyon !")
                    print("-----------------------------------------------------")
                    print("Pump Piyasa Yapılandırılıyor.")
                    print("Bitcoin")
                    print("-----------------------------------------------------")
                    print("\n\n")
                    # self.BTC_KARMA_SELL -= (self.BTC_KARMA_SELL * 30) / 100
                    self.BTC_KARMA_BUY += (self.BTC_KARMA_BUY * 30) / 100
                    self.Piyasa_DURUMU = 5
                elif YUKSEK_NOTR_SENSOR == 5:
                    print("\n\n")
                    print("Crypto ROB Private Core Versiyon !")
                    print("-----------------------------------------------------")
                    print("Yüksek Nötr Piyasa Yapılandırılıyor")
                    print("Bitcoin")
                    print("-----------------------------------------------------")
                    print("\n\n")
                    self.BTC_KARMA_BUY -= (self.BTC_KARMA_BUY * 35) / 100
                    self.BTC_KARMA_SELL -= (self.BTC_KARMA_SELL * 35) / 100
                    self.Piyasa_DURUMU = 4
                elif NOTR_SENSOR == 5:
                    print("\n\n")
                    print("Crypto ROB Private Core Versiyon !")
                    print("-----------------------------------------------------")
                    print("Nötr Piyasa Yapılandırılıyor")
                    print("Bitcoin")
                    print("-----------------------------------------------------")
                    print("\n\n")
                    self.BTC_KARMA_BUY -= (self.BTC_KARMA_BUY * 15) / 100
                    self.BTC_KARMA_SELL -= (self.BTC_KARMA_SELL * 15) / 100
                    self.Piyasa_DURUMU = 3

    def NOW_Coins_RETURNS(self):
        ocak_max = 31
        subat_max = 28
        mart_max = 31
        nisan_max = 30
        mayıs_max = 31
        haziran_max = 30
        temmuz_max = 31
        agustos_max = 31
        eylul_max = 30
        ekim_max = 31
        kasım_max = 30
        aralık_max = 31

        times = time.gmtime()
        years = times[0]
        month = times[1]
        days = times[2]

        years_new = times[0]
        month_new = times[1]
        days_new = times[2]

        if days == 1 and month == 1:
            days_new -= days_new
            month_new -= month_new
            days_new += aralık_max
            month_new += 12
            years_new -= years_new
            years_new += years - 1
        elif days == 1 and month == 2:
            days_new -= days_new
            month_new -= month_new
            days_new += ocak_max
            month_new += 1
        elif days == 1 and month == 3:
            days_new -= days_new
            month_new -= month_new
            days_new += subat_max
            month_new += 2
        elif days == 1 and month == 4:
            days_new -= days_new
            month_new -= month_new
            days_new += mart_max
            month_new += 3
        elif days == 1 and month == 5:
            days_new -= days_new
            month_new -= month_new
            days_new += nisan_max
            month_new += 4
        elif days == 1 and month == 6:
            days_new -= days_new
            month_new -= month_new
            days_new += mayıs_max
            month_new += 5
        elif days == 1 and month == 7:
            days_new -= days_new
            month_new -= month_new
            days_new += haziran_max
            month_new += 6
        elif days == 1 and month == 8:
            days_new -= days_new
            month_new -= month_new
            days_new += temmuz_max
            month_new += 7
        elif days == 1 and month == 9:
            days_new -= days_new
            month_new -= month_new
            days_new += agustos_max
            month_new += 8
        elif days == 1 and month == 10:
            days_new -= days_new
            month_new -= month_new
            days_new += eylul_max
            month_new += 9
        elif days == 1 and month == 11:
            days_new -= days_new
            month_new -= month_new
            days_new += ekim_max
            month_new += 10
        elif days == 1 and month == 12:
            days_new -= days_new
            month_new -= month_new
            days_new += kasım_max
            month_new += 11

        if self.NOW_Bitcoin_PRİCE != 0:
            btc = HistoricalData('BTC-USD', 900, ("{}-{}-{}-{}-{}".format(years_new, month_new, days_new, "00", "00")), verbose=False).retrieve_data()
            self.NOW_Bitcoin_LOW += btc['low'][-1]
            self.NOW_Bitcoin_HİGHT += btc['high'][-1]
            self.NOW_Bitcoin_OPEN += btc['open'][-1]
            self.NOW_Bitcoin_CLOSE += btc['close'][-1]

    def NOW_Coins_PRİCE(self):
        for j in self.Transpitor:
            if j == "BTCBUSD":
                btc_price = LiveCryptoData('BTC-USD', verbose=False).return_data()
                btc_return = btc_price["price"][0]
                self.NOW_Bitcoin_PRİCE += float(btc_return)

    def NOW_Coins_HOUR(self):
        for j in self.Transpitor:
            if j == "BTCBUSD":
                def Data(params):
                    data = LiveCryptoData(params, verbose=False).return_data()
                    return float(data["price"][0])

                Default_DATA = Data('BTC-USD')

                ONE_HOUR = 0
                TWO_HOUR = 0
                THREE_HOUR = 0
                FOUR_HOUR = 0
                FİVE_HOUR = 0
                SİX_HOUR = 0

                ONE_HOUR_OPEN = 0
                ONE_HOUR_CLOSE = 0
                TWO_HOUR_OPEN = 0
                TWO_HOUR_CLOSE = 0
                THREE_HOUR_OPEN = 0
                THREE_HOUR_CLOSE = 0
                FOUR_HOUR_OPEN = 0
                FOUR_HOUR_CLOSE = 0
                FİVE_HOUR_OPEN = 0
                FİVE_HOUR_CLOSE = 0
                SİX_HOUR_OPEN = 0
                SİX_HOUR_CLOSE = 0

                ocak_max = 31
                subat_max = 28
                mart_max = 31
                nisan_max = 30
                mayıs_max = 31
                haziran_max = 30
                temmuz_max = 31
                agustos_max = 31
                eylul_max = 30
                ekim_max = 31
                kasım_max = 30
                aralık_max = 31

                times = time.gmtime()
                years = times[0]
                month = times[1]
                days = times[2]
                hours = times[3]

                years_new = times[0]
                month_new = times[1]
                days_new = times[2]

                if days == 1 and month == 1:
                    days_new -= days_new
                    month_new -= month_new
                    days_new += aralık_max
                    month_new += 12
                    years_new -= years_new
                    years_new += years - 1
                elif days == 1 and month == 2:
                    days_new -= days_new
                    month_new -= month_new
                    days_new += ocak_max
                    month_new += 1
                elif days == 1 and month == 3:
                    days_new -= days_new
                    month_new -= month_new
                    days_new += subat_max
                    month_new += 2
                elif days == 1 and month == 4:
                    days_new -= days_new
                    month_new -= month_new
                    days_new += mart_max
                    month_new += 3
                elif days == 1 and month == 5:
                    days_new -= days_new
                    month_new -= month_new
                    days_new += nisan_max
                    month_new += 4
                elif days == 1 and month == 6:
                    days_new -= days_new
                    month_new -= month_new
                    days_new += mayıs_max
                    month_new += 5
                elif days == 1 and month == 7:
                    days_new -= days_new
                    month_new -= month_new
                    days_new += haziran_max
                    month_new += 6
                elif days == 1 and month == 8:
                    days_new -= days_new
                    month_new -= month_new
                    days_new += temmuz_max
                    month_new += 7
                elif days == 1 and month == 9:
                    days_new -= days_new
                    month_new -= month_new
                    days_new += agustos_max
                    month_new += 8
                elif days == 1 and month == 10:
                    days_new -= days_new
                    month_new -= month_new
                    days_new += eylul_max
                    month_new += 9
                elif days == 1 and month == 11:
                    days_new -= days_new
                    month_new -= month_new
                    days_new += ekim_max
                    month_new += 10
                elif days == 1 and month == 12:
                    days_new -= days_new
                    month_new -= month_new
                    days_new += kasım_max
                    month_new += 11

                try:
                    ONE_HOUR_OPEN += BTC['open'][-1]
                    ONE_HOUR_CLOSE += BTC['close'][-1]
                except:
                    pass

                try:
                    TWO_HOUR_OPEN += BTC['open'][-2]
                    TWO_HOUR_CLOSE += BTC['close'][-2]
                except:
                    pass

                try:
                    THREE_HOUR_OPEN += BTC['open'][-3]
                    THREE_HOUR_CLOSE += BTC['close'][-3]
                except:
                    pass

                try:
                    FOUR_HOUR_OPEN += BTC['open'][-4]
                    FOUR_HOUR_CLOSE += BTC['close'][-4]
                except:
                    pass

                try:
                    FİVE_HOUR_OPEN += BTC['open'][-5]
                    FİVE_HOUR_CLOSE += BTC['close'][-5]
                except:
                    pass

                try:
                    SİX_HOUR_OPEN += BTC['open'][-6]
                    SİX_HOUR_CLOSE += BTC['close'][-6]
                except:
                    pass

                def Enginner_NEG_I():
                    nonlocal ONE_HOUR
                    ekle = 0.0
                    close = ONE_HOUR_CLOSE
                    open = ONE_HOUR_OPEN
                    while True:
                        value = (close * (ekle)) / 100
                        if (int(close) + float(value)) >= int(open):
                            ONE_HOUR -= float(ekle)
                            break
                        else:
                            ekle += 0.005

                def Enginner_NEG_II():
                    nonlocal TWO_HOUR
                    ekle = 0.0
                    close = TWO_HOUR_CLOSE
                    open = TWO_HOUR_OPEN
                    while True:
                        value = (close * (ekle)) / 100
                        if (int(close) + float(value)) >= int(open):
                            TWO_HOUR -= float(ekle)
                            break
                        else:
                            ekle += 0.005

                def Enginner_NEG_III():
                    nonlocal THREE_HOUR
                    ekle = 0.0
                    close = THREE_HOUR_CLOSE
                    open = THREE_HOUR_OPEN
                    while True:
                        value = (close * (ekle)) / 100
                        if (int(close) + float(value)) >= int(open):
                            THREE_HOUR -= float(ekle)
                            break
                        else:
                            ekle += 0.005

                def Enginner_NEG_IV():
                    nonlocal FOUR_HOUR
                    ekle = 0.0
                    close = FOUR_HOUR_CLOSE
                    open = FOUR_HOUR_OPEN
                    while True:
                        value = (close * (ekle)) / 100
                        if (int(close) + float(value)) >= int(open):
                            FOUR_HOUR -= float(ekle)
                            break
                        else:
                            ekle += 0.005

                def Enginner_NEG_V():
                    nonlocal FİVE_HOUR
                    ekle = 0.0
                    close = FİVE_HOUR_CLOSE
                    open = FİVE_HOUR_OPEN
                    while True:
                        value = (close * (ekle)) / 100
                        if (int(close) + float(value)) >= int(open):
                            FİVE_HOUR -= float(ekle)
                            break
                        else:
                            ekle += 0.005

                def Enginner_NEG_VI():
                    nonlocal SİX_HOUR
                    ekle = 0.0
                    close = SİX_HOUR_CLOSE
                    open = SİX_HOUR_OPEN
                    while True:
                        value = (close * (ekle)) / 100
                        if (int(close) + float(value)) >= int(open):
                            SİX_HOUR -= float(ekle)
                            break
                        else:
                            ekle += 0.005

                def Enginner_POZ_I():
                    nonlocal ONE_HOUR
                    ekle = 0.0
                    close = ONE_HOUR_CLOSE
                    open = ONE_HOUR_OPEN
                    while True:
                        value = (open * (ekle)) / 100
                        if (int(open) + float(value)) >= int(close):
                            ONE_HOUR += float(ekle)
                            break
                        else:
                            ekle += 0.005

                def Enginner_POZ_II():
                    nonlocal TWO_HOUR
                    ekle = 0.0
                    close = TWO_HOUR_CLOSE
                    open = TWO_HOUR_OPEN
                    while True:
                        value = (open * (ekle)) / 100
                        if (int(open) + float(value)) >= int(close):
                            TWO_HOUR += float(ekle)
                            break
                        else:
                            ekle += 0.005

                def Enginner_POZ_III():
                    nonlocal THREE_HOUR
                    ekle = 0.0
                    close = THREE_HOUR_CLOSE
                    open = THREE_HOUR_OPEN
                    while True:
                        value = (open * (ekle)) / 100
                        if (int(open) + float(value)) >= int(close):
                            THREE_HOUR += float(ekle)
                            break
                        else:
                            ekle += 0.005

                def Enginner_POZ_IV():
                    nonlocal FOUR_HOUR
                    ekle = 0.0
                    close = FOUR_HOUR_CLOSE
                    open = FOUR_HOUR_OPEN
                    while True:
                        value = (open * (ekle)) / 100
                        if (int(open) + float(value)) >= int(close):
                            FOUR_HOUR += float(ekle)
                            break
                        else:
                            ekle += 0.005

                def Enginner_POZ_V():
                    nonlocal FİVE_HOUR
                    ekle = 0.0
                    close = FİVE_HOUR_CLOSE
                    open = FİVE_HOUR_OPEN
                    while True:
                        value = (open * (ekle)) / 100
                        if (int(open) + float(value)) >= int(close):
                            FİVE_HOUR += float(ekle)
                            break
                        else:
                            ekle += 0.005

                def Enginner_POZ_VI():
                    nonlocal SİX_HOUR
                    ekle = 0.0
                    close = SİX_HOUR_CLOSE
                    open = SİX_HOUR_OPEN
                    while True:
                        value = (open * (ekle)) / 100
                        if (int(open) + float(value)) >= int(close):
                            SİX_HOUR += float(ekle)
                            break
                        else:
                            ekle += 0.005

                Enginner_NEG_I()
                Enginner_NEG_II()
                Enginner_NEG_III()
                Enginner_NEG_IV()
                Enginner_NEG_V()
                Enginner_NEG_VI()
                Enginner_POZ_I()
                Enginner_POZ_II()
                Enginner_POZ_III()
                Enginner_POZ_IV()
                Enginner_POZ_V()
                Enginner_POZ_VI()

                btc_price = Data("BTC-USD")

                if ONE_HOUR > 0.3:
                    self.NOW_Bitcoin_BUY += (float(btc_price) * 0.60) / 100
                    self.NOW_Bitcoin_SELL -= (float(btc_price) * 0.45) / 100
                elif ONE_HOUR > 0.2:
                    self.NOW_Bitcoin_BUY += (float(btc_price) * 0.55) / 100
                    self.NOW_Bitcoin_SELL -= (float(btc_price) * 0.40) / 100
                elif ONE_HOUR > 0.1:
                    self.NOW_Bitcoin_BUY += (float(btc_price) * 0.50) / 100
                    self.NOW_Bitcoin_SELL -= (float(btc_price) * 0.35) / 100

                if ONE_HOUR < -0.3:
                    self.NOW_Bitcoin_SELL += (float(btc_price) * 0.60) / 100
                    self.NOW_Bitcoin_BUY -= (float(btc_price) * 0.45) / 100
                elif ONE_HOUR < -0.2:
                    self.NOW_Bitcoin_SELL += (float(btc_price) * 0.55) / 100
                    self.NOW_Bitcoin_BUY -= (float(btc_price) * 0.40) / 100
                elif ONE_HOUR < -0.1:
                    self.NOW_Bitcoin_SELL += (float(btc_price) * 0.50) / 100
                    self.NOW_Bitcoin_BUY -= (float(btc_price) * 0.35) / 100

                if TWO_HOUR > 0.3:
                    self.NOW_Bitcoin_BUY += (float(btc_price) * 0.55) / 100
                    self.NOW_Bitcoin_SELL -= (float(btc_price) * 0.40) / 100
                elif TWO_HOUR > 0.2:
                    self.NOW_Bitcoin_BUY += (float(btc_price) * 0.50) / 100
                    self.NOW_Bitcoin_SELL -= (float(btc_price) * 0.35) / 100
                elif TWO_HOUR > 0.1:
                    self.NOW_Bitcoin_BUY += (float(btc_price) * 0.45) / 100
                    self.NOW_Bitcoin_SELL -= (float(btc_price) * 0.30) / 100

                if TWO_HOUR < -0.3:
                    self.NOW_Bitcoin_SELL += (float(btc_price) * 0.55) / 100
                    self.NOW_Bitcoin_BUY -= (float(btc_price) * 0.40) / 100
                elif TWO_HOUR < -0.2:
                    self.NOW_Bitcoin_SELL += (float(btc_price) * 0.50) / 100
                    self.NOW_Bitcoin_BUY -= (float(btc_price) * 0.35) / 100
                elif TWO_HOUR < -0.1:
                    self.NOW_Bitcoin_SELL += (float(btc_price) * 0.45) / 100
                    self.NOW_Bitcoin_BUY -= (float(btc_price) * 0.30) / 100

                if THREE_HOUR > 0.3:
                    self.NOW_Bitcoin_BUY += (float(btc_price) * 0.50) / 100
                    self.NOW_Bitcoin_SELL -= (float(btc_price) * 0.35) / 100
                elif THREE_HOUR > 0.2:
                    self.NOW_Bitcoin_BUY += (float(btc_price) * 0.45) / 100
                    self.NOW_Bitcoin_SELL -= (float(btc_price) * 0.30) / 100
                elif THREE_HOUR > 0.1:
                    self.NOW_Bitcoin_BUY += (float(btc_price) * 0.40) / 100
                    self.NOW_Bitcoin_SELL -= (float(btc_price) * 0.25) / 100

                if THREE_HOUR < -0.3:
                    self.NOW_Bitcoin_SELL += (float(btc_price) * 0.50) / 100
                    self.NOW_Bitcoin_BUY -= (float(btc_price) * 0.35) / 100
                elif THREE_HOUR < -0.2:
                    self.NOW_Bitcoin_SELL += (float(btc_price) * 0.45) / 100
                    self.NOW_Bitcoin_BUY -= (float(btc_price) * 0.30) / 100
                elif THREE_HOUR < -0.1:
                    self.NOW_Bitcoin_SELL += (float(btc_price) * 0.40) / 100
                    self.NOW_Bitcoin_BUY -= (float(btc_price) * 0.25) / 100

                if FOUR_HOUR > 0.3:
                    self.NOW_Bitcoin_BUY += (float(btc_price) * 0.45) / 100
                    self.NOW_Bitcoin_SELL -= (float(btc_price) * 0.35) / 100
                elif FOUR_HOUR > 0.2:
                    self.NOW_Bitcoin_BUY += (float(btc_price) * 0.40) / 100
                    self.NOW_Bitcoin_SELL -= (float(btc_price) * 0.30) / 100
                elif FOUR_HOUR > 0.1:
                    self.NOW_Bitcoin_BUY += (float(btc_price) * 0.35) / 100
                    self.NOW_Bitcoin_SELL -= (float(btc_price) * 0.25) / 100

                if FOUR_HOUR < -0.3:
                    self.NOW_Bitcoin_SELL += (float(btc_price) * 0.45) / 100
                    self.NOW_Bitcoin_BUY -= (float(btc_price) * 0.35) / 100
                elif FOUR_HOUR < -0.2:
                    self.NOW_Bitcoin_SELL += (float(btc_price) * 0.40) / 100
                    self.NOW_Bitcoin_BUY -= (float(btc_price) * 0.30) / 100
                elif FOUR_HOUR < -0.1:
                    self.NOW_Bitcoin_SELL += (float(btc_price) * 0.35) / 100
                    self.NOW_Bitcoin_BUY -= (float(btc_price) * 0.25) / 100

                if FİVE_HOUR > 0.3:
                    self.NOW_Bitcoin_BUY += (float(btc_price) * 0.40) / 100
                    self.NOW_Bitcoin_SELL -= (float(btc_price) * 0.25) / 100
                elif FİVE_HOUR > 0.2:
                    self.NOW_Bitcoin_BUY += (float(btc_price) * 0.35) / 100
                    self.NOW_Bitcoin_SELL -= (float(btc_price) * 0.20) / 100
                elif FİVE_HOUR > 0.1:
                    self.NOW_Bitcoin_BUY += (float(btc_price) * 0.30) / 100
                    self.NOW_Bitcoin_SELL -= (float(btc_price) * 0.15) / 100

                if FİVE_HOUR < -0.3:
                    self.NOW_Bitcoin_SELL += (float(btc_price) * 0.40) / 100
                    self.NOW_Bitcoin_BUY -= (float(btc_price) * 0.25) / 100
                elif FİVE_HOUR < -0.2:
                    self.NOW_Bitcoin_SELL += (float(btc_price) * 0.35) / 100
                    self.NOW_Bitcoin_BUY -= (float(btc_price) * 0.20) / 100
                elif FİVE_HOUR < -0.1:
                    self.NOW_Bitcoin_SELL += (float(btc_price) * 0.30) / 100
                    self.NOW_Bitcoin_BUY -= (float(btc_price) * 0.15) / 100

                if SİX_HOUR > 0.3:
                    self.NOW_Bitcoin_BUY += (float(btc_price) * 0.35) / 100
                    self.NOW_Bitcoin_SELL -= (float(btc_price) * 0.20) / 100
                elif SİX_HOUR > 0.2:
                    self.NOW_Bitcoin_BUY += (float(btc_price) * 0.30) / 100
                    self.NOW_Bitcoin_SELL -= (float(btc_price) * 0.15) / 100
                elif SİX_HOUR > 0.1:
                    self.NOW_Bitcoin_BUY += (float(btc_price) * 0.25) / 100
                    self.NOW_Bitcoin_SELL -= (float(btc_price) * 0.10) / 100

                if SİX_HOUR < -0.3:
                    self.NOW_Bitcoin_SELL += (float(btc_price) * 0.35) / 100
                    self.NOW_Bitcoin_BUY -= (float(btc_price) * 0.20) / 100
                elif SİX_HOUR < -0.2:
                    self.NOW_Bitcoin_SELL += (float(btc_price) * 0.30) / 100
                    self.NOW_Bitcoin_BUY -= (float(btc_price) * 0.15) / 100
                elif SİX_HOUR < -0.1:
                    self.NOW_Bitcoin_SELL += (float(btc_price) * 0.25) / 100
                    self.NOW_Bitcoin_BUY -= (float(btc_price) * 0.10) / 100

    def NOW_GENEL_PİYASA_DURUMU(self):
        for i in self.Transpitor:
            if i == "BTCBUSD":
                def Data(params):
                    data = LiveCryptoData(params, verbose=False).return_data()
                    return data['price'][0]

                def Now_Data():
                    RETURNS_DATA = 0
                    times = time.gmtime()
                    years = times[0]
                    month = times[1]
                    days = times[2] - 1

                    def Enginner_NEG():
                        global RETURNS_DATA
                        ekle = 0.0
                        close = self.NOW_Bitcoin_CLOSE
                        open = self.NOW_Bitcoin_OPEN
                        while True:
                            value = (close * (ekle)) / 100
                            if (int(close) + float(value)) >= int(open):
                                RETURNS_DATA -= float(ekle)
                                break
                            else:
                                ekle += 0.005

                    def Enginner_POZ():
                        global RETURNS_DATA
                        ekle = 0.0
                        close = self.NOW_Bitcoin_CLOSE
                        open = self.NOW_Bitcoin_OPEN
                        while True:
                            value = (open * (ekle)) / 100
                            if (int(open) + float(value)) >= int(close):
                                self.RETURNS_DATA += float(ekle)
                                break
                            else:
                                ekle += 0.005

                    Enginner_POZ()
                    Enginner_NEG()

                    btc_price = Data("BTC-USD")
                    buy = 0.0
                    sell = 0.0

                    if RETURNS_DATA > 0.4:
                        buy = (float(btc_price) * 0.6) / 100
                        sell -= (float(btc_price) * 0.3) / 100
                    elif RETURNS_DATA > 0.3:
                        buy = (float(btc_price) * 0.5) / 100
                        sell -= (float(btc_price) * 0.2) / 100
                    elif RETURNS_DATA > 0.2:
                        buy = (float(btc_price) * 0.4) / 100
                        sell -= (float(btc_price) * 0.1) / 100
                    elif RETURNS_DATA > 0.1:
                        buy = (float(btc_price) * 0.3) / 100

                    if RETURNS_DATA < -0.4:
                        sell = (float(btc_price) * 0.6) / 100
                        buy -= (float(btc_price) * 0.3) / 100
                    elif RETURNS_DATA < -0.3:
                        sell = (float(btc_price) * 0.5) / 100
                        buy -= (float(btc_price) * 0.2) / 100
                    elif RETURNS_DATA < -0.2:
                        sell = (float(btc_price) * 0.4) / 100
                        buy -= (float(btc_price) * 0.1) / 100
                    elif RETURNS_DATA < -0.1:
                        sell = (float(btc_price) * 0.3) / 100

                    self.NOW_Bitcoin_SELL += sell
                    self.NOW_Bitcoin_BUY += buy

    def OLD_Coins_RETURNS(self):
        times = time.gmtime()
        years = times[0]
        month = times[1]
        days = times[2]
        if self.Bitcoin_PRİCE != 0:
            btc = HistoricalData('BTC-USD', 86400, ("{}-{}-{}-{}-{}".format(years, month, days, "00", "00")), verbose=False).retrieve_data()
            self.Bitcoin_LOW += btc['low'][0]
            self.Bitcoin_HİGHT += btc['high'][0]
            self.Bitcoin_OPEN += btc['open'][0]
            self.Bitcoin_CLOSE += btc['close'][0]

    def OLD_Coins_PRİCE(self):
        for j in self.Transpitor:
            if j == "BTCBUSD":
                btc_price = LiveCryptoData('BTC-USD', verbose=False).return_data()
                btc_return = btc_price["price"][0]
                self.Bitcoin_PRİCE += float(btc_return)

    def OLD_GENEL_PİYASA_DURUMU(self):
        def Data(params):
            data = LiveCryptoData(params, verbose=False).return_data()
            return data["price"][0]

        for i in self.Transpitor:
            if i == "BTCBUSD":
                def btc():
                    btc_price = Data("BTC-USD")
                    buy = 0.0
                    sell = 0.0
                    if Proposal.Market_INT == 1 or Proposal.Market_INT == 2:
                        buy = (float(btc_price) * 1.0) / 100
                        sell -= (float(btc_price) * 0.4) / 100
                    elif Proposal.Market_INT == 3 or Proposal.Market_INT == 4:
                        buy = (float(btc_price) * 0.9) / 100
                        sell -= (float(btc_price) * 0.3) / 100
                    elif Proposal.Market_INT == 5 or Proposal.Market_INT == 6:
                        buy = (float(btc_price) * 0.8) / 100

                    if Proposal.Market_INT == -1 or Proposal.Market_INT == -2:
                        sell = (float(btc_price) * 1.0) / 100
                        buy -= (float(btc_price) * 0.4) / 100
                    elif Proposal.Market_INT == -3 or Proposal.Market_INT == -4:
                        sell = (float(btc_price) * 0.9) / 100
                        buy -= (float(btc_price) * 0.3) / 100
                    elif Proposal.Market_INT == -5 or Proposal.Market_INT == -6:
                        sell = (float(btc_price) * 0.8) / 100

                    self.Bitcoin_BUY += buy
                    self.Bitcoin_SELL += sell

    def OLD_COİNS_WEEK(self):
        one_day_btc = Bitcoin().ONE_DAY_YUZDE
        two_day_btc = Bitcoin().TWO_DAY_YUZDE
        three_day_btc = Bitcoin().THREE_DAY_YUZDE
        four_day_btc = Bitcoin().FOUR_DAY_YUZDE
        five_day_btc = Bitcoin().FİVE_DAY_YUZDE
        BTC = one_day_btc + two_day_btc + three_day_btc + four_day_btc + five_day_btc
        for i in self.Transpitor:
            if i == "BTCBUSD":
                def btc(coin=BTC, param=self.Bitcoin_PRİCE):
                    buy = 0
                    sell = 0
                    if coin >= 10:
                        buy += (param * 0.65) / 100
                        sell += (param * 0.55) / 100
                    elif coin >= 8:
                        buy += (param * 0.60) / 100
                        sell += (param * 0.50) / 100
                    elif coin >= 6:
                        buy += (param * 0.55) / 100
                        sell += (param * 0.45) / 100
                    elif coin >= 4:
                        buy += (param * 0.50) / 100
                        sell += (param * 0.40) / 100
                    elif coin >= 2:
                        buy += (param * 0.45) / 100
                        sell += (param * 0.35) / 100
                    elif coin >= 0:
                        buy += (param * 0.35) / 100
                        sell += (param * 0.30) / 100

                    if coin <= -10:
                        buy += (param * 0.55) / 100
                        sell += (param * 0.65) / 100
                    elif coin <= -8:
                        buy += (param * 0.50) / 100
                        sell += (param * 0.60) / 100
                    elif coin <= -6:
                        buy += (param * 0.45) / 100
                        sell += (param * 0.55) / 100
                    elif coin <= -4:
                        buy += (param * 0.40) / 100
                        sell += (param * 0.50) / 100
                    elif coin <= -2:
                        buy += (param * 0.35) / 100
                        sell += (param * 0.45) / 100
                    elif coin <= 0:
                        buy += (param * 0.30) / 100
                        sell += (param * 0.35) / 100
                    self.Bitcoin_BUY += buy
                    self.Bitcoin_SELL += sell

                btc()

    def OLD_COİNS_DAY(self):
        one_day_btc = Bitcoin().ONE_DAY_YUZDE
        two_day_btc = Bitcoin().TWO_DAY_YUZDE
        three_day_btc = Bitcoin().THREE_DAY_YUZDE
        four_day_btc = Bitcoin().FOUR_DAY_YUZDE
        five_day_btc = Bitcoin().FİVE_DAY_YUZDE
        six_day_btc = Bitcoin().SİX_DAY_YUZDE
        seven_day_btc = Bitcoin().SEVEN_DAY_YUZDE

        if one_day_btc >= 10:
            self.Bitcoin_BUY += (self.Bitcoin_PRİCE * 0.17) / 100
            self.Bitcoin_SELL += (self.Bitcoin_PRİCE * 0.13) / 100
        elif one_day_btc >= 8:
            self.Bitcoin_BUY += (self.Bitcoin_PRİCE * 0.15) / 100
            self.Bitcoin_SELL += (self.Bitcoin_PRİCE * 0.11) / 100
        elif one_day_btc >= 5:
            self.Bitcoin_BUY += (self.Bitcoin_PRİCE * 0.13) / 100
            self.Bitcoin_SELL += (self.Bitcoin_PRİCE * 0.09) / 100
        elif one_day_btc >= 3:
            self.Bitcoin_BUY += (self.Bitcoin_PRİCE * 0.11) / 100
            self.Bitcoin_SELL += (self.Bitcoin_PRİCE * 0.07) / 100

        if one_day_btc <= -10:
            self.Bitcoin_SELL += (self.Bitcoin_PRİCE * 0.17) / 100
            self.Bitcoin_BUY += (self.Bitcoin_PRİCE * 0.13) / 100
        elif one_day_btc <= -8:
            self.Bitcoin_SELL += (self.Bitcoin_PRİCE * 0.15) / 100
            self.Bitcoin_BUY += (self.Bitcoin_PRİCE * 0.11) / 100
        elif one_day_btc <= -5:
            self.Bitcoin_SELL += (self.Bitcoin_PRİCE * 0.13) / 100
            self.Bitcoin_BUY += (self.Bitcoin_PRİCE * 0.09) / 100
        elif one_day_btc <= -3:
            self.Bitcoin_SELL += (self.Bitcoin_PRİCE * 0.11) / 100
            self.Bitcoin_BUY += (self.Bitcoin_PRİCE * 0.07) / 100

        if two_day_btc >= 10:
            self.Bitcoin_BUY += (self.Bitcoin_PRİCE * 0.17) / 100
            self.Bitcoin_SELL += (self.Bitcoin_PRİCE * 0.13) / 100
        elif two_day_btc >= 8:
            self.Bitcoin_BUY += (self.Bitcoin_PRİCE * 0.15) / 100
            self.Bitcoin_SELL += (self.Bitcoin_PRİCE * 0.11) / 100
        elif two_day_btc >= 5:
            self.Bitcoin_BUY += (self.Bitcoin_PRİCE * 0.13) / 100
            self.Bitcoin_SELL += (self.Bitcoin_PRİCE * 0.09) / 100
        elif two_day_btc >= 3:
            self.Bitcoin_BUY += (self.Bitcoin_PRİCE * 0.11) / 100
            self.Bitcoin_SELL += (self.Bitcoin_PRİCE * 0.07) / 100

        if two_day_btc <= -10:
            self.Bitcoin_SELL += (self.Bitcoin_PRİCE * 0.17) / 100
            self.Bitcoin_BUY += (self.Bitcoin_PRİCE * 0.13) / 100
        elif two_day_btc <= -8:
            self.Bitcoin_SELL += (self.Bitcoin_PRİCE * 0.15) / 100
            self.Bitcoin_BUY += (self.Bitcoin_PRİCE * 0.11) / 100
        elif two_day_btc <= -5:
            self.Bitcoin_SELL += (self.Bitcoin_PRİCE * 0.13) / 100
            self.Bitcoin_BUY += (self.Bitcoin_PRİCE * 0.09) / 100
        elif two_day_btc <= -3:
            self.Bitcoin_SELL += (self.Bitcoin_PRİCE * 0.11) / 100
            self.Bitcoin_BUY += (self.Bitcoin_PRİCE * 0.07) / 100

        if three_day_btc >= 10:
            self.Bitcoin_BUY += (self.Bitcoin_PRİCE * 0.17) / 100
            self.Bitcoin_SELL += (self.Bitcoin_PRİCE * 0.13) / 100
        elif three_day_btc >= 8:
            self.Bitcoin_BUY += (self.Bitcoin_PRİCE * 0.15) / 100
            self.Bitcoin_SELL += (self.Bitcoin_PRİCE * 0.11) / 100
        elif three_day_btc >= 5:
            self.Bitcoin_BUY += (self.Bitcoin_PRİCE * 0.13) / 100
            self.Bitcoin_SELL += (self.Bitcoin_PRİCE * 0.09) / 100
        elif three_day_btc >= 3:
            self.Bitcoin_BUY += (self.Bitcoin_PRİCE * 0.11) / 100
            self.Bitcoin_SELL += (self.Bitcoin_PRİCE * 0.07) / 100

        if three_day_btc <= -10:
            self.Bitcoin_SELL += (self.Bitcoin_PRİCE * 0.17) / 100
            self.Bitcoin_BUY += (self.Bitcoin_PRİCE * 0.13) / 100
        elif three_day_btc <= -8:
            self.Bitcoin_SELL += (self.Bitcoin_PRİCE * 0.15) / 100
            self.Bitcoin_BUY += (self.Bitcoin_PRİCE * 0.11) / 100
        elif three_day_btc <= -5:
            self.Bitcoin_SELL += (self.Bitcoin_PRİCE * 0.13) / 100
            self.Bitcoin_BUY += (self.Bitcoin_PRİCE * 0.09) / 100
        elif three_day_btc <= -3:
            self.Bitcoin_SELL += (self.Bitcoin_PRİCE * 0.11) / 100
            self.Bitcoin_BUY += (self.Bitcoin_PRİCE * 0.07) / 100

        if four_day_btc >= 10:
            self.Bitcoin_BUY += (self.Bitcoin_PRİCE * 0.17) / 100
            self.Bitcoin_SELL += (self.Bitcoin_PRİCE * 0.13) / 100
        elif four_day_btc >= 8:
            self.Bitcoin_BUY += (self.Bitcoin_PRİCE * 0.15) / 100
            self.Bitcoin_SELL += (self.Bitcoin_PRİCE * 0.11) / 100
        elif four_day_btc >= 5:
            self.Bitcoin_BUY += (self.Bitcoin_PRİCE * 0.13) / 100
            self.Bitcoin_SELL += (self.Bitcoin_PRİCE * 0.09) / 100
        elif four_day_btc >= 3:
            self.Bitcoin_BUY += (self.Bitcoin_PRİCE * 0.11) / 100
            self.Bitcoin_SELL += (self.Bitcoin_PRİCE * 0.07) / 100

        if four_day_btc <= -10:
            self.Bitcoin_SELL += (self.Bitcoin_PRİCE * 0.17) / 100
            self.Bitcoin_BUY += (self.Bitcoin_PRİCE * 0.13) / 100
        elif four_day_btc <= -8:
            self.Bitcoin_SELL += (self.Bitcoin_PRİCE * 0.15) / 100
            self.Bitcoin_BUY += (self.Bitcoin_PRİCE * 0.11) / 100
        elif four_day_btc <= -5:
            self.Bitcoin_SELL += (self.Bitcoin_PRİCE * 0.13) / 100
            self.Bitcoin_BUY += (self.Bitcoin_PRİCE * 0.09) / 100
        elif four_day_btc <= -3:
            self.Bitcoin_SELL += (self.Bitcoin_PRİCE * 0.11) / 100
            self.Bitcoin_BUY += (self.Bitcoin_PRİCE * 0.07) / 100

        if five_day_btc >= 10:
            self.Bitcoin_BUY += (self.Bitcoin_PRİCE * 0.17) / 100
            self.Bitcoin_SELL += (self.Bitcoin_PRİCE * 0.13) / 100
        elif five_day_btc >= 8:
            self.Bitcoin_BUY += (self.Bitcoin_PRİCE * 0.15) / 100
            self.Bitcoin_SELL += (self.Bitcoin_PRİCE * 0.11) / 100
        elif five_day_btc >= 5:
            self.Bitcoin_BUY += (self.Bitcoin_PRİCE * 0.13) / 100
            self.Bitcoin_SELL += (self.Bitcoin_PRİCE * 0.09) / 100
        elif five_day_btc >= 3:
            self.Bitcoin_BUY += (self.Bitcoin_PRİCE * 0.11) / 100
            self.Bitcoin_SELL += (self.Bitcoin_PRİCE * 0.07) / 100

        if five_day_btc <= -10:
            self.Bitcoin_SELL += (self.Bitcoin_PRİCE * 0.17) / 100
            self.Bitcoin_BUY += (self.Bitcoin_PRİCE * 0.13) / 100
        elif five_day_btc <= -8:
            self.Bitcoin_SELL += (self.Bitcoin_PRİCE * 0.15) / 100
            self.Bitcoin_BUY += (self.Bitcoin_PRİCE * 0.11) / 100
        elif five_day_btc <= -5:
            self.Bitcoin_SELL += (self.Bitcoin_PRİCE * 0.13) / 100
            self.Bitcoin_BUY += (self.Bitcoin_PRİCE * 0.09) / 100
        elif five_day_btc <= -3:
            self.Bitcoin_SELL += (self.Bitcoin_PRİCE * 0.11) / 100
            self.Bitcoin_BUY += (self.Bitcoin_PRİCE * 0.07) / 100

        if six_day_btc >= 10:
            self.Bitcoin_BUY += (self.Bitcoin_PRİCE * 0.14) / 100
            self.Bitcoin_SELL += (self.Bitcoin_PRİCE * 0.10) / 100
        elif six_day_btc >= 8:
            self.Bitcoin_BUY += (self.Bitcoin_PRİCE * 0.12) / 100
            self.Bitcoin_SELL += (self.Bitcoin_PRİCE * 0.08) / 100
        elif six_day_btc >= 5:
            self.Bitcoin_BUY += (self.Bitcoin_PRİCE * 0.10) / 100
            self.Bitcoin_SELL += (self.Bitcoin_PRİCE * 0.06) / 100
        elif six_day_btc >= 3:
            self.Bitcoin_BUY += (self.Bitcoin_PRİCE * 0.08) / 100
            self.Bitcoin_SELL += (self.Bitcoin_PRİCE * 0.04) / 100

        if six_day_btc <= -10:
            self.Bitcoin_SELL += (self.Bitcoin_PRİCE * 0.14) / 100
            self.Bitcoin_BUY += (self.Bitcoin_PRİCE * 0.10) / 100
        elif six_day_btc <= -8:
            self.Bitcoin_SELL += (self.Bitcoin_PRİCE * 0.12) / 100
            self.Bitcoin_BUY += (self.Bitcoin_PRİCE * 0.08) / 100
        elif six_day_btc <= -5:
            self.Bitcoin_SELL += (self.Bitcoin_PRİCE * 0.10) / 100
            self.Bitcoin_BUY += (self.Bitcoin_PRİCE * 0.06) / 100
        elif six_day_btc <= -3:
            self.Bitcoin_SELL += (self.Bitcoin_PRİCE * 0.08) / 100
            self.Bitcoin_BUY += (self.Bitcoin_PRİCE * 0.04) / 100

        if seven_day_btc >= 10:
            self.Bitcoin_BUY += (self.Bitcoin_PRİCE * 0.14) / 100
            self.Bitcoin_SELL += (self.Bitcoin_PRİCE * 0.10) / 100
        elif seven_day_btc >= 8:
            self.Bitcoin_BUY += (self.Bitcoin_PRİCE * 0.12) / 100
            self.Bitcoin_SELL += (self.Bitcoin_PRİCE * 0.08) / 100
        elif seven_day_btc >= 5:
            self.Bitcoin_BUY += (self.Bitcoin_PRİCE * 0.10) / 100
            self.Bitcoin_SELL += (self.Bitcoin_PRİCE * 0.06) / 100
        elif seven_day_btc >= 3:
            self.Bitcoin_BUY += (self.Bitcoin_PRİCE * 0.08) / 100
            self.Bitcoin_SELL += (self.Bitcoin_PRİCE * 0.04) / 100

        if seven_day_btc <= -10:
            self.Bitcoin_SELL += (self.Bitcoin_PRİCE * 0.14) / 100
            self.Bitcoin_BUY += (self.Bitcoin_PRİCE * 0.10) / 100
        elif seven_day_btc <= -8:
            self.Bitcoin_SELL += (self.Bitcoin_PRİCE * 0.12) / 100
            self.Bitcoin_BUY += (self.Bitcoin_PRİCE * 0.08) / 100
        elif seven_day_btc <= -5:
            self.Bitcoin_SELL += (self.Bitcoin_PRİCE * 0.10) / 100
            self.Bitcoin_BUY += (self.Bitcoin_PRİCE * 0.06) / 100
        elif seven_day_btc <= -3:
            self.Bitcoin_SELL += (self.Bitcoin_PRİCE * 0.08) / 100
            self.Bitcoin_BUY += (self.Bitcoin_PRİCE * 0.04) / 100

class Setting():
    def __init__(self):
        self.CONTROL_SYSTEMS = False
        self.Hedef = 0
        self.MARKET_CONTROL()
        self.CONTROL_SORGU()

        self.START_BALANCE = int(input("{} Başlangıç Sanal Bakiye Yazınız ($): ".format(DEMO)))
        self.HEDEF()
        self.AFTER_ROB()

    def CONTROL_SORGU(self):
        CONTROL_İNPUT = input("{} Kontrol Sistemini Çalıştırmak İster Misiniz ? 'E' ya da 'H' Yazınız. : ".format(DEMO))
        if CONTROL_İNPUT == "e" or CONTROL_İNPUT == "E":
            self.CONTROL_SYSTEMS += True
    def MARKET_CONTROL(self):
        if Proposal.Market_INT == 1 or Proposal.Market_INT == 2 or Proposal.Market_INT == -1 or Proposal.Market_INT == -2:
            print("{} Bu Tür Piyasalarda Çalıştırmak Çok Risklidir.".format(DEMO))
            Select = input("{} Yine de Çalıştıracaksanız ' E ' | Yoksa ' H ' Yazınız : ".format(DEMO))
            if Select == "E" or Select == "e":
                pass
            if Select == "H" or Select == "h":
                print("{} ROB Sonlanıyor.".format(DEMO))
                time.sleep(2)
                sys.exit()
    def HEDEF(self):
        try:
            Reload = input("{} Hedefinizi Manuel Olarak Girmek İstermisiniz ? 'E' / 'H' : ".format(DEMO))
            if Reload == "E" or Reload == "e":
                while True:
                    Reload_NUMBER = int(input("{} Hedefiniz : ".format(DEMO)))
                    if Reload_NUMBER < self.START_BALANCE:
                        print("{} Hedefiniz Bakiyeden Küçük Olamaz.".format(DEMO))
                    else:
                        self.Hedef = Reload_NUMBER
                        break
                print("{} Yeni Hedefiniz : ".format(DEMO), self.Hedef, end="$\n")
            else:
                if Proposal.Market_INT == 1 or Proposal.Market_INT == -1 or Proposal.Market_INT == 2 or Proposal.Market_INT == -2:
                    self.Hedef = (float(self.START_BALANCE) * 100.5) / 100
                elif Proposal.Market_INT == 3 or Proposal.Market_INT == -3 or Proposal.Market_INT == 4 or Proposal.Market_INT == -4:
                    self.Hedef = (float(self.START_BALANCE) * 100.7) / 100
                elif Proposal.Market_INT == 5 or Proposal.Market_INT == -5 or Proposal.Market_INT == 6 or Proposal.Market_INT == -6 or Proposal.Market_INT == 7 or Proposal.Market_INT == -7:
                    self.Hedef = (float(self.START_BALANCE) * 100.9) / 100
                else:
                    self.Hedef = (float(self.START_BALANCE) * 100.5) / 100
                print("{} Hedefiniz Crypto ROB Tarafından Otomatik Olarak Ayarlandı : {}$".format(DEMO,round(self.Hedef, 3)), end="\n")
        except:
            print("{} Hedef Ayarlar Hatası.".format(DEMO))
            print("{} Lütfen Hata Ayıklama Metnini Okuyunuz...".format(DEMO))
    def AFTER_ROB(self):
        After_ROB = input("{} İlk Alım Emrini Siz Vermek İstiyor Musunuz ? 'E' / 'H' : ".format(DEMO))
        if After_ROB == "E" or After_ROB == "e":
            STEP = 0
            print("{} Seçilen Kripto Para Anlık Fiyat : {}".format(DEMO,float(ROB.get_ticker(symbol="BTCBUSD")['lastPrice'])))
            After_ROB_ORDER = int(input("{} Alım Emri Fiyatı : ".format(DEMO)))

            def get_round_step_quantity(qty):
                global STEP
                info = ROB.get_symbol_info("BTCBUSD")
                for x in info["filters"]:
                    if x["filterType"] == "LOT_SIZE":
                        minQty = float(x["minQty"])
                        maxQty = float(x["maxQty"])
                        STEP = x["stepSize"]
                if qty < minQty:
                    qty = minQty
                return floor_step_size(qty)
            def floor_step_size(quantity):
                global STEP
                step_size_dec = Decimal(str(STEP))
                return float(int(Decimal(str(quantity)) / step_size_dec) * step_size_dec)
            def After_ROB_ORDER_FUNCTİON():
                while True:
                    try:
                        ANLIK = float(ROB.get_ticker(symbol="BTCBUSD")['lastPrice'])
                        BALANCE = float(self.START_BALANCE)
                        Quantity = math.floor(float(BALANCE)) / float(ANLIK)
                        STEP = get_round_step_quantity(qty=Quantity)
                        PRİCE = After_ROB_ORDER
                        print("{} Fiyatı : {}$ | Varlık : {}BTC 'dan Alım Emri Verilmiştir.".format(DEMO,PRİCE,STEP))
                    except:
                        print("{} After ROB Alım Emri Hatası...".format(DEMO))
                        break
                    break

            while True:
                try:
                    After_ROB_ORDER_FUNCTİON()
                    break
                except:
                    print("{} After ROB Alım Emri Loop Hatası...".format(DEMO))

            while True:
                try:
                    if float(ROB.get_ticker(symbol="BTCBUSD")['lastPrice']) < int(After_ROB_ORDER):
                        print("{} Satın Alım Başarılı !".format(DEMO))
                        break
                    else:
                        time.sleep(1)
                        print("{} Waiting Buy.".format(DEMO))
                except:
                    print("{} After ROB Loop Alım Bekleme Hatası...".format(DEMO))
            print("{} ROB Başlatılıyor. !".format(DEMO))
class MultiChainAutoSystem(Setting):
    def __init__(self):
        super().__init__()

        self.HEDEF = self.Hedef
        self.KAZANC_BALANCE = self.START_BALANCE
        self.KAZANILAN_BAKİYE = self.START_BALANCE
        self.CRYPTO = 0

        self.SORUMLU_COİN_ONE = "None"
        self.SORUMLU_COİN_ONE_AL = 0
        self.SORUMLU_COİN_ONE_SAT = 0


        self.PİYASA_DURUMU = 0
        self.CANCEL_CONTROL = 0

        self.Fee = 0
        self.Fee_CONTROL = False

        # Opportunity Algorithm
        # -------------------------
        self.SELL_Opportunity = 0
        self.BUY_Opportunity = 0
        self.Opportunity_TETİKLE = 0
        # -------------------------

        # Wavy Algorithm
        # -------------------------
        self.WAVY_STOP = False
        # -------------------------

        # Notr Algorithm
        # -------------------------
        self.NOTR_STOP = False
        # -------------------------

        # Control Algorithm
        # -------------------------
        self.CONTROL_SYSTEM = self.CONTROL_SYSTEMS
        # -------------------------

        self.MultiChain_OPTİON()
        self.MultiChain_START_CONTROL()
        self.MultiChain()

        # 1 = Dalgalı / 2 = Yuksek Dalgalı / 3 = Notr / 4 = Yuksek Notr / 5 = PUMP / 6 = Yuksek PUMP / 7 = DUMP / 8 = Yuksek DUMP /

    def MultiChain_START_CONTROL(self):
        if self.CONTROL_SYSTEM == True:
            def CONTROL_SYSTEM(Crypto="BTCBUSD"):
                DATA_CRYPTO = ""
                if Crypto == "BTCBUSD":
                    DATA_CRYPTO += "BTC-USD"

                SECOND = 0
                STOP_CONTROL = False
                while True:
                    if STOP_CONTROL == True:
                        break

                    elif SECOND == 900:
                        break

                    else:
                        time.sleep(3)
                        SECOND += 3
                        print("{} Kontrol Sistemi Sonlanmasına : {} Saniye Kaldı.\n\n".format(DEMO,int(900 - SECOND)))
                        times = time.gmtime()
                        years = times[0]
                        month = times[1]
                        days = times[2]
                        hour = times[3] - 3

                        CRYPTO_DATA = HistoricalData(DATA_CRYPTO, 900, ("{}-{}-{}-{}-{}".format(years, month, days, "00", "00")), verbose=False).retrieve_data()
                        NOW_CRYPTO_OPEN = CRYPTO_DATA['open'][-1]
                        NOW_CRYPTO_CLOSE = CRYPTO_DATA['close'][-1]

                        YUZDE = 0

                        def POZİTİF():
                            nonlocal YUZDE
                            ekle = 0
                            close = float(NOW_CRYPTO_CLOSE)
                            open = float(NOW_CRYPTO_OPEN)
                            while True:
                                value = (open * (ekle)) / 100
                                if (float(open) + float(value)) >= float(close):
                                    YUZDE += float(ekle)
                                    break
                                else:
                                    ekle += 0.005
                        def NEGATİF():
                            nonlocal YUZDE
                            ekle = 0
                            close = float(NOW_CRYPTO_CLOSE)
                            open = float(NOW_CRYPTO_OPEN)
                            while True:
                                value = (close * (ekle)) / 100
                                if (float(close) + float(value)) >= float(open):
                                    YUZDE -= float(ekle)
                                    break
                                else:
                                    ekle += 0.005

                        POZİTİF()
                        NEGATİF()

                        print("\n{} Kontrol Sistemi Aktif !\n------------------------------".format(DEMO))
                        print("{} Crypto Price : ".format(DEMO), round(YUZDE, 7), end="%  /15Min\n")
                        print(Fore.GREEN+"------------------------------\n")

                        if True:
                            STEP = 3
                            VUR_KAC_STOPED = False
                            while True:
                                time.sleep(1)
                                if VUR_KAC_STOPED == True:
                                    STOP_CONTROL += True
                                    break

                                else:
                                    while True:
                                        STEP -= 1
                                        if STEP == 0:
                                            VUR_KAC_STOPED += True
                                            break

                                        #----------------------------------------------------------
                                        STOP = False
                                        ONE_STOP = False
                                        TWO_STOP = False
                                        THREE_STOP = False
                                        CRYPTO_ACTİVE = "BTCBUSD"
                                        REPLACE = CRYPTO_ACTİVE.replace("BUSD", "")
                                        print(Fore.GREEN + "\n------------------------------")
                                        print("{} Vur Kaç Yapılandırılıyor...".format(DEMO))
                                        print(Fore.GREEN + "------------------------------")

                                        def Return_Fee():
                                            def Return_Fee_CONTROL():
                                                if self.KAZANC_BALANCE > 10000:
                                                    return 25
                                                elif self.KAZANC_BALANCE > 7500:
                                                    return 27.5
                                                elif self.KAZANC_BALANCE > 5000:
                                                    return 30
                                                elif self.KAZANC_BALANCE > 3500:
                                                    return 33.3
                                                elif self.KAZANC_BALANCE > 1500:
                                                    return 37.5
                                                else:
                                                    return 40
                                            try:
                                                if self.KAZANILAN_BAKİYE < self.KAZANC_BALANCE:
                                                    pass
                                                else:
                                                    KAAR = self.KAZANILAN_BAKİYE  # ANLIK BAKİYEMİZ
                                                    KAAR_HESAPLAYICISI = self.KAZANC_BALANCE

                                                    KAZANC = KAAR - KAAR_HESAPLAYICISI
                                                    KAZANC_NEW = float(KAZANC * Return_Fee_CONTROL()) / 100

                                                    self.Fee += KAZANC_NEW
                                                    self.KAZANC_BALANCE = self.KAZANILAN_BAKİYE
                                            except:
                                                print("{} Fee Error".format(DEMO))

                                        BUY_PRİCE = 0
                                        BUY_QUANTİTY = 0
                                        def LOW_CONTROL_BUY(Oran):
                                            nonlocal BUY_PRİCE,BUY_QUANTİTY
                                            while True:
                                                try:
                                                    ANLIK = float(ROB.get_ticker(symbol="BTCBUSD")['lastPrice'])
                                                    Quantity = self.KAZANILAN_BAKİYE / float(ANLIK)
                                                    PRİCE = float(ANLIK) - (float(ANLIK * Oran) / 100)

                                                    BUY_PRİCE += PRİCE
                                                    BUY_QUANTİTY += Quantity
                                                    self.KAZANILAN_BAKİYE -= self.KAZANILAN_BAKİYE
                                                    print("{} Fiyatı : {} | Varlık : {} 'dan Alım Emri Verilmiştir.".format(DEMO, round(PRİCE, 3), round(Quantity,6)))
                                                except:
                                                    break
                                                break
                                        while True:
                                            try:
                                                LOW_CONTROL_BUY(Oran=0.07)
                                                break
                                            except:
                                                print("{} Tekrardan Bağlantı Sağlanıyor.".format(DEMO))

                                        #-----------------
                                        while True:
                                            try:
                                                time.sleep(2)

                                                if ONE_STOP == True:
                                                    break

                                                elif float(ROB.get_ticker(symbol="BTCBUSD")['lastPrice']) < float(BUY_PRİCE):
                                                    print("{} Satın Alım Başarılı !".format(DEMO))
                                                    ONE_STOP += True

                                                elif float(ROB.get_ticker(symbol="BTCBUSD")['lastPrice']) > float(BUY_PRİCE * 101) / 100:
                                                    print("{} Emirler İptal Edildi.".format(DEMO))
                                                    STOP += True
                                                    ONE_STOP += True
                                                    self.KAZANILAN_BAKİYE = self.KAZANC_BALANCE

                                                else:
                                                    print("{} {}:{}  | Waiting Buy.".format(DEMO,time.gmtime()[3]+3,time.gmtime()[4]))
                                            except:
                                                print("{} Tekrardan Bağlantı Sağlanıyor.".format(DEMO))
                                        #-----------------

                                        SELL_PRİCE = 0
                                        SELL_BALANCE = 0
                                        def LOW_CONTROL_SELL(Oran):
                                            nonlocal SELL_PRİCE, SELL_BALANCE
                                            while True:
                                                try:
                                                    NEW_BALANCE = BUY_QUANTİTY
                                                    ANLIK = float(ROB.get_ticker(symbol="BTCBUSD")['lastPrice'])
                                                    PRİCE = float(ANLIK) + float(ANLIK * Oran) / 100
                                                    print("{} Fiyatı : {} | Varlık : {} 'dan Satım Emri Verilmiştir.".format(DEMO, round(PRİCE,3), round(NEW_BALANCE,6)))
                                                    SELL_PRİCE += PRİCE
                                                    SELL_BALANCE += NEW_BALANCE
                                                except:
                                                    break
                                                break


                                        # ---------------------
                                        while True:
                                            try:
                                                if STOP == True:
                                                    break

                                                elif TWO_STOP == True:
                                                    break

                                                LOW_CONTROL_SELL(Oran=0.07)
                                                TWO_STOP += True
                                            except:
                                                print("{} Tekrardan Bağlantı Sağlanıyor.".format(DEMO))
                                        # ---------------------


                                        while True:
                                            try:
                                                PRİCE = float(ROB.get_ticker(symbol="BTCBUSD")['lastPrice'])

                                                if STOP == True:
                                                    break

                                                elif THREE_STOP == True:
                                                    break

                                                elif PRİCE > float(SELL_PRİCE):
                                                    self.KAZANILAN_BAKİYE += PRİCE * SELL_BALANCE
                                                    STOP += True
                                                    THREE_STOP += True
                                                    Return_Fee()
                                                    print(Fore.YELLOW+"---------------------")
                                                    print(Fore.YELLOW+"---------------------")
                                                    print("{} Vur Kaç Başarılı.".format(DEMO))
                                                    print("{} Yeni Bakiyeniz : {}$".format(DEMO,round(self.KAZANILAN_BAKİYE,2)))
                                                    print("{} Ödemeniz Gereken Komisyon : {}$".format(DEMO,round(self.Fee,2)))
                                                    print(Fore.YELLOW + "---------------------")
                                                    print(Fore.YELLOW + "---------------------")
                                                elif (float(ROB.get_ticker(symbol="BTCBUSD")['lastPrice']) * 98.5) / 100 > float(SELL_PRİCE):
                                                    self.KAZANILAN_BAKİYE += PRİCE * SELL_BALANCE
                                                    THREE_STOP += True
                                                    print("{} Emirler İptal Edildi.".format(DEMO))
                                                    print("{} Stop Emri Verildi.".format(DEMO))
                                                    print("{} Yeni Bakiyeniz : {}$".format(DEMO,round(self.KAZANILAN_BAKİYE,2)))


                                                else:
                                                    print("{} {}:{}  | Waiting Sell.".format(DEMO,time.gmtime()[3]+3,time.gmtime()[4]))
                                                    time.sleep(2)
                                            except:
                                                print("{} Tekrardan Bağlantı Sağlanıyor.".format(DEMO))

                                    else:
                                        print("{} Vur Kaç Bekleniyor.".format(DEMO))

                        elif YUZDE < -0.01:
                            if True:
                                print("{} Düşüş Devam Ediyor ! Lütfen ROB Başlatılmasını Bekleyin.\n\n".format(DEMO))
                        elif YUZDE > 0.01:
                            if True:
                                print("{} Yükseliş Devam Ediyor ! Lütfen ROB Başlatılmasını Bekleyin.\n\n".format(DEMO))

            CONTROL_SYSTEM()
        else:
            print("{} Kontrol Sistemi Zaten İptal Edildi !".format(DEMO))
    def MultiChain_OPTİON(self):
        TST = Transpitor()
        TST.__copy__()
        PİYASA_DURUMU = TST.__str__()

        def MultiChain_COİN_YERLESTIR():
            if TST.MultiChain_INT == 1:
                self.SORUMLU_COİN_ONE = "BTCBUSD"

        def MultiChain_AL_YERLESTIR():
            if self.SORUMLU_COİN_ONE == "BTCBUSD":
                self.SORUMLU_COİN_ONE_AL = TST.BTC_KARMA_BUY

        def MultiChain_SAT_YERLESTIR():
            if self.SORUMLU_COİN_ONE == "BTCBUSD":
                self.SORUMLU_COİN_ONE_SAT = TST.BTC_KARMA_SELL

        def MultiChain_Piyasa_DURUMU_YERLESTIR():
            if PİYASA_DURUMU == 1:
                self.PİYASA_DURUMU = 1
            elif PİYASA_DURUMU == 2:
                self.PİYASA_DURUMU = 2
            elif PİYASA_DURUMU == 3:
                self.PİYASA_DURUMU = 3
            elif PİYASA_DURUMU == 4:
                self.PİYASA_DURUMU = 4
            elif PİYASA_DURUMU == 5:
                self.PİYASA_DURUMU = 5
            elif PİYASA_DURUMU == 6:
                self.PİYASA_DURUMU = 6
            elif PİYASA_DURUMU == 7:
                self.PİYASA_DURUMU = 7
            elif PİYASA_DURUMU == 8:
                self.PİYASA_DURUMU = 8

        def MultiChain_STOP_FUNCTİON():
            if PİYASA_DURUMU == 3 or 4:
                self.NOTR_STOP += True

        def MultiChain_WAVY_FUNCTİON():
            if PİYASA_DURUMU == 1 or 2:
                self.WAVY_STOP += True

        MultiChain_WAVY_FUNCTİON()
        MultiChain_COİN_YERLESTIR()
        MultiChain_AL_YERLESTIR()
        MultiChain_SAT_YERLESTIR()
        MultiChain_Piyasa_DURUMU_YERLESTIR()
        MultiChain_STOP_FUNCTİON()
    def MultiChain(self):
        def MultiChain_Algorithm(LossAlgorithm=bool, ControlAlgorithm=bool, SELL_OpportunityAlgorithm=bool, BUY_OpportunityAlgorithm=bool, WavyAlgorithm=bool):
            print("{} Crypto ROB (I) ON".format(Fore.RED+"[DEMO]"))
            STEP = 0
            BUY_PRİCE = 0
            BUY_QUANTİTY = 0
            SELL_PRİCE = 0
            SELL_BALANCE = 0
            LOOP_RETURN = False

            def Return_Fee():
                def Return_Fee_CONTROL():
                    if self.KAZANC_BALANCE > 10000:
                        return 25
                    elif self.KAZANC_BALANCE > 7500:
                        return 27.5
                    elif self.KAZANC_BALANCE > 5000:
                        return 30
                    elif self.KAZANC_BALANCE > 3500:
                        return 33.3
                    elif self.KAZANC_BALANCE > 1500:
                        return 37.5
                    else:
                        return 40

                try:
                    if self.KAZANILAN_BAKİYE < self.KAZANC_BALANCE:
                        pass
                    else:
                        KAAR = self.KAZANILAN_BAKİYE  # ANLIK BAKİYEMİZ
                        KAAR_HESAPLAYICISI = self.KAZANC_BALANCE

                        KAZANC = KAAR - KAAR_HESAPLAYICISI
                        KAZANC_NEW = float(KAZANC * Return_Fee_CONTROL()) / 100

                        self.Fee += KAZANC_NEW
                        self.KAZANC_BALANCE = self.KAZANILAN_BAKİYE
                except:
                    print("{} Fee Error".format(DEMO))
            def Multi_Chain_Hedef_Options():
                try:
                    if float(self.KAZANILAN_BAKİYE) >= float(self.HEDEF):
                        try:
                            print("{} Emirler İptal Edildi.".format(DEMO))
                        except:
                            pass
                        print("""{}
                                    Crypto ROB The Best Trading !

                                    Aim Succesful ! Setting Goals for the Game Again !



                                    Crypto ROB The Best Trading !

                                    Hedef Tamamlandı ! Tekrar Soyguna Başlamak İçin Hedefinizi Belirleyin !
                                                                                                                        """.format(Fore.BLUE+"[DEMO]"))

                        print("\nCrypto ROB The Best Trading !")
                        time.sleep(1)
                        sys.exit()
                        # os.system("shutdown /s /t 2")
                except:
                    print("{} Hedef Options Error".format(DEMO))
            def Multi_Chain_BUY_START():
                nonlocal BUY_PRİCE, BUY_QUANTİTY
                while True:
                    try:
                        ANLIK = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])
                        Quantity = self.KAZANILAN_BAKİYE / float(ANLIK)
                        PRİCE = float(ANLIK) - self.SORUMLU_COİN_ONE_AL

                        BUY_PRİCE = PRİCE
                        BUY_QUANTİTY = Quantity
                        self.KAZANILAN_BAKİYE -= self.KAZANILAN_BAKİYE
                        print("{} Fiyatı : {} | Varlık : {} 'dan Alım Emri Verilmiştir.".format(DEMO, round(PRİCE, 3), round(Quantity, 6)))
                    except:
                        break
                    break
            def Multi_Chain_SELL_START():
                nonlocal SELL_PRİCE, SELL_BALANCE
                while True:
                    try:
                        NEW_BALANCE = BUY_QUANTİTY
                        ANLIK = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])
                        PRİCE = float(ANLIK) + self.SORUMLU_COİN_ONE_SAT
                        print("{} Fiyatı : {} | Varlık : {} 'dan Satım Emri Verilmiştir.".format(DEMO, round(PRİCE, 3), round(NEW_BALANCE, 6)))

                        SELL_PRİCE = PRİCE
                        SELL_BALANCE = NEW_BALANCE
                    except:
                        break
                    break

            while True:
                time.sleep(2)
                Multi_Chain_Hedef_Options()

                if LOOP_RETURN == True:
                    time.sleep(1)
                    break

                # CONTROL ALGORİTMA ELSE BLOĞUNDA KALDIK

                elif ControlAlgorithm == True and self.CANCEL_CONTROL == 1:
                    time.sleep(2)
                    if not(self.KAZANILAN_BAKİYE > 10):
                        if (float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice']) * 98.5) / 100 > float(self.Opportunity_TETİKLE):
                            time.sleep(2)
                            print("{} Control Algorithm I".format(DEMO))
                            CONTROL_SELL_PRİCE = 0
                            CONTROL_SELL_BALANCE = 0
                            def ControlAlgorithm_I():
                                nonlocal CONTROL_SELL_PRİCE, CONTROL_SELL_BALANCE
                                while True:
                                    try:
                                        NEW_BALANCE = float(SELL_BALANCE)
                                        ANLIK = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])
                                        PRİCE = float(ANLIK) + (float(ANLIK * 100.7) / 100)
                                        print("{} Fiyatı : {} | Varlık : {} 'dan Satım Emri Verilmiştir.".format(DEMO, round(PRİCE, 3), round(NEW_BALANCE, 6)))
                                        CONTROL_SELL_PRİCE += PRİCE
                                        CONTROL_SELL_BALANCE += NEW_BALANCE
                                    except:
                                        break
                                    break

                            while True:
                                try:
                                    ControlAlgorithm_I()
                                    break
                                except:
                                    print("Tekrardan Bağlantı Sağlanılıyor.")

                            RETURN_MAX_ZARAR = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])
                            while True:
                                PRİCE = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])
                                try:
                                    if PRİCE > CONTROL_SELL_PRİCE:
                                        self.KAZANILAN_BAKİYE += PRİCE * CONTROL_SELL_BALANCE
                                        self.CANCEL_CONTROL -= 1
                                        self.CANCEL_CONTROL -= self.CANCEL_CONTROL
                                        Return_Fee()
                                        print("{} Yeni Bakiyeniz : {}$".format(DEMO, round(self.KAZANILAN_BAKİYE, 2)))
                                        print("{} Ödemeniz Gereken Komisyon : {}$".format(DEMO, round(self.Fee, 2)))
                                        break
                                    elif float(RETURN_MAX_ZARAR * 98.5) / 100 > float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice']):
                                        self.KAZANILAN_BAKİYE += PRİCE * CONTROL_SELL_BALANCE
                                        THREE_STOP += True
                                        self.CANCEL_CONTROL -= 1
                                        self.CANCEL_CONTROL -= self.CANCEL_CONTROL
                                        print("{} Emirler İptal Edildi.".format(DEMO))
                                        print("{} Stop Emri Verildi.".format(DEMO))
                                        print("{} Yeni Bakiyeniz : {}$".format(DEMO, round(self.KAZANILAN_BAKİYE, 2)))
                                        break
                                    else:
                                        print("{} {}:{}  | Waiting Sell".format(DEMO, time.gmtime()[3]+3, time.gmtime()[4]))
                                        time.sleep(1)

                                except:
                                    print("Tekrardan Bağlantı Sağlanılıyor.")
                        elif (float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice']) * 99) / 100 > float(self.Opportunity_TETİKLE):
                            time.sleep(2)
                            print("{} Control Algorithm II".format(DEMO))
                            CONTROL_SELL_PRİCE_II = 0
                            CONTROL_SELL_BALANCE_II = 0
                            def ControlAlgorithm_II():
                                nonlocal CONTROL_SELL_PRİCE_II, CONTROL_SELL_BALANCE_II
                                while True:
                                    try:
                                        NEW_BALANCE = float(SELL_BALANCE)
                                        ANLIK = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])
                                        PRİCE = float(ANLIK) + (float(ANLIK * 100.5) / 100)
                                        print("{} Fiyatı : {} | Varlık : {} 'dan Satım Emri Verilmiştir.".format(DEMO, round(PRİCE, 3), round(NEW_BALANCE, 6)))
                                        CONTROL_SELL_PRİCE_II += PRİCE
                                        CONTROL_SELL_BALANCE_II += NEW_BALANCE
                                    except:
                                        break
                                    break

                            while True:
                                try:
                                    ControlAlgorithm_II()
                                    break
                                except:
                                    print("Tekrardan Bağlantı Sağlanılıyor.")

                            RETURN_MAX_ZARAR = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])
                            while True:
                                PRİCE = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])
                                try:

                                    if PRİCE > CONTROL_SELL_PRİCE_II:
                                        self.KAZANILAN_BAKİYE += PRİCE * CONTROL_SELL_BALANCE_II
                                        self.CANCEL_CONTROL -= 1
                                        self.CANCEL_CONTROL -= self.CANCEL_CONTROL
                                        Return_Fee()
                                        print("{} Yeni Bakiyeniz : {}$".format(DEMO, round(self.KAZANILAN_BAKİYE, 2)))
                                        print("{} Ödemeniz Gereken Komisyon : {}$".format(DEMO, round(self.Fee, 2)))
                                        break
                                    elif float(RETURN_MAX_ZARAR * 98.5) / 100 > float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice']):
                                        self.KAZANILAN_BAKİYE += PRİCE * CONTROL_SELL_BALANCE_II
                                        THREE_STOP += True
                                        self.CANCEL_CONTROL -= 1
                                        self.CANCEL_CONTROL -= self.CANCEL_CONTROL
                                        print("{} Emirler İptal Edildi.".format(DEMO))
                                        print("{} Stop Emri Verildi.".format(DEMO))
                                        print("{} Yeni Bakiyeniz : {}$".format(DEMO, round(self.KAZANILAN_BAKİYE, 2)))
                                        break
                                    else:
                                        print("Control Algorithm II")
                                        print("{} {}:{}  | Waiting Sell".format(DEMO, time.gmtime()[3]+3, time.gmtime()[4]))
                                        time.sleep(1)

                                except:
                                    print("Tekrardan Bağlantı Sağlanılıyor.")
                        elif (float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice']) * 99.5) / 100 > float(self.Opportunity_TETİKLE):
                            time.sleep(2)
                            print("{} Control Algorithm III".format(DEMO))
                            CONTROL_SELL_PRİCE_III = 0
                            CONTROL_SELL_BALANCE_III = 0

                            def ControlAlgorithm_III():
                                nonlocal CONTROL_SELL_PRİCE_III, CONTROL_SELL_BALANCE_III
                                while True:
                                    try:
                                        NEW_BALANCE = float(SELL_BALANCE)
                                        ANLIK = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])
                                        PRİCE = float(ANLIK) + (float(ANLIK * 100.5) / 100)
                                        print("{} Fiyatı : {} | Varlık : {} 'dan Satım Emri Verilmiştir.".format(DEMO, round(PRİCE, 3), round(NEW_BALANCE, 6)))
                                        CONTROL_SELL_PRİCE_III += PRİCE
                                        CONTROL_SELL_BALANCE_III += NEW_BALANCE
                                    except:
                                        break
                                    break

                            while True:
                                try:
                                    ControlAlgorithm_III()
                                    break
                                except:
                                    print("Tekrardan Bağlantı Sağlanılıyor.")

                            RETURN_MAX_ZARAR = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])
                            while True:
                                PRİCE = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])
                                try:
                                    if PRİCE > CONTROL_SELL_PRİCE_III:
                                        self.KAZANILAN_BAKİYE += PRİCE * CONTROL_SELL_BALANCE_III
                                        self.CANCEL_CONTROL -= 1
                                        self.CANCEL_CONTROL -= self.CANCEL_CONTROL
                                        Return_Fee()
                                        print("{} Yeni Bakiyeniz : {}$".format(DEMO, round(self.KAZANILAN_BAKİYE, 2)))
                                        print("{} Ödemeniz Gereken Komisyon : {}$".format(DEMO, round(self.Fee, 2)))
                                        break
                                    elif float(RETURN_MAX_ZARAR * 98.5) / 100 > float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice']):
                                        self.KAZANILAN_BAKİYE += PRİCE * CONTROL_SELL_BALANCE_III
                                        THREE_STOP += True
                                        self.CANCEL_CONTROL -= 1
                                        self.CANCEL_CONTROL -= self.CANCEL_CONTROL
                                        print("{} Emirler İptal Edildi.".format(DEMO))
                                        print("{} Stop Emri Verildi.".format(DEMO))
                                        print("{} Yeni Bakiyeniz : {}$".format(DEMO, round(self.KAZANILAN_BAKİYE, 2)))
                                        break
                                    else:
                                        print("Control Algorithm III")
                                        print("{} {}:{}  | Waiting Sell".format(DEMO, time.gmtime()[3] + 3, time.gmtime()[4]))
                                        time.sleep(1)

                                except:
                                    print("Tekrardan Bağlantı Sağlanılıyor.")
                        else:
                            self.CANCEL_CONTROL -= 1
                            print("{} Sell ControlAlgorithm STOP !".format(DEMO))
                    else:
                        if (self.Opportunity_TETİKLE * 101.5) / 100 < (float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])):
                            time.sleep(2)
                            print("{} Control Algorithm I".format(DEMO))
                            CONTROL_BUY_BALANCE = 0
                            CONTROL_BUY_PRİCE = 0
                            def ControlAlgorithm_I():
                                nonlocal CONTROL_BUY_PRİCE,CONTROL_BUY_BALANCE
                                while True:
                                    try:
                                        ANLIK = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])
                                        Quantity = self.KAZANILAN_BAKİYE / float(ANLIK)
                                        PRİCE = float(ANLIK * 99.3) / 100
                                        print("{} Fiyatı : {} | Varlık : {} 'dan Alım Emri Verilmiştir.".format(DEMO, round(PRİCE, 3), round(NEW_BALANCE, 6)))

                                        CONTROL_BUY_PRİCE += PRİCE
                                        CONTROL_BUY_BALANCE += NEW_BALANCE
                                        self.KAZANILAN_BAKİYE = 0
                                    except:
                                        break
                                    break

                            while True:
                                try:
                                    ControlAlgorithm_I()
                                    break
                                except:
                                    print("{} Tekrardan Bağlantı Sağlanılıyor.".format(DEMO))

                            while True:
                                try:
                                    if float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice']) < CONTROL_BUY_PRİCE:
                                        print("{} Satın Alım Başarılı !".format(DEMO))
                                        break
                                    else:
                                        time.sleep(1)
                                        print("{} {}:{}  | Waiting Buy.".format(DEMO,time.gmtime()[3]+3,time.gmtime()[4]))
                                except:
                                    print("{} Tekrardan Bağlantı Sağlanılıyor.".format(DEMO))
                        elif (self.Opportunity_TETİKLE * 101) / 100 < (float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])):
                            time.sleep(2)
                            print("{} Control Algorithm II".format(DEMO))
                            CONTROL_BUY_BALANCE_II = 0
                            CONTROL_BUY_PRİCE_II = 0

                            def ControlAlgorithm_II():
                                nonlocal CONTROL_BUY_PRİCE_II, CONTROL_BUY_BALANCE_II
                                while True:
                                    try:
                                        ANLIK = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])
                                        Quantity = self.KAZANILAN_BAKİYE / float(ANLIK)
                                        PRİCE = float(ANLIK * 99.5) / 100
                                        print("{} Fiyatı : {} | Varlık : {} 'dan Alım Emri Verilmiştir.".format(DEMO, round(PRİCE, 3), round(NEW_BALANCE, 6)))

                                        CONTROL_BUY_PRİCE_II += PRİCE
                                        CONTROL_BUY_BALANCE_II += NEW_BALANCE
                                        self.KAZANILAN_BAKİYE = 0
                                    except:
                                        break
                                    break

                            while True:
                                try:
                                    ControlAlgorithm_II()
                                    break
                                except:
                                    print("{} Tekrardan Bağlantı Sağlanılıyor.".format(DEMO))

                            while True:
                                try:
                                    if float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice']) < CONTROL_BUY_PRİCE_II:
                                        print("{} Satın Alım Başarılı !".format(DEMO))
                                        break
                                    else:
                                        time.sleep(1)
                                        print("{} {}:{}  | Waiting Buy.".format(DEMO, time.gmtime()[3] + 3, time.gmtime()[4]))
                                except:
                                    print("{} Tekrardan Bağlantı Sağlanılıyor.".format(DEMO))
                        elif (self.Opportunity_TETİKLE * 100.5) / 100 < (float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])):
                            time.sleep(2)
                            print("{} Control Algorithm III".format(DEMO))
                            CONTROL_BUY_BALANCE_III = 0
                            CONTROL_BUY_PRİCE_III = 0

                            def ControlAlgorithm_III(Price):
                                nonlocal CONTROL_BUY_PRİCE_III, CONTROL_BUY_BALANCE_III
                                while True:
                                    try:
                                        ANLIK = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])
                                        Quantity = self.KAZANILAN_BAKİYE / float(ANLIK)
                                        PRİCE = Price
                                        print("{} Fiyatı : {} | Varlık : {} 'dan Alım Emri Verilmiştir.".format(DEMO, round(PRİCE, 3), round(NEW_BALANCE, 6)))

                                        CONTROL_BUY_PRİCE_III += PRİCE
                                        CONTROL_BUY_BALANCE_III += NEW_BALANCE
                                        self.KAZANILAN_BAKİYE = 0
                                    except:
                                        break
                                    break

                            while True:
                                try:
                                    ControlAlgorithm_III(Price=self.Opportunity_TETİKLE)
                                    break
                                except:
                                    print("{} Tekrardan Bağlantı Sağlanılıyor.".format(DEMO))

                            while True:
                                try:
                                    if float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice']) < CONTROL_BUY_PRİCE_III:
                                        print("{} Satın Alım Başarılı !".format(DEMO))
                                        break
                                    else:
                                        time.sleep(1)
                                        print("{} {}:{}  | Waiting Buy.".format(DEMO, time.gmtime()[3] + 3, time.gmtime()[4]))
                                except:
                                    print("{} Tekrardan Bağlantı Sağlanılıyor.".format(DEMO))
                        else:
                            self.CANCEL_CONTROL -= 1
                            print("{} Buy ControlAlgorithm STOP !".format(DEMO))
                elif WavyAlgorithm == True and self.WAVY_STOP == True and BUSD > 10 and (self.BUY_Opportunity == 2 or self.SELL_Opportunity == 2):
                    print("Special WavyAlgorithm Activate !")
                    BUY_ORDER_PRİCE = 0
                    # ------------------------
                    BALANCE = self.KAZANILAN_BAKİYE
                    BALANCE_ONE = BALANCE / 4
                    BALANCE_TWO = BALANCE / 4
                    BALANCE_THREE = BALANCE / 4
                    BALANCE_FOUR = BALANCE / 4

                    # CONTROLLER
                    # -------------------------------------------
                    BUY_ONE_CONTROL = False
                    BUY_TWO_CONTROL = False
                    BUY_THREE_CONTROL = False
                    BUY_FOUR_CONTROL = False
                    # -------------------------------------------
                    SELL_ONE_CONTROL = False
                    SELL_TWO_CONTROL = False
                    SELL_THREE_CONTROL = False
                    SELL_FOUR_CONTROL = False

                    # ENGİNNER
                    def Enginner():
                        try:
                            nonlocal BUY_ORDER_PRİCE
                            ANLIK = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])
                            BUY_WAVY_CRYPTO_GENERATOR = self.KAZANILAN_BAKİYE / ANLIK
                            # ---------------------------------------------------------------
                            if BUY_WAVY_CRYPTO_GENERATOR * ((ANLIK * 100.1) / 100) >= self.HEDEF:
                                BUY_ORDER_PRİCE += (ANLIK * 99.9) / 100
                            elif BUY_WAVY_CRYPTO_GENERATOR * ((ANLIK * 100.2) / 100) >= self.HEDEF:
                                BUY_ORDER_PRİCE += (ANLIK * 99.8) / 100
                            # ---------------------------------------------------------------
                            elif BUY_WAVY_CRYPTO_GENERATOR * ((ANLIK * 100.3) / 100) >= self.HEDEF:
                                BUY_ORDER_PRİCE += (ANLIK * 99.7) / 100
                            elif BUY_WAVY_CRYPTO_GENERATOR * ((ANLIK * 100.4) / 100) >= self.HEDEF:
                                BUY_ORDER_PRİCE += (ANLIK * 99.6) / 100
                            # ---------------------------------------------------------------
                            elif BUY_WAVY_CRYPTO_GENERATOR * ((ANLIK * 100.5) / 100) >= self.HEDEF:
                                BUY_ORDER_PRİCE += (ANLIK * 99.5) / 100
                            elif BUY_WAVY_CRYPTO_GENERATOR * ((ANLIK * 100.6) / 100) >= self.HEDEF:
                                BUY_ORDER_PRİCE += (ANLIK * 99.4) / 100
                            # ---------------------------------------------------------------
                            elif BUY_WAVY_CRYPTO_GENERATOR * ((ANLIK * 100.7) / 100) >= self.HEDEF:
                                BUY_ORDER_PRİCE += (ANLIK * 99.3) / 100
                            elif BUY_WAVY_CRYPTO_GENERATOR * ((ANLIK * 100.8) / 100) >= self.HEDEF:
                                BUY_ORDER_PRİCE += (ANLIK * 99.2) / 100
                            # -------------------------------------------------------------
                            elif BUY_WAVY_CRYPTO_GENERATOR * ((ANLIK * 100.9) / 100) >= self.HEDEF:
                                BUY_ORDER_PRİCE += (ANLIK * 99.1) / 100
                            elif BUY_WAVY_CRYPTO_GENERATOR * ((ANLIK * 101.0) / 100) >= self.HEDEF:
                                BUY_ORDER_PRİCE += (ANLIK * 99.0) / 100
                            # -------------------------------------------------------------
                            elif BUY_WAVY_CRYPTO_GENERATOR * ((ANLIK * 101.1) / 100) >= self.HEDEF:
                                BUY_ORDER_PRİCE += (ANLIK * 98.9) / 100
                            elif BUY_WAVY_CRYPTO_GENERATOR * ((ANLIK * 101.2) / 100) >= self.HEDEF:
                                BUY_ORDER_PRİCE += (ANLIK * 98.8) / 100
                            # -------------------------------------------------------------
                        except:
                            print("Wavy Algorithm Try Again !")
                        finally:
                            print("Wavy Algorithm Successful !")
                            print("Wavy MOD ON !")
                            print("Center Price : ", BUY_ORDER_PRİCE)

                    # ORDERS CENTER
                    CONTROLLER_FEE = 0
                    Wavy_STOP = False
                    Wavy_Default_ONE = False
                    Wavy_Default_TWO = False
                    Wavy_Default_THREE = False
                    Wavy_Default_FOUR = False
                    Enginner()
                    # -------------------------------------------

                    BUY_ORDER_ONE = (BUY_ORDER_PRİCE * 99.9) / 100
                    BUY_ORDER_TWO = (BUY_ORDER_PRİCE * 99.8) / 100
                    BUY_ORDER_THREE = (BUY_ORDER_PRİCE * 99.7) / 100
                    BUY_ORDER_FOUR = (BUY_ORDER_PRİCE * 99.6) / 100

                    # -------------------------------------------

                    SELL_ORDER_ONE = (BUY_ORDER_PRİCE * 100.0) / 100
                    SELL_ORDER_TWO = (BUY_ORDER_PRİCE * 99.9) / 100
                    SELL_ORDER_THREE = (BUY_ORDER_PRİCE * 99.8) / 100
                    SELL_ORDER_FOUR = (BUY_ORDER_PRİCE * 99.7) / 100

                    # -------------------------------------------


                    Wavy_BUY_ONE_BALANCE = 0
                    Wavy_BUY_ONE_PRİCE = 0

                    Wavy_BUY_TWO_BALANCE = 0
                    Wavy_BUY_TWO_PRİCE = 0

                    Wavy_BUY_THREE_BALANCE = 0
                    Wavy_BUY_THREE_PRİCE = 0

                    Wavy_BUY_FOUR_BALANCE = 0
                    Wavy_BUY_FOUR_PRİCE = 0


                    # -------------------------------------------

                    Wavy_SELL_ONE_BALANCE = 0
                    Wavy_SELL_ONE_PRİCE = 0

                    Wavy_SELL_TWO_BALANCE = 0
                    Wavy_SELL_TWO_PRİCE = 0

                    Wavy_SELL_THREE_BALANCE = 0
                    Wavy_SELL_THREE_PRİCE = 0

                    Wavy_SELL_FOUR_BALANCE = 0
                    Wavy_SELL_FOUR_PRİCE = 0

                    # -------------------------------------------

                    Wavy_Default_BALANCE_BUY = 0
                    Wavy_Default_PRİCE_BUY = 0

                    Wavy_Default_BALANCE_SELL = 0
                    Wavy_Default_PRİCE_SELL = 0

                    # -------------------------------------------

                    class Wavy:
                        def WavyAlgorithm_I_BUY(Balance=BALANCE_ONE):
                            nonlocal BUY_ORDER_ONE, BUY_ONE_CONTROL, SELL_ONE_CONTROL, Wavy_BUY_ONE_BALANCE, Wavy_BUY_ONE_PRİCE
                            while True:
                                try:
                                    ANLIK = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])
                                    Quantity = Balance / float(ANLIK)
                                    PRİCE = int(BUY_ORDER_ONE)

                                    Wavy_BUY_ONE_PRİCE += PRİCE
                                    Wavy_BUY_ONE_BALANCE += Quantity
                                    self.KAZANILAN_BAKİYE -= self.KAZANILAN_BAKİYE
                                    BUY_ONE_CONTROL += True
                                    SELL_ONE_CONTROL += True
                                    print("Wavy Buy I ON")
                                    print("{} Fiyatı : {} | Varlık : {} 'dan Alım Emri Verilmiştir.".format(DEMO, round(PRİCE, 3), round(Quantity, 6)))
                                except:
                                    break
                                break
                        def WavyAlgorithm_II_BUY(Balance=BALANCE_TWO):
                            nonlocal BUY_ORDER_TWO, BUY_TWO_CONTROL, SELL_TWO_CONTROL, Wavy_BUY_TWO_BALANCE , Wavy_BUY_TWO_PRİCE
                            while True:
                                try:
                                    ANLIK = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])
                                    Quantity = Balance / float(ANLIK)
                                    PRİCE = int(BUY_ORDER_TWO)

                                    Wavy_BUY_TWO_PRİCE += PRİCE
                                    Wavy_BUY_TWO_BALANCE += Quantity
                                    self.KAZANILAN_BAKİYE -= self.KAZANILAN_BAKİYE
                                    BUY_TWO_CONTROL += True
                                    SELL_TWO_CONTROL += True
                                    print("Wavy Buy II ON")
                                    print("{} Fiyatı : {} | Varlık : {} 'dan Alım Emri Verilmiştir.".format(DEMO, round(PRİCE, 3), round(Quantity, 6)))
                                except:
                                    break
                                break
                        def WavyAlgorithm_III_BUY(Balance=BALANCE_THREE):
                            nonlocal BUY_ORDER_THREE, BUY_THREE_CONTROL, SELL_THREE_CONTROL, Wavy_BUY_THREE_BALANCE , Wavy_BUY_THREE_PRİCE
                            while True:
                                try:
                                    ANLIK = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])
                                    Quantity = Balance / float(ANLIK)
                                    PRİCE = int(BUY_ORDER_THREE)

                                    Wavy_BUY_THREE_PRİCE += PRİCE
                                    Wavy_BUY_THREE_BALANCE += Quantity
                                    self.KAZANILAN_BAKİYE -= self.KAZANILAN_BAKİYE
                                    BUY_THREE_CONTROL += True
                                    SELL_THREE_CONTROL += True
                                    print("Wavy Buy III ON")
                                    print("{} Fiyatı : {} | Varlık : {} 'dan Alım Emri Verilmiştir.".format(DEMO, round(PRİCE, 3), round(Quantity, 6)))
                                except:
                                    break
                                break
                        def WavyAlgorithm_IV_BUY(Balance=BALANCE_FOUR):
                            nonlocal BUY_ORDER_FOUR, BUY_FOUR_CONTROL, SELL_FOUR_CONTROL, Wavy_BUY_FOUR_BALANCE , Wavy_BUY_FOUR_PRİCE
                            while True:
                                try:
                                    ANLIK = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])
                                    Quantity = Balance / float(ANLIK)
                                    PRİCE = int(BUY_ORDER_FOUR)

                                    Wavy_BUY_FOUR_PRİCE += PRİCE
                                    Wavy_BUY_FOUR_BALANCE += Quantity
                                    self.KAZANILAN_BAKİYE -= self.KAZANILAN_BAKİYE
                                    BUY_FOUR_CONTROL += True
                                    SELL_FOUR_CONTROL += True
                                    print("Wavy Buy IV ON")
                                    print("{} Fiyatı : {} | Varlık : {} 'dan Alım Emri Verilmiştir.".format(DEMO, round(PRİCE, 3), round(Quantity, 6)))
                                except:
                                    break
                                break


                        def WavyAlgorithm_I_SELL(Price=SELL_ORDER_ONE):
                            nonlocal BUY_ONE_CONTROL, SELL_ONE_CONTROL, Wavy_SELL_ONE_PRİCE, Wavy_SELL_ONE_BALANCE
                            while True:
                                try:
                                    NEW_BALANCE = Wavy_BUY_ONE_BALANCE
                                    ANLIK = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])
                                    PRİCE = Price

                                    Wavy_SELL_ONE_PRİCE = PRİCE
                                    Wavy_SELL_ONE_BALANCE = NEW_BALANCE
                                    BUY_ONE_CONTROL += False
                                    SELL_ONE_CONTROL += False
                                    print("Wavy Sell I ON")
                                    print("{} Fiyatı : {} | Varlık : {} 'dan Satım Emri Verilmiştir.".format(DEMO, round(PRİCE, 3), round(NEW_BALANCE, 6)))
                                except:
                                    break
                                break
                        def WavyAlgorithm_II_SELL(Price=SELL_ORDER_TWO):
                            nonlocal BUY_TWO_CONTROL, SELL_TWO_CONTROL, Wavy_SELL_TWO_PRİCE, Wavy_SELL_TWO_BALANCE
                            while True:
                                try:
                                    NEW_BALANCE = Wavy_BUY_TWO_BALANCE
                                    ANLIK = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])
                                    PRİCE = Price

                                    Wavy_SELL_TWO_PRİCE = PRİCE
                                    Wavy_SELL_TWO_BALANCE = NEW_BALANCE
                                    BUY_TWO_CONTROL += False
                                    SELL_TWO_CONTROL += False
                                    print("Wavy Sell II ON")
                                    print("{} Fiyatı : {} | Varlık : {} 'dan Satım Emri Verilmiştir.".format(DEMO, round(PRİCE, 3), round(NEW_BALANCE, 6)))
                                except:
                                    break
                                break
                        def WavyAlgorithm_III_SELL(Price=SELL_ORDER_THREE):
                            nonlocal BUY_THREE_CONTROL, SELL_THREE_CONTROL, Wavy_SELL_THREE_PRİCE, Wavy_SELL_THREE_BALANCE
                            while True:
                                try:
                                    NEW_BALANCE = Wavy_BUY_THREE_BALANCE
                                    ANLIK = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])
                                    PRİCE = Price

                                    Wavy_SELL_THREE_PRİCE = PRİCE
                                    Wavy_SELL_THREE_BALANCE = NEW_BALANCE
                                    BUY_THREE_CONTROL += False
                                    SELL_THREE_CONTROL += False
                                    print("Wavy Sell III ON")
                                    print("{} Fiyatı : {} | Varlık : {} 'dan Satım Emri Verilmiştir.".format(DEMO, round(PRİCE, 3), round(NEW_BALANCE, 6)))
                                except:
                                    break
                                break
                        def WavyAlgorithm_IV_SELL(Price=SELL_ORDER_FOUR):
                            nonlocal BUY_FOUR_CONTROL, SELL_FOUR_CONTROL, Wavy_SELL_FOUR_PRİCE, Wavy_SELL_FOUR_BALANCE
                            while True:
                                try:
                                    NEW_BALANCE = Wavy_BUY_FOUR_BALANCE
                                    ANLIK = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])
                                    PRİCE = Price

                                    Wavy_SELL_FOUR_PRİCE = PRİCE
                                    Wavy_SELL_FOUR_BALANCE = NEW_BALANCE
                                    BUY_FOUR_CONTROL += False
                                    SELL_FOUR_CONTROL += False
                                    print("Wavy Sell IV ON")
                                    print("{} Fiyatı : {} | Varlık : {} 'dan Satım Emri Verilmiştir.".format(DEMO, round(PRİCE, 3), round(NEW_BALANCE, 6)))
                                except:
                                    break
                                break

                    class Wavy_Default:
                        def Wavy_NORMAL_BUYİNG():
                            nonlocal Wavy_Default_PRİCE_BUY, Wavy_Default_BALANCE_BUY
                            while True:
                                try:
                                    Wavy_Default_BALANCE_BUY -= Wavy_Default_BALANCE_BUY
                                    Wavy_Default_PRİCE_BUY -= Wavy_Default_PRİCE_BUY

                                    ANLIK = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])
                                    Quantity = self.KAZANILAN_BAKİYE / float(ANLIK)
                                    PRİCE = float(ANLIK * 99.9) / 100

                                    Wavy_Default_BALANCE_BUY += Quantity
                                    Wavy_Default_PRİCE_BUY += PRİCE
                                    self.KAZANILAN_BAKİYE -= self.KAZANILAN_BAKİYE
                                    print("Wavy Buy Default I ON")
                                    print("{} Fiyatı : {} | Varlık : {} 'dan Alım Emri Verilmiştir.".format(DEMO, round(PRİCE, 3), round(Quantity, 6)))
                                except:
                                    break
                                break
                        def Wavy_NORMAL_SELLİNG():
                            nonlocal Wavy_Default_PRİCE_SELL, Wavy_Default_BALANCE_SELL, Wavy_Default_BALANCE_BUY
                            while True:
                                try:
                                    Wavy_Default_BALANCE_SELL -= Wavy_Default_BALANCE_SELL
                                    Wavy_Default_PRİCE_SELL -= Wavy_Default_PRİCE_SELL

                                    ANLIK = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])
                                    NEW_BALANCE = float(Wavy_Default_BALANCE_BUY)
                                    PRİCE = float(ANLIK * 100.1) / 100

                                    Wavy_Default_PRİCE_SELL += PRİCE
                                    Wavy_Default_BALANCE_SELL += NEW_BALANCE
                                except:
                                    break
                                break

                    ONE_END = False
                    TWO_END = False
                    THREE_END = False
                    FOUR_END = False
                    while True:
                        Loss_SECOND = 0

                        if Wavy_STOP == True:
                            break

                        if CONTROLLER_FEE == 5:
                            print("{} Tüm Emirler İptal Edildi.".format(DEMO))
                            Fee = (self.KAZANC_BALANCE * 100.5) / 100
                            self.KAZANILAN_BAKİYE -= self.KAZANILAN_BAKİYE
                            self.KAZANILAN_BAKİYE += Fee
                            Return_Fee()
                            break

                        while True:
                            time.sleep(1)
                            Loss_SECOND += 1
                            ANLIK = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])
                            if Loss_SECOND == 2:
                                break

                            try:
                                if Wavy_Default_ONE == False:

                                    if BUY_ONE_CONTROL != True:
                                        Wavy.WavyAlgorithm_I_BUY()
                                        print("{} Wavy Buy Try Again I".format(DEMO))
                                        break

                                    elif ANLIK < Wavy_BUY_ONE_PRİCE:
                                        Wavy.WavyAlgorithm_I_SELL()
                                        print("{} Wavy Sell Try Again I".format(DEMO))
                                        CONTROLLER_FEE += 1
                                        ONE_END += True
                                        break

                                    elif ONE_END == True and ANLIK > Wavy_SELL_ONE_PRİCE:
                                        self.KAZANILAN_BAKİYE += ANLIK * Wavy_SELL_ONE_BALANCE
                                        Wavy_Default_ONE += True
                                        print("{} Wavy Satış Başarılı".format(DEMO))
                                        print("{} Yeni Bakiyeniz : {}".format(DEMO,self.KAZANILAN_BAKİYE))
                                        break

                                elif Wavy_Default_ONE == True:

                                    if self.KAZANILAN_BAKİYE >= 10:
                                        Wavy_Default.Wavy_NORMAL_BUYİNG()
                                        print("Wavy_DEF Buy Try Again I")
                                        break

                                    elif ANLIK < Wavy_Default_PRİCE_BUY:
                                        Wavy_Default.Wavy_NORMAL_SELLİNG()
                                        print("Wavy_DEF Sell Try Again I")
                                        CONTROLLER_FEE += 1
                                        break

                            except:
                                print("WavyAlgorithm I Try Again !")

                            finally:
                                print("Multi C-ROB (I) Waiting !")
                                print("--------------------------------------")
                                print("Multi C-ROB (I) Coin: ", self.SORUMLU_COİN_ONE)
                                print("Multi C-ROB (I) Buy: ", int(BUY_ORDER_ONE), " ", int(BUY_ORDER_TWO), " ", int(BUY_ORDER_THREE), " ", int(BUY_ORDER_FOUR))
                                print("Multi C-ROB (I) Sell: ", int(SELL_ORDER_ONE), " ", int(SELL_ORDER_TWO), " ", int(SELL_ORDER_THREE), " ", int(SELL_ORDER_FOUR))
                                print("Multi C-ROB (I) Piyasa: ", Proposal.Market_STR)
                                print("Toplam İşlem Ücretiniz : ", self.Fee, end="$\n")
                                print("--------------------------------------")
                        while True:
                            time.sleep(1)
                            Loss_SECOND += 1
                            ANLIK = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])
                            if Loss_SECOND == 4:
                                break

                            try:
                                if Wavy_Default_TWO == False:

                                    if BUY_TWO_CONTROL != True:
                                        Wavy.WavyAlgorithm_II_BUY()
                                        print("{} Wavy Buy Try Again II".format(DEMO))
                                        break

                                    elif ANLIK < Wavy_BUY_TWO_PRİCE:
                                        Wavy.WavyAlgorithm_II_SELL()
                                        print("{} Wavy Sell Try Again II".format(DEMO))
                                        CONTROLLER_FEE += 1
                                        TWO_END += True
                                        break

                                    elif TWO_END == True and ANLIK > Wavy_SELL_TWO_PRİCE:
                                        self.KAZANILAN_BAKİYE += ANLIK * Wavy_SELL_TWO_BALANCE
                                        Wavy_Default_TWO += True
                                        print("{} Wavy Satış Başarılı".format(DEMO))
                                        print("{} Yeni Bakiyeniz : {}".format(DEMO,self.KAZANILAN_BAKİYE))
                                        break

                                elif Wavy_Default_TWO == True:

                                    if self.KAZANILAN_BAKİYE >= 10:
                                        Wavy_Default.Wavy_NORMAL_BUYİNG()
                                        print("Wavy_DEF Buy Try Again II")
                                        break

                                    elif ANLIK < Wavy_Default_PRİCE_BUY:
                                        Wavy_Default.Wavy_NORMAL_SELLİNG()
                                        print("Wavy_DEF Sell Try Again II")
                                        CONTROLLER_FEE += 1
                                        break
                            except:
                                print("WavyAlgorithm II Try Again !")

                            finally:
                                print("Multi C-ROB (I) Waiting !")
                                print("--------------------------------------")
                                print("Multi C-ROB (I) Coin: ", self.SORUMLU_COİN_ONE)
                                print("Multi C-ROB (I) Buy: ", int(BUY_ORDER_ONE), " ", int(BUY_ORDER_TWO), " ", int(BUY_ORDER_THREE), " ", int(BUY_ORDER_FOUR))
                                print("Multi C-ROB (I) Sell: ", int(SELL_ORDER_ONE), " ", int(SELL_ORDER_TWO), " ", int(SELL_ORDER_THREE), " ", int(SELL_ORDER_FOUR))
                                print("Multi C-ROB (I) Piyasa: ", Proposal.Market_STR)
                                print("Toplam İşlem Ücretiniz : ", self.Fee, end="$\n")
                                print("--------------------------------------")
                        while True:
                            time.sleep(1)
                            Loss_SECOND += 1
                            ANLIK = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])
                            if Loss_SECOND == 6:
                                break

                            try:
                                if Wavy_Default_THREE == False:

                                    if BUY_THREE_CONTROL != True:
                                        Wavy.WavyAlgorithm_III_BUY()
                                        print("{} Wavy Buy Try Again III".format(DEMO))
                                        break

                                    elif ANLIK < Wavy_BUY_THREE_PRİCE:
                                        Wavy.WavyAlgorithm_III_SELL()
                                        print("{} Wavy Sell Try Again III".format(DEMO))
                                        CONTROLLER_FEE += 1
                                        THREE_END += True
                                        break

                                    elif THREE_END == True and ANLIK > Wavy_SELL_THREE_PRİCE:
                                        self.KAZANILAN_BAKİYE += ANLIK * Wavy_SELL_THREE_BALANCE
                                        Wavy_Default_THREE += True
                                        print("{} Wavy Satış Başarılı".format(DEMO))
                                        print("{} Yeni Bakiyeniz : {}".format(DEMO,self.KAZANILAN_BAKİYE))
                                        break

                                elif Wavy_Default_THREE == True:

                                    if self.KAZANILAN_BAKİYE >= 10:
                                        Wavy_Default.Wavy_NORMAL_BUYİNG()
                                        print("Wavy_DEF Buy Try Again III")
                                        break

                                    elif ANLIK < Wavy_Default_PRİCE_BUY:
                                        Wavy_Default.Wavy_NORMAL_SELLİNG()
                                        print("Wavy_DEF Sell Try Again III")
                                        CONTROLLER_FEE += 1
                                        break
                            except:
                                print("WavyAlgorithm III Try Again !")

                            finally:
                                print("Multi C-ROB (I) Waiting !")
                                print("--------------------------------------")
                                print("Multi C-ROB (I) Coin: ", self.SORUMLU_COİN_ONE)
                                print("Multi C-ROB (I) Buy: ", int(BUY_ORDER_ONE), " ", int(BUY_ORDER_TWO), " ", int(BUY_ORDER_THREE), " ", int(BUY_ORDER_FOUR))
                                print("Multi C-ROB (I) Sell: ", int(SELL_ORDER_ONE), " ", int(SELL_ORDER_TWO), " ", int(SELL_ORDER_THREE), " ", int(SELL_ORDER_FOUR))
                                print("Multi C-ROB (I) Piyasa: ", Proposal.Market_STR)
                                print("Toplam İşlem Ücretiniz : ", self.Fee, end="$\n")
                                print("--------------------------------------")
                        while True:
                            time.sleep(1)
                            Loss_SECOND += 1
                            ANLIK = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])
                            if Loss_SECOND == 8:
                                break

                            try:
                                if Wavy_Default_FOUR == False:

                                    if BUY_FOUR_CONTROL != True:
                                        Wavy.WavyAlgorithm_IV_BUY()
                                        print("{} Wavy Buy Try Again IV".format(DEMO))
                                        break

                                    elif ANLIK < Wavy_BUY_FOUR_PRİCE:
                                        Wavy.WavyAlgorithm_IV_SELL()
                                        print("{} Wavy Sell Try Again IV".format(DEMO))
                                        CONTROLLER_FEE += 1
                                        FOUR_END += True
                                        break

                                    elif FOUR_END == True and ANLIK > Wavy_SELL_FOUR_PRİCE:
                                        self.KAZANILAN_BAKİYE += ANLIK * Wavy_SELL_FOUR_BALANCE
                                        Wavy_Default_FOUR += True
                                        print("{} Wavy Satış Başarılı".format(DEMO))
                                        print("{} Yeni Bakiyeniz : {}".format(DEMO,self.KAZANILAN_BAKİYE))
                                        break

                                elif Wavy_Default_FOUR == True:

                                    if self.KAZANILAN_BAKİYE >= 10:
                                        Wavy_Default.Wavy_NORMAL_BUYİNG()
                                        print("Wavy_DEF Buy Try Again IV")
                                        break

                                    elif ANLIK < Wavy_Default_PRİCE_BUY:
                                        Wavy_Default.Wavy_NORMAL_SELLİNG()
                                        print("Wavy_DEF Sell Try Again IV")
                                        CONTROLLER_FEE += 1
                                        break
                            except:
                                print("WavyAlgorithm IV Try Again !")

                            finally:
                                print("Multi C-ROB (I) Waiting !")
                                print("--------------------------------------")
                                print("Multi C-ROB (I) Coin: ", self.SORUMLU_COİN_ONE)
                                print("Multi C-ROB (I) Buy: ", int(BUY_ORDER_ONE), " ", int(BUY_ORDER_TWO), " ", int(BUY_ORDER_THREE), " ", int(BUY_ORDER_FOUR))
                                print("Multi C-ROB (I) Sell: ", int(SELL_ORDER_ONE), " ", int(SELL_ORDER_TWO), " ", int(SELL_ORDER_THREE), " ", int(SELL_ORDER_FOUR))
                                print("Multi C-ROB (I) Piyasa: ", Proposal.Market_STR)
                                print("Toplam İşlem Ücretiniz : ", self.Fee, end="$\n")
                                print("--------------------------------------")
                elif BUY_OpportunityAlgorithm == True and self.BUY_Opportunity == 3 and self.KAZANILAN_BAKİYE > 10:
                    while True:
                        try:
                            print("{} Buy OpportunityAlgorithm Activate !".format(DEMO))
                            ANLIK = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])
                            BUY_OpportunityAlgorithm_PRİCE = 0
                            BUY_OpportunityAlgorithm_CRYPTO_GENERATOR = self.KAZANILAN_BAKİYE / ANLIK

                            # ---------------------------------------------------------------
                            if BUY_OpportunityAlgorithm_CRYPTO_GENERATOR * ((ANLIK * 100.1) / 100) >= self.HEDEF:
                                BUY_OpportunityAlgorithm_PRİCE += (ANLIK * 99.8) / 100
                            elif BUY_OpportunityAlgorithm_CRYPTO_GENERATOR * ((ANLIK * 100.2) / 100) >= self.HEDEF:
                                BUY_OpportunityAlgorithm_PRİCE += (ANLIK * 99.7) / 100
                            # ---------------------------------------------------------------
                            elif BUY_OpportunityAlgorithm_CRYPTO_GENERATOR * ((ANLIK * 100.3) / 100) >= self.HEDEF:
                                BUY_OpportunityAlgorithm_PRİCE += (ANLIK * 99.6) / 100
                            elif BUY_OpportunityAlgorithm_CRYPTO_GENERATOR * ((ANLIK * 100.4) / 100) >= self.HEDEF:
                                BUY_OpportunityAlgorithm_PRİCE += (ANLIK * 99.5) / 100
                            # ---------------------------------------------------------------
                            elif BUY_OpportunityAlgorithm_CRYPTO_GENERATOR * ((ANLIK * 100.5) / 100) >= self.HEDEF:
                                BUY_OpportunityAlgorithm_PRİCE += (ANLIK * 99.4) / 100
                            elif BUY_OpportunityAlgorithm_CRYPTO_GENERATOR * ((ANLIK * 100.6) / 100) >= self.HEDEF:
                                BUY_OpportunityAlgorithm_PRİCE += (ANLIK * 99.3) / 100
                            # ---------------------------------------------------------------
                            elif BUY_OpportunityAlgorithm_CRYPTO_GENERATOR * ((ANLIK * 100.7) / 100) >= self.HEDEF:
                                BUY_OpportunityAlgorithm_PRİCE += (ANLIK * 99.2) / 100
                            elif BUY_OpportunityAlgorithm_CRYPTO_GENERATOR * ((ANLIK * 100.8) / 100) >= self.HEDEF:
                                BUY_OpportunityAlgorithm_PRİCE += (ANLIK * 99.1) / 100
                            # -------------------------------------------------------------
                            elif BUY_OpportunityAlgorithm_CRYPTO_GENERATOR * ((ANLIK * 100.9) / 100) >= self.HEDEF:
                                BUY_OpportunityAlgorithm_PRİCE += (ANLIK * 99.0) / 100
                            elif BUY_OpportunityAlgorithm_CRYPTO_GENERATOR * ((ANLIK * 101.0) / 100) >= self.HEDEF:
                                BUY_OpportunityAlgorithm_PRİCE += (ANLIK * 98.9) / 100
                            # -------------------------------------------------------------
                            print("Buy Opportunity Price : ", BUY_OpportunityAlgorithm_PRİCE)
                            print("Generator : ", BUY_OpportunityAlgorithm_CRYPTO_GENERATOR)
                            if BUY_OpportunityAlgorithm_PRİCE != 0:
                                Opportunity_BALANCE = 0
                                Opportunity_PRİCE = 0
                                def OpportunityAlgorithm(Price):
                                    nonlocal Opportunity_PRİCE, Opportunity_BALANCE
                                    while True:
                                        try:
                                            ANLIK = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])
                                            Quantity = self.KAZANILAN_BAKİYE / ANLIK
                                            PRİCE = Price

                                            Opportunity_PRİCE += PRİCE
                                            Opportunity_BALANCE += Quantity
                                            self.KAZANILAN_BAKİYE = 0
                                            print("{} Fiyatı : {} | Varlık : {} 'dan Alım Emri Verilmiştir.".format(DEMO, round(PRİCE, 3), round(Quantity, 6)))
                                        except:
                                            break
                                        break

                                while True:
                                    try:
                                        OpportunityAlgorithm(Price=BUY_OpportunityAlgorithm_PRİCE)
                                        break
                                    except:
                                        print("Tekrardan Bağlantı Sağlanıyor.")

                                while True:
                                    try:
                                        ANLIK = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])
                                        if ANLIK < Opportunity_PRİCE:
                                            print("{} Satın Alım Başarılı !".format(DEMO))
                                            break

                                        elif (Opportunity_PRİCE * 101.8) / 100 < ANLIK:
                                            self.KAZANILAN_BAKİYE += self.KAZANC_BALANCE
                                            print("{} Emirler İptal Edildi.".format(DEMO))
                                            print("{} Stop Emri Verildi.".format(DEMO))
                                            print("{} Yeni Bakiyeniz : {}$".format(DEMO, round(self.KAZANILAN_BAKİYE, 2)))
                                            break
                                        else:
                                            time.sleep(1)
                                            print("{} {}:{}  | Waiting Buy.".format(DEMO,time.gmtime()[3]+3,time.gmtime()[4]))
                                    except:
                                        print("{} Tekrardan Bağlantı Sağlanılıyor.".format(DEMO))
                            else:
                                self.BUY_Opportunity -= 3
                            break
                        except:
                            print("{} Buy OpportunityAlgorithm Error ! ".format(DEMO))
                elif SELL_OpportunityAlgorithm == True and self.SELL_Opportunity == 3 and not(self.KAZANILAN_BAKİYE > 10):
                    try:
                        print("{} Sell OpportunityAlgorithm Activate !".format(DEMO))
                        SELL_ORDER_PRİCE = 0
                        BALANCE = BUY_QUANTİTY
                        ANLIK = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])
                        # -------------------------------------------------
                        if ((ANLIK * 100.1) / 100) * BALANCE >= self.HEDEF:
                            SELL_ORDER_PRİCE += (ANLIK * 100.1) / 100
                        elif ((ANLIK * 100.2) / 100) * BALANCE >= self.HEDEF:
                            SELL_ORDER_PRİCE += (ANLIK * 100.2) / 100
                        # -------------------------------------------------
                        elif ((ANLIK * 100.3) / 100) * BALANCE >= self.HEDEF:
                            SELL_ORDER_PRİCE += (ANLIK * 100.3) / 100
                        elif ((ANLIK * 100.4) / 100) * BALANCE >= self.HEDEF:
                            SELL_ORDER_PRİCE += (ANLIK * 100.4) / 100
                        # -------------------------------------------------
                        elif ((ANLIK * 100.5) / 100) * BALANCE >= self.HEDEF:
                            SELL_ORDER_PRİCE += (ANLIK * 100.5) / 100
                        elif ((ANLIK * 100.6) / 100) * BALANCE >= self.HEDEF:
                            SELL_ORDER_PRİCE += (ANLIK * 100.6) / 100
                        # -------------------------------------------------
                        elif ((ANLIK * 100.7) / 100) * BALANCE >= self.HEDEF:
                            SELL_ORDER_PRİCE += (ANLIK * 100.7) / 100
                        elif ((ANLIK * 100.8) / 100) * BALANCE >= self.HEDEF:
                            SELL_ORDER_PRİCE += (ANLIK * 100.8) / 100
                        # -------------------------------------------------
                        elif ((ANLIK * 100.9) / 100) * BALANCE >= self.HEDEF:
                            SELL_ORDER_PRİCE += (ANLIK * 100.9) / 100
                        elif ((ANLIK * 101.0) / 100) * BALANCE >= self.HEDEF:
                            SELL_ORDER_PRİCE += (ANLIK * 101.0) / 100
                        # -------------------------------------------------
                        print("{} Sell Opportunity Price : {}".format(DEMO,SELL_ORDER_PRİCE))

                        if SELL_ORDER_PRİCE != 0:
                            SELL_OpportunityAlgorithm_PRİCE = 0
                            SELL_OpportunityAlgorithm_BALANCE = 0
                            def OpportunityAlgorithm(Price):
                                nonlocal SELL_OpportunityAlgorithm_PRİCE, SELL_OpportunityAlgorithm_BALANCE
                                while True:
                                    try:
                                        NEW_BALANCE = float(BUY_QUANTİTY)
                                        PRİCE = Price
                                        SELL_OpportunityAlgorithm_PRİCE += PRİCE
                                        SELL_OpportunityAlgorithm_BALANCE += NEW_BALANCE
                                        print("{} Fiyatı : {} | Varlık : {} 'dan Satım Emri Verilmiştir.".format(DEMO, round(PRİCE, 3), round(NEW_BALANCE, 6)))
                                    except:
                                        break
                                    break

                            while True:
                                try:
                                    OpportunityAlgorithm(Price=SELL_ORDER_PRİCE)
                                    break
                                except:
                                    print("{} Tekrardan Bağlantı Sağlanıyor.".format(DEMO))

                            while True:
                                try:
                                    ANLIK = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])

                                    if ANLIK < (SELL_OpportunityAlgorithm_PRİCE * 98) / 100:
                                        self.KAZANILAN_BAKİYE += ANLIK * SELL_OpportunityAlgorithm_BALANCE
                                        print("{} Emirler İptal Edildi.".format(DEMO))
                                        print("{} Stop Emri Verildi.".format(DEMO))
                                        print("{} Yeni Bakiyeniz : {}$".format(DEMO, round(self.KAZANILAN_BAKİYE, 2)))
                                        break

                                    elif ANLIK > SELL_ORDER_PRİCE:
                                        self.KAZANILAN_BAKİYE += ANLIK * SELL_OpportunityAlgorithm_BALANCE
                                        Return_Fee()
                                        print("{} Sell OpportunityAlgorithm Successful !".format(DEMO))
                                        print("{} Yeni Bakiyeniz : {}$".format(DEMO, round(self.KAZANILAN_BAKİYE, 2)))
                                        print("{} Ödemeniz Gereken Komisyon : {}$".format(DEMO, round(self.Fee, 2)))
                                        self.SELL_Opportunity -= 3
                                        break

                                    else:
                                        time.sleep(1)
                                        print("{} {}:{}  | Waiting Sell.".format(DEMO, time.gmtime()[3] + 3, time.gmtime()[4]))
                                except:
                                    print("{} Tekrardan Bağlantı Sağlanılıyor.".format(DEMO))

                        else:
                            self.SELL_Opportunity -= 3
                    except:
                        print("Sell OpportunityAlgorithm Error ".format(DEMO))
                elif self.KAZANILAN_BAKİYE >= 10:
                    AL_MultiChain_ONE = list()
                    TİME_ZONE = list()
                    STOP_BUSD = False
                    BUY_ZARAR_KURTARMA = False
                    CANCEL_SAYAC = 0

                    while True:
                        try:
                            Multi_Chain_BUY_START()
                            break
                        except:
                            print("{} Tekrardan Bağlantı Sağlanıyor.".format(DEMO))

                    ILK_ANLIK_FIYAT_BUSD = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])
                    AL_MultiChain_ONE.append(float(ILK_ANLIK_FIYAT_BUSD))
                    while True:
                        WARNİNG_BUSD = 40
                        TRY_TİME_BUSD = 0
                        IKINCI_ANLIK_FIYAT_BUSD = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])

                        if STOP_BUSD == True:
                            break

                        def NOW_MARKETİNG_STR_DATA():
                            if self.PİYASA_DURUMU == 1:
                                return "Dalgalı Piyasa"
                            elif self.PİYASA_DURUMU == 2:
                                return "Yüksek Dalgalı"
                            elif self.PİYASA_DURUMU == 3:
                                return "Nötr"
                            elif self.PİYASA_DURUMU == 4:
                                return "Yüksek Nötr"
                            elif self.PİYASA_DURUMU == 5:
                                return "Pump"
                            elif self.PİYASA_DURUMU == 6:
                                return "Yüksek Pump"
                            elif self.PİYASA_DURUMU == 7:
                                return "Dump"
                            elif self.PİYASA_DURUMU == 8:
                                return "Yüksek Dump"
                        def Hight_PRİCE():
                            self.MultiChain_OPTİON()
                            SORUMLU_COİN_ONE_AL = self.SORUMLU_COİN_ONE_AL
                            SORUMLU_COİN_ONE_SAT = self.SORUMLU_COİN_ONE_SAT
                            STOP_FUNCTİON_BUY_PRİCE = round(float(SORUMLU_COİN_ONE_AL), 1)
                            STOP_FUNCTİON_SELL_PRİCE = round(float(SORUMLU_COİN_ONE_SAT * 50) / 100, 1)

                            try:
                                print("{} Emirler İptal Edildi".format(DEMO))
                                self.KAZANILAN_BAKİYE = self.KAZANC_BALANCE
                            except:
                                print("{} Tekrardan Bağlantı Sağlanıyor.".format(DEMO))

                            BUY_PRİCE_HİGHT_FUNCTİON = 0
                            BUY_QUANTİTY_HİGHT_FUNCTİON = 0
                            SELL_PRİCE_HİGHT_FUNCTİON = 0
                            SELL_QUANTİTY_HİGHT_FUNCTİON = 0

                            def STOP_FUNCTİON_BUY(Price=STOP_FUNCTİON_BUY_PRİCE):
                                nonlocal BUY_PRİCE_HİGHT_FUNCTİON, BUY_QUANTİTY_HİGHT_FUNCTİON
                                while True:
                                    try:
                                        ANLIK = float(ROB.get_ticker(symbol="BTCBUSD")['lastPrice'])
                                        Quantity = self.KAZANILAN_BAKİYE / float(ANLIK)
                                        PRİCE = float(ANLIK) - Price

                                        BUY_PRİCE_HİGHT_FUNCTİON += PRİCE
                                        BUY_QUANTİTY_HİGHT_FUNCTİON += Quantity
                                        self.KAZANILAN_BAKİYE = 0
                                        print("{} Fiyatı : {} | Varlık : {} 'dan Alım Emri Verilmiştir.".format(DEMO, round(PRİCE, 3), round(Quantity, 6)))
                                    except:
                                        break
                                    break
                            def STOP_FUNCTİON_SELL(Price=STOP_FUNCTİON_SELL_PRİCE):
                                nonlocal SELL_PRİCE_HİGHT_FUNCTİON, SELL_QUANTİTY_HİGHT_FUNCTİON
                                while True:
                                    try:
                                        NEW_BALANCE = BUY_QUANTİTY_HİGHT_FUNCTİON
                                        ANLIK = float(ROB.get_ticker(symbol="BTCBUSD")['lastPrice'])
                                        PRİCE = float(ANLIK) + Price
                                        print("{} Fiyatı : {} | Varlık : {} 'dan Satım Emri Verilmiştir.".format(DEMO, round(PRİCE, 3), round(NEW_BALANCE, 6)))

                                        SELL_PRİCE_HİGHT_FUNCTİON += PRİCE
                                        SELL_QUANTİTY_HİGHT_FUNCTİON += NEW_BALANCE
                                    except:
                                        break
                                    break
                            def SECURTY_SELL():
                                def Securty_MARKET():
                                    while True:
                                        try:
                                            BALANCE = SELL_QUANTİTY_HİGHT_FUNCTİON
                                            ANLIK = float(ROB.get_ticker(symbol="BTCBUSD")['lastPrice'])
                                            PRİCE = ANLIK
                                            self.KAZANILAN_BAKİYE += ANLIK * BALANCE
                                            print("{} Fiyatı : {} | Varlık : {} 'dan Satış Gerçekleşmiştir.".format(DEMO, PRİCE, BALANCE))

                                        except:
                                            break
                                        break

                                try:
                                    print("{} Emirler İptal Edildi.".format(DEMO))
                                except:
                                    print("{} Tekrardan Bağlantı Sağlanıyor.".format(DEMO))

                                while True:
                                    try:
                                        Securty_MARKET()
                                        print("{} Yeni Bakiyeniz : {}".format(DEMO,self.KAZANILAN_BAKİYE))
                                        break
                                    except:
                                        print("{} Tekrardan Bağlantı Sağlanıyor.".format(DEMO))

                            while True:
                                try:
                                    STOP_FUNCTİON_BUY()
                                    break
                                except:
                                    print("{} Tekrardan Bağlantı Sağlanıyor.".format(DEMO))


                            while True:
                                try:


                                    if float(ROB.get_ticker(symbol="BTCBUSD")['lastPrice']) < BUY_PRİCE_HİGHT_FUNCTİON:
                                        print("{} Satın Alım Başarılı ! ".format(DEMO))
                                        STOP_FUNCTİON_SELL()
                                        print("{} Satış Emri Başarıyla Verildi.".format(DEMO))
                                        break


                                    else:
                                        time.sleep(1)
                                        print("{} {}:{}  | Waiting Buy.".format(DEMO,time.gmtime()[3]+3,time.gmtime()[4]))


                                except:
                                    print("{} Tekrardan Bağlantı Sağlanıyor.".format(DEMO))


                            while True:
                                try:


                                    if float(SELL_PRİCE_HİGHT_FUNCTİON * 98.5) / 100 > float(ROB.get_ticker(symbol="BTCBUSD")['lastPrice']):
                                        while True:
                                            try:
                                                SECURTY_SELL()
                                                Return_Fee()
                                                break
                                            except:
                                                print("{} Tekrardan Bağlantı Sağlanıyor.".format(DEMO))


                                    elif float(SELL_PRİCE_HİGHT_FUNCTİON + STOP_FUNCTİON_SELL_PRİCE) < float(ROB.get_ticker(symbol=SORUMLU_COİN_ONE)['lastPrice']):
                                        print("{} Satış Başarılı !".format(DEMO))
                                        self.KAZANILAN_BAKİYE += float(ROB.get_ticker(symbol=SORUMLU_COİN_ONE)['lastPrice']) * SELL_QUANTİTY_HİGHT_FUNCTİON
                                        Return_Fee()
                                        break


                                    else:
                                        time.sleep(2)
                                        print("{} {}:{}  | Waiting Sell".format(DEMO,time.gmtime()[3]+3,time.gmtime()[4]))


                                except:
                                    print("{} Tekrardan Bağlantı Sağlanıyor.".format(DEMO))
                        def Dump_BUSD_EX():
                            STOP_TRY_TİME_EX = False
                            TRY_TİME_BUSD_EX = 0
                            STOP_MultiChain_ONE = list()

                            def DUMP_EX():
                                while True:
                                    try:
                                        EXCEPT_CRYPTO_BALANCE = float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE))
                                        EXCEPT_CRYPTO_NEW_BALANCE = float(EXCEPT_CRYPTO_BALANCE)
                                        Intelence.ROB_SELL_MARKET(symbol=self.SORUMLU_COİN_ONE, quantity=EXCEPT_CRYPTO_NEW_BALANCE)
                                    except:
                                        break
                                    break

                            while True:
                                try:
                                    if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)) < 0.001:
                                        break
                                    else:
                                        time.sleep(1)
                                        print("Dump Ex Loop")
                                except:
                                    print("Tekrardan Bağlantı Sağlanıyor.")

                            EXCEPT_ANLIK = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])
                            STOP_MultiChain_ONE.clear()
                            STOP_MultiChain_ONE.append(float(EXCEPT_ANLIK))

                            while TRY_TİME_BUSD_EX < 14400:
                                time.sleep(1)
                                DUMP_BUSD_EX = 15
                                DUMP_DEGİSMEYEN_FİYAT_BUSD = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])
                                TRY_TİME_BUSD_EX += 1
                                print("DUMP CONTROL I !")

                                if STOP_TRY_TİME_EX == True:
                                    break

                                while DUMP_BUSD_EX > 0:
                                    print("DUMP CONTROL II !")
                                    time.sleep(1)
                                    DUMP_BUSD_EX -= 1
                                    DUMP_DEGİSEN_FİYAT_BUSD = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])

                                    if (float(DUMP_DEGİSMEYEN_FİYAT_BUSD) + ((float(DUMP_DEGİSMEYEN_FİYAT_BUSD * 0.40) / 100)) <= float(DUMP_DEGİSEN_FİYAT_BUSD)):
                                        print("EXCEPT BLOCK DUMP OPTİON I TRUE")

                                        class DUMP_ONE_BUSD():
                                            def DUMP_OPTİON_START():
                                                while True:
                                                    try:
                                                        BUSD = Intelence.ROB_ACCOUNT_GET_BALANCE(symbol='BUSD')
                                                        ANLIK = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])
                                                        Quantity = math.floor(float(BUSD)) / float(ANLIK)
                                                        STEP = get_round_step_quantity(qty=Quantity)
                                                        Intelence.ROB_BUY_MARKET(symbol=self.SORUMLU_COİN_ONE, quantity=float(STEP))
                                                    except:
                                                        break
                                                    break

                                            def DUMP_OPTİON_ONE():
                                                while True:
                                                    try:
                                                        BALANCE = Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)
                                                        NEW_BALANCE = float(BALANCE)
                                                        ANLIK = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])
                                                        PRİCE = float(ANLIK) + ((float(ANLIK) * 0.5) / 100)
                                                        Intelence.ROB_SELL_LİMİT(symbol=self.SORUMLU_COİN_ONE, quantity=float(NEW_BALANCE), price=str(PRİCE))
                                                    except:
                                                        break
                                                    break

                                        while True:
                                            try:
                                                if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol='BUSD')) <= 10:
                                                    break
                                                else:
                                                    time.sleep(1)
                                                    DUMP_ONE_BUSD.DUMP_OPTİON_START()
                                                    print("Try Again DUMP Buy Order...")
                                            except:
                                                print("Tekrardan Bağlantı Sağlanıyor.")

                                        while True:
                                            try:
                                                if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)) <= 0.001:
                                                    TRY_TİME_BUSD_EX += 14400
                                                    DUMP_BUSD_EX -= 15
                                                    STOP_TRY_TİME_EX += True
                                                    break
                                                else:
                                                    time.sleep(1)
                                                    DUMP_ONE_BUSD.DUMP_OPTİON_ONE()
                                                    print("Try Again DUMP Sell Order...")
                                            except:
                                                print("Tekrardan Bağlantı Sağlanıyor.")
                                        break

                                    elif float(DUMP_DEGİSEN_FİYAT_BUSD) > ((STOP_MultiChain_ONE[0] * 101.5) / 100):
                                        print("EXCEPT BLOCK DUMP OPTİON II TRUE")
                                        TİME_ZONE.append(float(DUMP_DEGİSEN_FİYAT_BUSD))
                                        TİME_ZONE_SECOND_DUMP = 14400

                                        DUMP_OPTİON_START_ORDER_ID = ""

                                        class DUMP_ONE_BUSD():
                                            def DUMP_OPTİON_START():
                                                while True:
                                                    try:
                                                        BUSD = Intelence.ROB_ACCOUNT_GET_BALANCE(symbol='BUSD')
                                                        ANLIK = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])
                                                        Quantity = math.floor(float(BUSD)) / float(ANLIK)
                                                        STEP = get_round_step_quantity(qty=Quantity)
                                                        PRİCE = float(ANLIK) - (float(ANLIK * 0.6) / 100)
                                                        Intelence.ROB_BUY_LİMİT(symbol=self.SORUMLU_COİN_ONE, quantity=float(STEP), price=str(PRİCE))
                                                    except:
                                                        break
                                                    break

                                            def DUMP_OPTİON_ONE():
                                                while True:
                                                    try:
                                                        BALANCE = Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)
                                                        NEW_BALANCE = float(BALANCE)
                                                        ANLIK = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])
                                                        PRİCE = float(ANLIK) + ((float(ANLIK) * 0.7) / 100)
                                                        Intelence.ROB_SELL_LİMİT(symbol=self.SORUMLU_COİN_ONE, quantity=float(NEW_BALANCE), price=str(PRİCE))
                                                    except:
                                                        break
                                                    break

                                            def DUMP_OPTİON_TWO():
                                                while True:
                                                    try:
                                                        Intelence.ROB_CANCEL(symbol=self.SORUMLU_COİN_ONE, orderID=str(DUMP_OPTİON_START_ORDER_ID))
                                                        time.sleep(2)
                                                        BUSD = Intelence.ROB_ACCOUNT_GET_BALANCE(symbol='BUSD')
                                                        ANLIK = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])
                                                        Quantity = math.floor(float(BUSD)) / float(ANLIK)
                                                        STEP = get_round_step_quantity(qty=Quantity)
                                                        PRİCE = float(ANLIK) - (float(ANLIK * 0.8) / 100)
                                                        Intelence.ROB_BUY_LİMİT(symbol=self.SORUMLU_COİN_ONE, quantity=float(STEP), price=str(PRİCE))
                                                    except:
                                                        break
                                                    break

                                        while True:
                                            try:
                                                if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol='BUSD')) <= 10:
                                                    break
                                                else:
                                                    time.sleep(1)
                                                    DUMP_ONE_BUSD.DUMP_OPTİON_START()
                                                    print("Try Again DUMP Buy Order...")
                                            except:
                                                print("Tekrardan Bağlantı Sağlanıyor.")

                                        orders = ROB.get_open_orders(symbol=self.SORUMLU_COİN_ONE)
                                        orders_ID = orders[0]['orderId']
                                        DUMP_OPTİON_START_ORDER_ID += str(orders_ID)
                                        while TİME_ZONE_SECOND_DUMP >= 0:
                                            time.sleep(2)
                                            TİME_ZONE_DEGİSEN_FIYAT_DUMP_TWO = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])
                                            TİME_ZONE_SECOND_DUMP -= 1

                                            if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)) > 0.001:
                                                while True:
                                                    try:
                                                        if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)) <= 0.001:
                                                            TİME_ZONE_SECOND_DUMP -= 14400
                                                            DUMP_BUSD_EX -= 15
                                                            STOP_TRY_TİME_EX += True
                                                            break
                                                        else:
                                                            time.sleep(1)
                                                            DUMP_ONE_BUSD.DUMP_OPTİON_ONE()
                                                            print("Try Again DUMP Sell Order...")
                                                    except:
                                                        print("Tekrardan Bağlantı Sağlanıyor.")
                                                break

                                            elif float(TİME_ZONE_DEGİSEN_FIYAT_DUMP_TWO) >= float(TİME_ZONE[0] * 101.5) / 100:
                                                while True:
                                                    try:
                                                        if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol='BUSD')) <= 10:
                                                            TİME_ZONE_SECOND_DUMP -= 14400
                                                            DUMP_BUSD_EX -= 15
                                                            STOP_TRY_TİME_EX += True
                                                            break
                                                        else:
                                                            time.sleep(1)
                                                            DUMP_ONE_BUSD.DUMP_OPTİON_TWO()
                                                            print("Try Again DUMP Buy Order...")
                                                    except:
                                                        print("Tekrardan Bağlantı Sağlanıyor.")
                                                break

                                            elif TİME_ZONE_SECOND_DUMP == 1:
                                                TİME_ZONE_SECOND_DUMP -= 14400
                                                DUMP_BUSD_EX -= 15
                                                STOP_TRY_TİME_EX += True
                                                break

                                    elif float(DUMP_DEGİSEN_FİYAT_BUSD) <= ((STOP_MultiChain_ONE[0] * 99) / 100):
                                        print("EXCEPT BLOCK DUMP OPTİON III TRUE")

                                        class DUMP_ONE_BUSD():
                                            def DUMP_OPTİON_START():
                                                while True:
                                                    try:
                                                        BUSD = Intelence.ROB_ACCOUNT_GET_BALANCE(symbol='BUSD')
                                                        ANLIK = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])
                                                        Quantity = math.floor(float(BUSD)) / float(ANLIK)
                                                        STEP = get_round_step_quantity(qty=Quantity)
                                                        Intelence.ROB_BUY_MARKET(symbol=self.SORUMLU_COİN_ONE, quantity=float(STEP))
                                                    except:
                                                        break
                                                    break

                                            def DUMP_OPTİON_ONE():
                                                while True:
                                                    try:
                                                        BALANCE = Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)
                                                        NEW_BALANCE = float(BALANCE)
                                                        ANLIK = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])
                                                        PRİCE = float(ANLIK) + ((float(ANLIK) * 0.5) / 100)
                                                        Intelence.ROB_SELL_LİMİT(symbol=self.SORUMLU_COİN_ONE, quantity=float(NEW_BALANCE), price=str(PRİCE))
                                                    except:
                                                        break
                                                    break

                                        while True:
                                            try:
                                                if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol='BUSD')) <= 10:
                                                    break
                                                else:
                                                    time.sleep(1)
                                                    DUMP_ONE_BUSD.DUMP_OPTİON_START()
                                                    print("Try Again DUMP Buy Order...")
                                            except:
                                                print("Tekrardan Bağlantı Sağlanıyor.")

                                        while True:
                                            try:
                                                if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)) <= 0.001:
                                                    TİME_ZONE_SECOND_DUMP -= 14400
                                                    DUMP_BUSD_EX -= 15
                                                    STOP_TRY_TİME_EX += True
                                                    break
                                                else:
                                                    time.sleep(1)
                                                    DUMP_ONE_BUSD.DUMP_OPTİON_ONE()
                                                    print("Try Again DUMP Sell Order...")
                                                    break
                                            except:
                                                print("Tekrardan Bağlantı Sağlanıyor.")
                        def Dump_BUSD():
                            try:
                                STOP_TRY_TİME = False
                                TRY_TİME_BUSD = 0
                                STOP_MultiChain_ONE = list()

                                print("DUMP DETECTED I !")
                                TRY_ANLIK = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])
                                STOP_MultiChain_ONE.append(float(TRY_ANLIK))
                                Intelence.ROB_CANCEL(symbol=self.SORUMLU_COİN_ONE, orderID=str(START_BUY_ORDER_ID))

                                while TRY_TİME_BUSD < 14400:
                                    time.sleep(1)
                                    DUMP_BUSD = 15
                                    TRY_TİME_BUSD += 1
                                    DUMP_DEGİSMEYEN_FİYAT_BUSD = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])
                                    print("DUMP CONTROL I !")

                                    if STOP_TRY_TİME == True:
                                        break

                                    while DUMP_BUSD > 0:
                                        print("DUMP CONTROL II !")
                                        time.sleep(1)
                                        DUMP_BUSD -= 1
                                        DUMP_DEGİSEN_FİYAT_BUSD = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])

                                        if float(DUMP_DEGİSMEYEN_FİYAT_BUSD) + ((float(DUMP_DEGİSMEYEN_FİYAT_BUSD * 0.35) / 100)) <= float(DUMP_DEGİSEN_FİYAT_BUSD):
                                            print("DUMP OPTİON I TRUE")

                                            class DUMP_ONE_BUSD():
                                                def DUMP_OPTİON_START():
                                                    while True:
                                                        try:
                                                            BUSD = Intelence.ROB_ACCOUNT_GET_BALANCE(symbol='BUSD')
                                                            ANLIK = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])
                                                            Quantity = math.floor(float(BUSD)) / float(ANLIK)
                                                            STEP = get_round_step_quantity(qty=Quantity)
                                                            DUMP_OPTİON_EMİR = Intelence.ROB_BUY_MARKET(symbol=self.SORUMLU_COİN_ONE, quantity=float(STEP))
                                                        except:
                                                            break
                                                        break

                                                def DUMP_OPTİON_ONE():
                                                    while True:
                                                        try:
                                                            BALANCE = Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)
                                                            NEW_BALANCE = float(BALANCE)
                                                            ANLIK = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])
                                                            PRİCE = float(ANLIK) + ((float(ANLIK) * 0.3) / 100)
                                                            Intelence.ROB_SELL_LİMİT(symbol=self.SORUMLU_COİN_ONE, quantity=float(NEW_BALANCE), price=str(PRİCE))
                                                        except:
                                                            break
                                                        break

                                            while True:
                                                try:
                                                    if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol='BUSD')) <= 10:
                                                        break
                                                    else:
                                                        time.sleep(1)
                                                        DUMP_ONE_BUSD.DUMP_OPTİON_START()
                                                        print("Try Again DUMP Buy Order...")
                                                except:
                                                    print("Tekrardan Bağlantı Sağlanıyor.")

                                            while True:
                                                try:
                                                    if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)) <= 0.001:
                                                        DUMP_BUSD -= 15
                                                        STOP_TRY_TİME += True
                                                        break
                                                    else:
                                                        time.sleep(1)
                                                        DUMP_ONE_BUSD.DUMP_OPTİON_ONE()
                                                        print("Try Again DUMP Sell Order...")
                                                except:
                                                    print("Tekrardan Bağlantı Sağlanıyor.")
                                            break

                                        elif float(DUMP_DEGİSEN_FİYAT_BUSD) > float((STOP_MultiChain_ONE[0] * 101) / 100):
                                            print("DUMP OPTİON II TRUE")
                                            TİME_ZONE.append(float(DUMP_DEGİSEN_FİYAT_BUSD))
                                            TİME_ZONE_SECOND_DUMP = 14400
                                            DUMP_OPTİON_START_ORDER_ID = ""

                                            class DUMP_ONE_BUSD():
                                                def DUMP_OPTİON_START():
                                                    while True:
                                                        try:
                                                            BUSD = Intelence.ROB_ACCOUNT_GET_BALANCE(symbol='BUSD')
                                                            ANLIK = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])
                                                            Quantity = math.floor(float(BUSD)) / float(ANLIK)
                                                            STEP = get_round_step_quantity(qty=Quantity)
                                                            PRİCE = float(ANLIK) - (float(ANLIK * 0.40) / 100)
                                                            DUMP_OPTİON_EMİR = Intelence.ROB_BUY_LİMİT(symbol=self.SORUMLU_COİN_ONE, quantity=float(STEP), price=str(PRİCE))
                                                        except:
                                                            break
                                                        break

                                                def DUMP_OPTİON_ONE():
                                                    while True:
                                                        try:
                                                            BALANCE = Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)
                                                            NEW_BALANCE = float(BALANCE)
                                                            ANLIK = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])
                                                            PRİCE = float(ANLIK) + ((float(ANLIK) * 0.50) / 100)
                                                            Intelence.ROB_SELL_LİMİT(symbol=self.SORUMLU_COİN_ONE, quantity=float(NEW_BALANCE), price=str(PRİCE))
                                                        except:
                                                            break
                                                        break

                                                def DUMP_OPTİON_TWO():
                                                    while True:
                                                        try:
                                                            CANCEL = Intelence.ROB_CANCEL(symbol=self.SORUMLU_COİN_ONE, orderID=str(DUMP_OPTİON_START_ORDER_ID))
                                                            time.sleep(2)
                                                            BUSD = Intelence.ROB_ACCOUNT_GET_BALANCE(symbol='BUSD')
                                                            ANLIK = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])
                                                            Quantity = math.floor(float(BUSD)) / float(ANLIK)
                                                            STEP = get_round_step_quantity(qty=Quantity)
                                                            PRİCE = float(ANLIK) - (float(ANLIK * 0.60) / 100)
                                                            Intelence.ROB_BUY_LİMİT(symbol=self.SORUMLU_COİN_ONE, quantity=float(STEP), price=str(PRİCE))
                                                        except:
                                                            break
                                                        break

                                            while True:
                                                try:
                                                    if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol='BUSD')) <= 10:
                                                        break
                                                    else:
                                                        time.sleep(1)
                                                        DUMP_ONE_BUSD.DUMP_OPTİON_START()
                                                        print("Try Again DUMP Buy Order...")
                                                except:
                                                    print("Tekrardan Bağlantı Sağlanıyor.")

                                            orders = ROB.get_open_orders(symbol=self.SORUMLU_COİN_ONE)
                                            orders_ID = orders[0]['orderId']
                                            DUMP_OPTİON_START_ORDER_ID += str(orders_ID)
                                            while TİME_ZONE_SECOND_DUMP >= 0:
                                                time.sleep(2)
                                                TİME_ZONE_DEGİSEN_FIYAT_DUMP = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])
                                                TİME_ZONE_SECOND_DUMP -= 1

                                                if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)) > 0.001:
                                                    while True:
                                                        try:
                                                            if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)) <= 0.001:
                                                                TİME_ZONE_SECOND_DUMP_TWO -= 14400
                                                                DUMP_BUSD -= 15
                                                                STOP_TRY_TİME += True
                                                                break
                                                            else:
                                                                time.sleep(1)
                                                                DUMP_ONE_BUSD.DUMP_OPTİON_ONE()
                                                                print("Try Again DUMP Sell Order...")
                                                        except:
                                                            print("Tekrardan Bağlantı Sağlanıyor.")
                                                    break

                                                elif float(TİME_ZONE_DEGİSEN_FIYAT_DUMP) >= float(TİME_ZONE[0] * 101) / 100:
                                                    while True:
                                                        try:
                                                            if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol='BUSD')) <= 10:
                                                                TİME_ZONE_SECOND_DUMP_TWO -= 14400
                                                                DUMP_BUSD -= 15
                                                                STOP_TRY_TİME += True
                                                                break
                                                            else:
                                                                time.sleep(1)
                                                                DUMP_ONE_BUSD.DUMP_OPTİON_TWO()
                                                                print("Try Again DUMP Buy Order...")
                                                        except:
                                                            print("Tekrardan Bağlantı Sağlanıyor.")
                                                    break

                                                elif TİME_ZONE_SECOND_DUMP == 1:
                                                    TİME_ZONE_SECOND_DUMP_TWO -= 14400
                                                    DUMP_BUSD -= 15
                                                    STOP_TRY_TİME += True
                                                    break

                                        elif float(DUMP_DEGİSEN_FİYAT_BUSD) <= float((STOP_MultiChain_ONE[0] * 99.5) / 100):
                                            print("DUMP OPTİON III TRUE")

                                            class DUMP_ONE_BUSD():
                                                def DUMP_OPTİON_START():
                                                    while True:
                                                        try:
                                                            BUSD = Intelence.ROB_ACCOUNT_GET_BALANCE(symbol='BUSD')
                                                            ANLIK = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])
                                                            Quantity = math.floor(float(BUSD)) / float(ANLIK)
                                                            STEP = get_round_step_quantity(qty=Quantity)
                                                            DUMP_OPTİON_EMİR = Intelence.ROB_BUY_MARKET(symbol=self.SORUMLU_COİN_ONE, quantity=float(STEP))
                                                        except:
                                                            break
                                                        break

                                                def DUMP_OPTİON_ONE():
                                                    while True:
                                                        try:
                                                            BALANCE = Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)
                                                            NEW_BALANCE = float(BALANCE)
                                                            ANLIK = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])
                                                            PRİCE = float(ANLIK) + ((float(ANLIK) * 0.3) / 100)
                                                            Intelence.ROB_SELL_LİMİT(symbol=self.SORUMLU_COİN_ONE, quantity=float(NEW_BALANCE), price=str(PRİCE))
                                                        except:
                                                            break
                                                        break

                                            while True:
                                                try:
                                                    if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol='BUSD')) <= 10:
                                                        break
                                                    else:
                                                        time.sleep(1)
                                                        DUMP_ONE_BUSD.DUMP_OPTİON_START()
                                                        print("Try Again DUMP Buy Order...")
                                                except:
                                                    print("Tekrardan Bağlantı Sağlanıyor.")

                                            while True:
                                                try:
                                                    if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)) <= 0.001:
                                                        DUMP_BUSD -= 15
                                                        STOP_TRY_TİME += True
                                                        break
                                                    else:
                                                        time.sleep(1)
                                                        DUMP_ONE_BUSD.DUMP_OPTİON_ONE()
                                                        print("Try Again DUMP Sell Order...")
                                                except:
                                                    print("Tekrardan Bağlantı Sağlanıyor.")
                                            break
                            except:
                                Dump_BUSD_EX()
                        def Pump_BUSD():
                            print("PUMP DETECTED I !")
                            STOP_TRY_TİME = False
                            TRY_TİME_BUSD = 0
                            STOP_MultiChain_ONE = list()
                            Intelence.ROB_CANCEL(symbol=self.SORUMLU_COİN_ONE, orderID=str(START_BUY_ORDER_ID))
                            time.sleep(2)

                            def PUMP_START():
                                while True:
                                    try:
                                        BUSD = Intelence.ROB_ACCOUNT_GET_BALANCE(symbol='BUSD')
                                        ANLIK = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])
                                        QUANTİTY = math.floor(float(BUSD)) / float(ANLIK)
                                        STEP = get_round_step_quantity(qty=QUANTİTY)
                                        Intelence.ROB_BUY_MARKET(symbol=self.SORUMLU_COİN_ONE, quantity=float(STEP))
                                    except:
                                        break
                                    break

                            while True:
                                try:
                                    if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol='BUSD')) <= 10:
                                        break
                                    else:
                                        time.sleep(1)
                                        PUMP_START()
                                        print("Try Again PUMP Buy Order...")
                                except:
                                    print("Tekrardan Bağlantı Sağlanıyor.")

                            TRY_ANLIK = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])
                            STOP_MultiChain_ONE.append(float(TRY_ANLIK))
                            while TRY_TİME_BUSD < 14400:
                                time.sleep(1)
                                TRY_TİME_BUSD += 1
                                PUMP_BUSD = 15
                                PUMP_DEGİSMEYEN_FIYAT_BUSD = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])
                                print("PUMP CONTROL I !")

                                if STOP_TRY_TİME == True:
                                    break

                                while PUMP_BUSD > 0:
                                    print("PUMP CONTROL II !")
                                    time.sleep(1)
                                    PUMP_BUSD -= 1
                                    PUMP_DEGİSEN_FIYAT_BUSD = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])

                                    if (float(PUMP_DEGİSMEYEN_FIYAT_BUSD) - ((float(PUMP_DEGİSMEYEN_FIYAT_BUSD * 0.35) / 100)) >= float(PUMP_DEGİSEN_FIYAT_BUSD)):
                                        print("PUMP OPTİON I TRUE")

                                        class PUMP_ONE_BUSD():
                                            def PUMP_OPTİON_START():
                                                while True:
                                                    try:
                                                        BALANCE = Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)
                                                        NEW_BALANCE = float(BALANCE)
                                                        EMİR = Intelence.ROB_SELL_MARKET(symbol=self.SORUMLU_COİN_ONE, quantity=float(NEW_BALANCE))
                                                    except:
                                                        break
                                                    break

                                            def PUMP_OPTİON_ONE():
                                                while True:
                                                    try:
                                                        BUSD = Intelence.ROB_ACCOUNT_GET_BALANCE(symbol='BUSD')
                                                        ANLIK = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])
                                                        QUANTİTY = math.floor(float(BUSD)) / float(ANLIK)
                                                        STEP = get_round_step_quantity(qty=QUANTİTY)
                                                        PRİCE = float(ANLIK) - ((float(ANLIK * 0.3) / 100))
                                                        EMİR = Intelence.ROB_BUY_LİMİT(symbol=self.SORUMLU_COİN_ONE, quantity=float(STEP), price=str(PRİCE))
                                                    except:
                                                        break
                                                    break

                                        while True:
                                            try:
                                                if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)) <= 0.001:
                                                    break
                                                else:
                                                    time.sleep(1)
                                                    print("Try Again PUMP Sell Order...")
                                                    PUMP_ONE_BUSD.PUMP_OPTİON_START()
                                            except:
                                                print("Tekrardan Bağlantı Sağlanıyor.")
                                        while True:
                                            try:
                                                if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol='BUSD')) <= 10:
                                                    PUMP_BUSD -= 15
                                                    STOP_TRY_TİME += True
                                                    break
                                                else:
                                                    time.sleep(1)
                                                    PUMP_ONE_BUSD.PUMP_OPTİON_ONE()
                                                    print("Try Again PUMP Buy Order...")
                                            except:
                                                print("Tekrardan Bağlantı Sağlanıyor.")
                                        break

                                    elif float(PUMP_DEGİSEN_FIYAT_BUSD) >= (STOP_MultiChain_ONE[0] * 100.5) / 100:
                                        print("PUMP OPTİON II TRUE")

                                        class PUMP_ONE_BUSD():
                                            def PUMP_OPTİON_START():
                                                while True:
                                                    try:
                                                        BALANCE = Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)
                                                        NEW_BALANCE = float(BALANCE)
                                                        EMİR = Intelence.ROB_SELL_MARKET(symbol=self.SORUMLU_COİN_ONE, quantity=float(NEW_BALANCE))
                                                    except:
                                                        break
                                                    break

                                            def PUMP_OPTİON_ONE():
                                                while True:
                                                    try:
                                                        BUSD = Intelence.ROB_ACCOUNT_GET_BALANCE(symbol='BUSD')
                                                        ANLIK = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])
                                                        QUANTİTY = math.floor(float(BUSD)) / float(ANLIK)
                                                        STEP = get_round_step_quantity(qty=QUANTİTY)
                                                        PRİCE = float(ANLIK) - ((float(ANLIK * 0.3) / 100))
                                                        EMİR = Intelence.ROB_BUY_LİMİT(symbol=self.SORUMLU_COİN_ONE, quantity=float(STEP), price=str(PRİCE))
                                                    except:
                                                        break
                                                    break

                                        while True:
                                            try:
                                                if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)) <= 0.001:
                                                    break
                                                else:
                                                    time.sleep(1)
                                                    print("Try Again PUMP Sell Order...")
                                                    PUMP_ONE_BUSD.PUMP_OPTİON_START()
                                            except:
                                                print("Tekrardan Bağlantı Sağlanıyor.")

                                        while True:
                                            try:
                                                if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol='BUSD')) <= 10:
                                                    PUMP_BUSD -= 15
                                                    STOP_TRY_TİME += True
                                                    break
                                                else:
                                                    time.sleep(1)
                                                    PUMP_ONE_BUSD.PUMP_OPTİON_ONE()
                                                    print("Try Again PUMP Buy Order...")
                                            except:
                                                print("Tekrardan Bağlantı Sağlanıyor.")
                                        break

                                    elif (STOP_MultiChain_ONE[0] * 99) / 100 >= float(PUMP_DEGİSEN_FIYAT_BUSD):
                                        print("PUMP OPTİON III TRUE")
                                        TİME_ZONE.append(float(PUMP_DEGİSEN_FIYAT_BUSD))
                                        TİME_ZONE_SECOND_PUMP = 14400

                                        PUMP_OPTİON_START_ORDER_ID = ""

                                        class PUMP_ONE_BUSD():
                                            def PUMP_OPTİON_START():
                                                while True:
                                                    try:
                                                        BALANCE = Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)
                                                        NEW_BALANCE = float(BALANCE)
                                                        ANLIK = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])
                                                        PRİCE = float(ANLIK) + ((float(ANLIK) * 0.40) / 100)
                                                        EMİR = Intelence.ROB_SELL_LİMİT(symbol=self.SORUMLU_COİN_ONE, quantity=float(NEW_BALANCE), price=str(PRİCE))
                                                    except:
                                                        break
                                                    break

                                            def PUMP_OPTİON_ONE():
                                                while True:
                                                    try:
                                                        BUSD = Intelence.ROB_ACCOUNT_GET_BALANCE(symbol='BUSD')
                                                        ANLIK = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])
                                                        QUANTİTY = math.floor(float(BUSD)) / float(ANLIK)
                                                        STEP = get_round_step_quantity(qty=QUANTİTY)
                                                        PRİCE = float(ANLIK) - ((float(ANLIK * 0.5) / 100))
                                                        EMİR = Intelence.ROB_BUY_LİMİT(symbol=self.SORUMLU_COİN_ONE, quantity=float(STEP), price=str(PRİCE))
                                                    except:
                                                        break
                                                    break

                                            def PUMP_OPTİON_TWO():
                                                while True:
                                                    try:
                                                        Intelence.ROB_CANCEL(symbol=self.SORUMLU_COİN_ONE, orderID=str(PUMP_OPTİON_START_ORDER_ID))
                                                        time.sleep(2)
                                                        BALANCE = Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)
                                                        NEW_BALANCE = float(BALANCE)
                                                        ANLIK = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])
                                                        PRİCE = (float(ANLIK) + ((float(ANLIK) * 0.6) / 100))
                                                        Intelence.ROB_SELL_LİMİT(symbol=self.SORUMLU_COİN_ONE, quantity=float(NEW_BALANCE), price=str(PRİCE))
                                                    except:
                                                        break
                                                    break

                                        while True:
                                            try:
                                                if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)) <= 0.001:
                                                    break
                                                else:
                                                    time.sleep(1)
                                                    print("Try Again PUMP Sell Order...")
                                                    PUMP_ONE_BUSD.PUMP_OPTİON_START()
                                            except:
                                                print("Tekrardan Bağlantı Sağlanıyor.")

                                        orders = ROB.get_open_orders(symbol=self.SORUMLU_COİN_ONE)
                                        orders_ID = orders[0]['orderId']
                                        PUMP_OPTİON_START_ORDER_ID += str(orders_ID)
                                        while TİME_ZONE_SECOND_PUMP > 0:
                                            time.sleep(2)
                                            TİME_ZONE_DEGİSEN_FIYAT_PUMP = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])
                                            TİME_ZONE_SECOND_PUMP -= 1

                                            if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol='BUSD')) > 10:
                                                while True:
                                                    try:
                                                        if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol='BUSD')) <= 10:
                                                            TİME_ZONE_SECOND_PUMP_SİX -= 14400
                                                            PUMP_BUSD -= 15
                                                            STOP_TRY_TİME += True
                                                            break
                                                        else:
                                                            time.sleep(1)
                                                            PUMP_ONE_BUSD.PUMP_OPTİON_ONE()
                                                            print("Try Again PUMP Buy Order...")
                                                    except:
                                                        print("Tekrardan Bağlantı Sağlanıyor.")
                                                break

                                            elif float(TİME_ZONE_DEGİSEN_FIYAT_PUMP) <= float(TİME_ZONE[0] * 99) / 100:
                                                while True:
                                                    try:
                                                        if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)) <= 0.001:
                                                            TİME_ZONE_SECOND_PUMP_SİX -= 14400
                                                            PUMP_BUSD -= 15
                                                            STOP_TRY_TİME += True
                                                            break
                                                        else:
                                                            time.sleep(1)
                                                            PUMP_ONE_BUSD.PUMP_OPTİON_TWO()
                                                            print("Try Again PUMP Sell Order...")
                                                    except:
                                                        print("Tekrardan Bağlantı Sağlanıyor.")
                                                break

                                            elif TİME_ZONE_SECOND_PUMP == 1:
                                                TİME_ZONE_SECOND_PUMP_SİX -= 14400
                                                PUMP_BUSD -= 15
                                                STOP_TRY_TİME += True
                                                break

                        while WARNİNG_BUSD > 0:
                            try:
                                time.sleep(1)
                                WARNİNG_BUSD -= 1
                                CANCEL_SAYAC += 1
                                UCUNCU_ANLIK_FIYAT_BUSD = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])
                                print("{} Multi C-ROB (I) Waiting !".format(DEMO))
                                print("--------------------------------------")
                                print("{} Multi C-ROB (I) Coin: ".format(DEMO), self.SORUMLU_COİN_ONE)
                                print("{} Multi C-ROB (I) Buy: ".format(DEMO), round(float(self.SORUMLU_COİN_ONE_AL), 1),end="$\n")
                                print("{} Multi C-ROB (I) Sell: ".format(DEMO), round(float(self.SORUMLU_COİN_ONE_SAT), 1),end="$\n")
                                print("{} Multi C-ROB (I) Genel Piyasa: ".format(DEMO), Proposal.Market_STR)
                                print("{} Multi C-ROB (I) Anlık Piyasa: ".format(DEMO), NOW_MARKETİNG_STR_DATA())
                                print("{} Toplam İşlem Ücretiniz : ".format(DEMO), round(self.Fee, 4), end="$\n")
                                print("--------------------------------------")
                                print("{} Geçen Süre : ".format(DEMO), CANCEL_SAYAC, end="\n\n\n\n")

                                if (self.NOTR_STOP == False) and float(IKINCI_ANLIK_FIYAT_BUSD) - float(UCUNCU_ANLIK_FIYAT_BUSD) >= float(self.SORUMLU_COİN_ONE_AL) - (float(self.SORUMLU_COİN_ONE_AL * 7.5) / 100):
                                    Dump_BUSD()
                                    WARNİNG_BUSD = 0
                                    STOP_BUSD += True
                                    LOOP_RETURN += True
                                    print("Dump Function Activate !")
                                    break
                                elif (self.NOTR_STOP == False) and float(UCUNCU_ANLIK_FIYAT_BUSD) - float(IKINCI_ANLIK_FIYAT_BUSD) >= (float(IKINCI_ANLIK_FIYAT_BUSD) * 0.8) / 100:
                                    Pump_BUSD()
                                    WARNİNG_BUSD = 0
                                    STOP_BUSD += True
                                    LOOP_RETURN += True
                                    print("Pump Function Activate !")
                                    break
                                elif float(UCUNCU_ANLIK_FIYAT_BUSD) < float(AL_MultiChain_ONE[0]) - float(self.SORUMLU_COİN_ONE_AL):
                                    self.BUY_Opportunity += 1
                                    WARNİNG_BUSD = 0
                                    STOP_BUSD += True
                                    LOOP_RETURN += True
                                    print("Normal Buying Function Activate !")
                                    break
                                elif float(UCUNCU_ANLIK_FIYAT_BUSD) >= float(AL_MultiChain_ONE[0]) + (float(AL_MultiChain_ONE[0] * 1.0) / 100):
                                    Hight_PRİCE()
                                    self.BUY_Opportunity += 1
                                    WARNİNG_BUSD = 0
                                    STOP_BUSD += True
                                    LOOP_RETURN += True
                                    print("Hight Price Function Activate !")
                                    break
                                elif float(UCUNCU_ANLIK_FIYAT_BUSD) >= float(AL_MultiChain_ONE[0]) + (float(AL_MultiChain_ONE[0] * 0.5) / 100) and BUY_ZARAR_KURTARMA == False:
                                    print("{} Buying Zarar Kurtarma Function !".format(DEMO))
                                    print("{} Tüm Emirler İptal Edildi.".format(DEMO))
                                    self.KAZANILAN_BAKİYE += self.KAZANC_BALANCE
                                    ZARAR_KURTARMA_BALANCE = 0
                                    ZARAR_KURTARMA_PRİCE = 0
                                    ZARAR_KURTARMA_TETİKLE = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])

                                    def ZARAR_KURTARMA(Price=AL_MultiChain_ONE[0]):
                                        nonlocal ZARAR_KURTARMA_BALANCE, ZARAR_KURTARMA_PRİCE
                                        while True:
                                            try:
                                                ANLIK = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])
                                                Quantity = self.KAZANILAN_BAKİYE / float(ANLIK)
                                                PRİCE = Price

                                                self.KAZANILAN_BAKİYE -= self.KAZANILAN_BAKİYE
                                                ZARAR_KURTARMA_BALANCE += Quantity
                                                ZARAR_KURTARMA_PRİCE += Price
                                                print("{} Fiyatı : {} | Varlık : {} 'dan Alım Emri Verilmiştir.".format(DEMO, round(PRİCE, 3), round(Quantity, 6)))
                                            except:
                                                break
                                            break
                                    ZARAR_KURTARMA()

                                    while True:
                                        try:
                                            ANLIK = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])

                                            if ANLIK < ZARAR_KURTARMA_PRİCE:
                                                print("{} Satın Alım Başarılı.".format(DEMO))
                                                break

                                            elif (ZARAR_KURTARMA_TETİKLE * 101.5) / 100 < ANLIK:
                                                print("{} Tüm Emirler İptal Edildi.".format(DEMO))
                                                self.KAZANILAN_BAKİYE += self.KAZANC_BALANCE
                                                break
                                            else:
                                                time.sleep(1)
                                                print("{} {}:{}  | Waiting Buy.".format(DEMO,time.gmtime()[3]+3,time.gmtime()[4]))
                                        except:
                                            pass

                                elif WARNİNG_BUSD == 30:
                                    if self.NOTR_STOP == False and float(IKINCI_ANLIK_FIYAT_BUSD) - float(UCUNCU_ANLIK_FIYAT_BUSD) >= float(self.SORUMLU_COİN_ONE_AL) - (float(self.SORUMLU_COİN_ONE_AL * 9.0) / 100):
                                        Dump_BUSD()
                                        WARNİNG_BUSD = 0
                                        STOP_BUSD += True
                                        LOOP_RETURN += True
                                        print("Dump Order Function Activate !")
                                        break
                                    if self.NOTR_STOP == False and float(UCUNCU_ANLIK_FIYAT_BUSD) - float(IKINCI_ANLIK_FIYAT_BUSD) >= (float(IKINCI_ANLIK_FIYAT_BUSD) * 0.5) / 100:  # PUMP
                                        Pump_BUSD()
                                        WARNİNG_BUSD = 0
                                        STOP_BUSD += True
                                        LOOP_RETURN += True
                                        print("Pump Order Function Activate !")
                                        break
                                elif WARNİNG_BUSD == 20:
                                    if self.NOTR_STOP == False and float(IKINCI_ANLIK_FIYAT_BUSD) - float(UCUNCU_ANLIK_FIYAT_BUSD) >= float(self.SORUMLU_COİN_ONE_AL) - (float(self.SORUMLU_COİN_ONE_AL * 8.5) / 100):
                                        Dump_BUSD()
                                        WARNİNG_BUSD = 0
                                        STOP_BUSD += True
                                        LOOP_RETURN += True
                                        print("Dump Order Function Activate !")
                                        break
                                    if self.NOTR_STOP == False and float(UCUNCU_ANLIK_FIYAT_BUSD) - float(IKINCI_ANLIK_FIYAT_BUSD) >= (float(IKINCI_ANLIK_FIYAT_BUSD) * 0.6) / 100:
                                        Pump_BUSD()
                                        WARNİNG_BUSD = 0
                                        STOP_BUSD += True
                                        LOOP_RETURN += True
                                        print("Pump Order Function Activate !")
                                        break
                                elif WARNİNG_BUSD == 10:
                                    if self.NOTR_STOP == False and float(IKINCI_ANLIK_FIYAT_BUSD) - float(UCUNCU_ANLIK_FIYAT_BUSD) >= float(self.SORUMLU_COİN_ONE_AL) - (float(self.SORUMLU_COİN_ONE_AL * 8.0) / 100):
                                        Dump_BUSD()
                                        WARNİNG_BUSD = 0
                                        STOP_BUSD += True
                                        LOOP_RETURN += True
                                        print("Dump Order Function Activate !")
                                        break
                                    if self.NOTR_STOP == False and float(UCUNCU_ANLIK_FIYAT_BUSD) - float(IKINCI_ANLIK_FIYAT_BUSD) >= (float(IKINCI_ANLIK_FIYAT_BUSD) * 0.7) / 100:
                                        Pump_BUSD()
                                        WARNİNG_BUSD = 0
                                        STOP_BUSD += True
                                        LOOP_RETURN += True
                                        print("Pump Order Function Activate !")
                                        break
                                elif WARNİNG_BUSD == 1:
                                    if self.NOTR_STOP == False and float(IKINCI_ANLIK_FIYAT_BUSD) - float(UCUNCU_ANLIK_FIYAT_BUSD) >= float(self.SORUMLU_COİN_ONE_AL) - (float(self.SORUMLU_COİN_ONE_AL * 7.5) / 100):
                                        Dump_BUSD()
                                        WARNİNG_BUSD = 0
                                        STOP_BUSD += True
                                        LOOP_RETURN += True
                                        print("Dump Order Function Activate !")
                                        break
                                    if self.NOTR_STOP == False and float(UCUNCU_ANLIK_FIYAT_BUSD) - float(IKINCI_ANLIK_FIYAT_BUSD) >= (float(IKINCI_ANLIK_FIYAT_BUSD) * 0.8) / 100:
                                        Pump_BUSD()
                                        WARNİNG_BUSD = 0
                                        STOP_BUSD += True
                                        LOOP_RETURN += True
                                        print("Pump Order Function Activate !")
                                        break
                                elif CANCEL_SAYAC == 900 or CANCEL_SAYAC == 1800 or CANCEL_SAYAC == 2700 or CANCEL_SAYAC == 3600 or CANCEL_SAYAC == 4500 or CANCEL_SAYAC == 5400 or CANCEL_SAYAC == 6300 or CANCEL_SAYAC == 7200 or CANCEL_SAYAC == 8100 or CANCEL_SAYAC == 9000 or CANCEL_SAYAC == 9900 or CANCEL_SAYAC == 10798:
                                    if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)) >= 0.001:
                                        WARNİNG_BUSD = 0
                                        STOP_BUSD += True
                                        LOOP_RETURN += True
                                        AL_MultiChain_ONE.clear()
                                elif LossAlgorithm == True and CANCEL_SAYAC == 10800:
                                    try:
                                        orders = ROB.get_open_orders(symbol=self.SORUMLU_COİN_ONE)
                                        orders_ID = orders[0]['orderId']
                                        Intelence.ROB_CANCEL(symbol=self.SORUMLU_COİN_ONE, orderID=orders_ID)
                                    except:
                                        pass
                                    time.sleep(1)
                                    CANCEL_SAYAC -= CANCEL_SAYAC
                                    WARNİNG_BUSD -= 40
                                    STOP_BUSD += True
                                    LOOP_RETURN += True
                                    self.CANCEL_CONTROL += 1
                                    AL_MultiChain_ONE.clear()
                                    break
                            except:
                                print("Tekrardan Bağlantı Sağlanıyor.")
                elif BALANCE >= 0.001:
                    SORUMLU_COİN_BALANCE = self.SORUMLU_COİN_ONE.replace('BUSD', '')
                    SAT_MultiChain_ONE = list()
                    MAX_MultiChain_ONE = list()
                    TİME_ZONE = list()
                    CANCEL_SAYAC_BALANCE = 0
                    STOP = False

                    while True:
                        try:
                            if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)) <= 0.001:
                                break
                            else:
                                time.sleep(1)
                                Multi_Chain_SELL_START()
                                print("Try Again Sell Order...")
                        except:
                            print("Tekrardan Bağlantı Sağlanıyor.")

                    orders = ROB.get_open_orders(symbol=self.SORUMLU_COİN_ONE)
                    orders_ID = orders[0]['orderId']
                    ORDER_ID = str(orders_ID)

                    ILK_ANLIK_FIYAT = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])
                    SAT_MultiChain_ONE.append(float(ILK_ANLIK_FIYAT))
                    MAX_MultiChain_ONE.append(float(ILK_ANLIK_FIYAT))
                    while True:
                        WARNİNG = 40
                        TRY_TİME = 0
                        IKINCI_ANLIK_FIYAT = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])

                        if STOP == True:
                            break

                        def NOW_MARKETİNG_STR_DATA():
                            if self.PİYASA_DURUMU == 1:
                                return "Dalgalı Piyasa"
                            elif self.PİYASA_DURUMU == 2:
                                return "Yüksek Dalgalı"
                            elif self.PİYASA_DURUMU == 3:
                                return "Nötr"
                            elif self.PİYASA_DURUMU == 4:
                                return "Yüksek Nötr"
                            elif self.PİYASA_DURUMU == 5:
                                return "Pump"
                            elif self.PİYASA_DURUMU == 6:
                                return "Yüksek Pump"
                            elif self.PİYASA_DURUMU == 7:
                                return "Dump"
                            elif self.PİYASA_DURUMU == 8:
                                return "Yüksek Dump"

                        def LOW_PRİCE():
                            try:
                                orders = ROB.get_open_orders(symbol=self.SORUMLU_COİN_ONE)
                                orders_ID = orders[0]['orderId']
                                Intelence.ROB_CANCEL(symbol=self.SORUMLU_COİN_ONE, orderID=orders_ID)
                            except:
                                print("Tekrardan Bağlantı Sağlanıyor.")
                            self.MultiChain_OPTİON()
                            Sensor_STOP = False

                            SORUMLU_COİN_ONE = self.SORUMLU_COİN_ONE
                            SORUMLU_COİN_BALANCE = self.SORUMLU_COİN_ONE.replace('BUSD', '')
                            SORUMLU_COİN_ONE_AL = self.SORUMLU_COİN_ONE_AL
                            SORUMLU_COİN_ONE_SAT = self.SORUMLU_COİN_ONE_SAT

                            STOP_FUNCTİON_BUY_PRİCE = round(float(SORUMLU_COİN_ONE_AL), 1)
                            STOP_FUNCTİON_SELL_PRİCE = round((float(SORUMLU_COİN_ONE_SAT * 40) / 100), 1)
                            STEP = 0

                            def STOP_FUNCTİON_BUY(Price=STOP_FUNCTİON_BUY_PRİCE):
                                while True:
                                    try:
                                        BUSD = float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol='BUSD'))
                                        ANLIK = float(ROB.get_ticker(symbol=SORUMLU_COİN_ONE)['lastPrice'])
                                        Quantity = math.floor(float(BUSD)) / float(ANLIK)
                                        STEP = get_round_step_quantity(qty=Quantity)
                                        PRİCE = float(ANLIK) - Price
                                        Intelence.ROB_BUY_LİMİT(symbol=SORUMLU_COİN_ONE, quantity=float(STEP), price=str(PRİCE))
                                    except:
                                        print("Try Again BUY Order...")
                                        break
                                    break

                            def STOP_FUNCTİON_SELL(Price=STOP_FUNCTİON_SELL_PRİCE):
                                while True:
                                    try:
                                        BALANCE = Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)
                                        NEW_BALANCE = float(BALANCE)
                                        ANLIK = float(ROB.get_ticker(symbol=SORUMLU_COİN_ONE)['lastPrice'])
                                        PRİCE = float(ANLIK) + float(Price)
                                        Intelence.ROB_SELL_LİMİT(symbol=SORUMLU_COİN_ONE, quantity=float(NEW_BALANCE), price=str(PRİCE))  # SAT LİMİT EMRİ # HEDEFE GÖRE AYARLANACAK
                                    except:
                                        print("Try Again SELL Order...")
                                        break
                                    break

                            def SECURTY_SELL():
                                try:
                                    Sensor_STOP_Orders = ROB.get_open_orders(symbol=SORUMLU_COİN_ONE)
                                    Sensor_STOP_Orders_ID = Sensor_STOP_Orders[0]['orderId']
                                    Intelence.ROB_CANCEL(symbol=SORUMLU_COİN_ONE, orderID=str(Sensor_STOP_Orders_ID))
                                except:
                                    pass

                                def SECURİTY_SELL_ORDER():
                                    while True:
                                        try:
                                            Sensor_CRYPTO_BALANCE = Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)
                                            Sensor_CRYPTO_PRİCE = float(Sensor_CRYPTO_BALANCE)
                                            Intelence.ROB_SELL_MARKET(symbol=SORUMLU_COİN_ONE, quantity=Sensor_CRYPTO_PRİCE)
                                        except:
                                            break
                                        break

                                while True:
                                    try:
                                        if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)) < 0.001:
                                            break
                                        else:
                                            time.sleep(1)
                                            SECURİTY_SELL_ORDER()
                                            print("Security Sell Order...")
                                    except:
                                        pass

                            if (SORUMLU_COİN_ONE == "BTCBUSD" or SORUMLU_COİN_ONE == "SOLBUSD") and SORUMLU_COİN_ONE_AL < (float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice']) * 0.5) / 100:
                                SORUMLU_COİN_ONE_AL *= 2

                            while True:
                                try:
                                    if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)) <= 0.001:
                                        break
                                    else:
                                        time.sleep(1)
                                        STOP_FUNCTİON_SELL()
                                        print("Low Price SELL Order...")
                                except:
                                    print("Tekrardan Bağlantı Sağlanıyor.")

                            STOP_FUNCTİON_SELL_ANLIK = float(ROB.get_ticker(symbol=SORUMLU_COİN_ONE)['lastPrice'])
                            while True:
                                try:
                                    print("Low Price Function Last Loop !")
                                    time.sleep(2)

                                    if Sensor_STOP == True:
                                        break

                                    elif float(STOP_FUNCTİON_SELL_ANLIK * 99) / 100 > float(ROB.get_ticker(symbol=SORUMLU_COİN_ONE)['lastPrice']):
                                        while True:
                                            try:
                                                if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)) <= 0.001:
                                                    sys.exit()
                                                    break
                                                else:
                                                    time.sleep(2)
                                                    SECURTY_SELL()
                                                    print("Maksimum Zarar Algılandı !")
                                            except:
                                                print("Tekrardan Bağlantı Sağlanıyor.")
                                    elif STOP_FUNCTİON_SELL_PRİCE + STOP_FUNCTİON_SELL_ANLIK < float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol='BUSD')):
                                        Sensor_STOP += True
                                        break
                                except:
                                    print("Tekrardan Bağlantı Sağlanıyor.")
                            while True:
                                try:
                                    if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol='BUSD')) <= 10:
                                        break
                                    else:
                                        time.sleep(1)
                                        STOP_FUNCTİON_BUY()
                                        print("Low Price BUY Order...")
                                except:
                                    print("Tekrardan Bağlantı Sağlanıyor.")

                        def DUMP():
                            print("DUMP DETECTED I !")
                            TRY_TİME = 0
                            STOP_TRY_TİME = False
                            STOP_MultiChain_ONE = list()

                            try:
                                orders = ROB.get_open_orders(symbol=self.SORUMLU_COİN_ONE)
                                orders_ID = orders[0]['orderId']
                                Intelence.ROB_CANCEL(symbol=self.SORUMLU_COİN_ONE, orderID=str(orders_ID))
                                time.sleep(2)
                            except:
                                print("Tekrardan Bağlantı Sağlanıyor.")

                            def DUMP_START():
                                while True:
                                    try:
                                        BALANCE = Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)
                                        NEW_BALANCE = float(BALANCE)
                                        EMİR = Intelence.ROB_SELL_MARKET(symbol=self.SORUMLU_COİN_ONE, quantity=float(NEW_BALANCE))
                                    except:
                                        break
                                    break

                            while True:
                                try:
                                    if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)) <= 0.001:
                                        break
                                    else:
                                        time.sleep(1)
                                        DUMP_START()
                                        print("Try Again DUMP Sell Order...")
                                except:
                                    print("Tekrardan Bağlantı Sağlanıyor.")

                            DUMP_START_PRİCE = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])
                            STOP_MultiChain_ONE.append(float(DUMP_START_PRİCE))
                            while TRY_TİME < 14400:
                                time.sleep(1)
                                TRY_TİME += 1
                                DUMP = 15
                                DUMP_DEGİSMEYEN_FIYAT = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])
                                print("DUMP CONTROL I !")

                                if STOP_TRY_TİME == True:
                                    break

                                while DUMP > 0:
                                    print("DUMP CONTROL II !")
                                    time.sleep(1)
                                    DUMP -= 1
                                    DUMP_DEGİSEN_FIYAT = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])

                                    if (float(DUMP_DEGİSEN_FIYAT) <= STOP_MultiChain_ONE[0]) and (float(DUMP_DEGİSMEYEN_FIYAT) + ((float(DUMP_DEGİSMEYEN_FIYAT) * 0.35) / 100) <= float(DUMP_DEGİSEN_FIYAT)):
                                        print("DUMP OPTİON I TRUE")

                                        class DUMP_ONE_BUSD():
                                            def DUMP_OPTİON_START():
                                                while True:
                                                    try:
                                                        EXCEPT_CRYPTO_BALANCE = Intelence.ROB_ACCOUNT_GET_BALANCE(symbol='BUSD')
                                                        EXCEPT_CRYPTO_ANLIK = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])
                                                        Quantity = math.floor(float(EXCEPT_CRYPTO_BALANCE)) / float(EXCEPT_CRYPTO_ANLIK)
                                                        STEP = get_round_step_quantity(qty=Quantity)
                                                        Intelence.ROB_BUY_MARKET(symbol=self.SORUMLU_COİN_ONE, quantity=STEP)
                                                    except:
                                                        break
                                                    break

                                            def DUMP_OPTİON_ONE():
                                                while True:
                                                    try:
                                                        BALANCE = Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)
                                                        NEW_BALANCE = float(BALANCE)
                                                        ANLIK = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])
                                                        PRİCE = float(ANLIK) + ((float(ANLIK) * 0.3) / 100)
                                                        Intelence.ROB_SELL_LİMİT(symbol=self.SORUMLU_COİN_ONE, quantity=float(NEW_BALANCE), price=str(PRİCE))
                                                    except:
                                                        break
                                                    break

                                        while True:
                                            try:
                                                if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol='BUSD')) <= 10:
                                                    break
                                                else:
                                                    time.sleep(1)
                                                    DUMP_ONE_BUSD.DUMP_OPTİON_START()
                                                    print("Try Again DUMP Buy Order...")
                                            except:
                                                print("Tekrardan Bağlantı Sağlanıyor.")

                                        while True:
                                            try:
                                                if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)) <= 0.001:
                                                    DUMP -= 15
                                                    STOP_TRY_TİME += True
                                                    break
                                                else:
                                                    time.sleep(1)
                                                    DUMP_ONE_BUSD.DUMP_OPTİON_ONE()
                                                    print("Try Again DUMP Sell Order...")
                                            except:
                                                print("Tekrardan Bağlantı Sağlanıyor.")
                                        break

                                    elif float(DUMP_DEGİSEN_FIYAT) > (STOP_MultiChain_ONE[0] * 101) / 100:
                                        print("DUMP OPTİON II TRUE")
                                        TİME_ZONE.append(float(DUMP_DEGİSEN_FIYAT))
                                        TİME_ZONE_SECOND_DUMP = 14400
                                        DUMP_OPTİON_START_ORDER_ID = ""

                                        class DUMP_ONE_BUSD():
                                            def DUMP_OPTİON_START():
                                                while True:
                                                    time.sleep(1)
                                                    try:
                                                        BUSD = Intelence.ROB_ACCOUNT_GET_BALANCE(symbol='BUSD')
                                                        ANLIK = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])
                                                        Quantity = math.floor(float(BUSD)) / float(ANLIK)
                                                        STEP = get_round_step_quantity(qty=Quantity)
                                                        PRİCE = float(ANLIK) - ((float(ANLIK * 0.4) / 100))
                                                        Intelence.ROB_BUY_LİMİT(symbol=self.SORUMLU_COİN_ONE, quantity=float(STEP), price=str(PRİCE))
                                                    except:
                                                        break
                                                    break

                                            def DUMP_OPTİON_ONE():
                                                while True:
                                                    try:
                                                        BALANCE = Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)
                                                        NEW_BALANCE = float(BALANCE)
                                                        ANLIK = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])
                                                        PRİCE = float(ANLIK) + ((float(ANLIK) * 0.5) / 100)
                                                        Intelence.ROB_SELL_LİMİT(symbol=self.SORUMLU_COİN_ONE, quantity=float(NEW_BALANCE), price=str(PRİCE))
                                                    except:
                                                        break
                                                    break

                                            def DUMP_OPTİON_TWO():
                                                try:
                                                    Intelence.ROB_CANCEL(symbol=self.SORUMLU_COİN_ONE, orderID=str(DUMP_OPTİON_START_ORDER_ID))
                                                except:
                                                    pass
                                                while True:
                                                    try:
                                                        BUSD = Intelence.ROB_ACCOUNT_GET_BALANCE(symbol='BUSD')
                                                        ANLIK = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])
                                                        Quantity = math.floor(float(BUSD)) / float(ANLIK)
                                                        STEP = get_round_step_quantity(qty=Quantity)
                                                        PRİCE = float(ANLIK) - ((float(ANLIK * 0.6) / 100))
                                                        Intelence.ROB_BUY_LİMİT(symbol=self.SORUMLU_COİN_ONE, quantity=float(STEP), price=str(PRİCE))
                                                    except:
                                                        break
                                                    break

                                        while True:
                                            try:
                                                if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol='BUSD')) <= 10:
                                                    break
                                                else:
                                                    time.sleep(1)
                                                    DUMP_ONE_BUSD.DUMP_OPTİON_START()
                                                    print("Try Again DUMP Buy Order...")
                                            except:
                                                print("Tekrardan Bağlantı Sağlanıyor.")

                                        orders = ROB.get_open_orders(symbol=self.SORUMLU_COİN_ONE)
                                        orders_ID = orders[0]['orderId']
                                        DUMP_OPTİON_START_ORDER_ID += str(orders_ID)
                                        while TİME_ZONE_SECOND_DUMP > 0:
                                            print("Balance DUMP I Loop !")
                                            time.sleep(2)
                                            TİME_ZONE_DEGİSEN_FIYAT_DUMP = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])
                                            TİME_ZONE_SECOND_DUMP -= 1

                                            if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)) > 0.001:
                                                while True:
                                                    try:
                                                        if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)) <= 0.001:
                                                            DUMP -= 15
                                                            STOP_TRY_TİME += True
                                                            break
                                                        else:
                                                            time.sleep(1)
                                                            DUMP_ONE_BUSD.DUMP_OPTİON_ONE()
                                                            print("Try Again DUMP Sell Order...")
                                                    except:
                                                        print("Tekrardan Bağlantı Sağlanıyor.")
                                                break

                                            elif float(TİME_ZONE_DEGİSEN_FIYAT_DUMP) >= float(TİME_ZONE[0] * 101) / 100:
                                                while True:
                                                    try:
                                                        if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol='BUSD')) <= 10:
                                                            DUMP -= 15
                                                            STOP_TRY_TİME += True
                                                            break
                                                        else:
                                                            time.sleep(1)
                                                            DUMP_ONE_BUSD.DUMP_OPTİON_TWO()
                                                            print("Try Again DUMP Buy Order...")
                                                    except:
                                                        print("Tekrardan Bağlantı Sağlanıyor.")
                                                break

                                            elif TİME_ZONE_SECOND_DUMP == 1:
                                                DUMP -= 15
                                                STOP_TRY_TİME += True
                                                break

                                    elif float(DUMP_DEGİSEN_FIYAT) <= (STOP_MultiChain_ONE[0] * 99.5) / 100:
                                        print("DUMP OPTİON III TRUE")

                                        class DUMP_ONE_BUSD():
                                            def DUMP_OPTİON_START():
                                                while True:
                                                    time.sleep(1)
                                                    try:
                                                        EXCEPT_CRYPTO_BALANCE = Intelence.ROB_ACCOUNT_GET_BALANCE(symbol='BUSD')
                                                        EXCEPT_CRYPTO_ANLIK = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])
                                                        Quantity = math.floor(float(EXCEPT_CRYPTO_BALANCE)) / float(EXCEPT_CRYPTO_ANLIK)
                                                        STEP = get_round_step_quantity(qty=Quantity)
                                                        Intelence.ROB_BUY_MARKET(symbol=self.SORUMLU_COİN_ONE, quantity=STEP)
                                                    except:
                                                        break
                                                    break

                                            def DUMP_OPTİON_ONE():
                                                while True:
                                                    try:
                                                        BALANCE = Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)
                                                        NEW_BALANCE = float(BALANCE)
                                                        ANLIK = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])
                                                        PRİCE = float(ANLIK) + ((float(ANLIK) * 0.3) / 100)
                                                        Intelence.ROB_SELL_LİMİT(symbol=self.SORUMLU_COİN_ONE, quantity=float(NEW_BALANCE), price=str(PRİCE))
                                                    except:
                                                        break
                                                    break

                                        while True:
                                            try:
                                                if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol='BUSD')) <= 10:
                                                    break
                                                else:
                                                    time.sleep(1)
                                                    DUMP_ONE_BUSD.DUMP_OPTİON_START()
                                                    print("Try Again DUMP Buy Order...")
                                            except:
                                                print("Tekrardan Bağlantı Sağlanıyor.")

                                        while True:
                                            try:
                                                if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)) <= 0.001:
                                                    DUMP -= 15
                                                    STOP_TRY_TİME += True
                                                    break
                                                else:
                                                    time.sleep(1)
                                                    DUMP_ONE_BUSD.DUMP_OPTİON_ONE()
                                                    print("Try Again DUMP Sell Order...")
                                            except:
                                                print("Tekrardan Bağlantı Sağlanıyor.")

                        def PUMP_EX():
                            TRY_TİME_EX = 0
                            STOP_TRY_TİME_EX = False
                            STOP_MultiChain_ONE = list()

                            def PUMP_EX_START():
                                while True:
                                    try:
                                        EXCEPT_CRYPTO_BALANCE = Intelence.ROB_ACCOUNT_GET_BALANCE(symbol='BUSD')
                                        EXCEPT_CRYPTO_ANLIK = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])
                                        Quantity = math.floor(float(EXCEPT_CRYPTO_BALANCE)) / float(EXCEPT_CRYPTO_ANLIK)
                                        STEP = get_round_step_quantity(qty=Quantity)
                                        Intelence.ROB_BUY_MARKET(symbol=self.SORUMLU_COİN_ONE, quantity=STEP)
                                    except:
                                        break
                                    break

                            while True:
                                try:
                                    if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol="BUSD")) < 10:
                                        break
                                    else:
                                        time.sleep(1)
                                        PUMP_EX_START()
                                        print("PUMP_EX_START Loop Try Again !")
                                except:
                                    print("Tekrardan Bağlantı Sağlanıyor.")

                            EXCEPT_ANLIK = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])
                            STOP_MultiChain_ONE.clear()
                            STOP_MultiChain_ONE.append(float(EXCEPT_ANLIK))
                            time.sleep(2)

                            while TRY_TİME < 14400:
                                time.sleep(1)
                                PUMP = 15
                                TRY_TİME += 1
                                PUMP_DEGİSMEYEN_FİYAT = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])
                                print("PUMP CONTROL I !")

                                if STOP_TRY_TİME_EX == True:
                                    break

                                while PUMP > 0:
                                    print("PUMP CONTROL II !")
                                    time.sleep(1)
                                    PUMP -= 1
                                    PUMP_DEGİSEN_FİYAT = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])

                                    if (float(PUMP_DEGİSEN_FİYAT) >= STOP_MultiChain_ONE[0]) and (float(PUMP_DEGİSMEYEN_FİYAT) - ((float(PUMP_DEGİSMEYEN_FİYAT * 0.40) / 100)) >= float(PUMP_DEGİSEN_FİYAT)):
                                        print("EXCEPT BLOCK PUMP OPTİON I TRUE")

                                        class PUMP_TWO_BUSD():
                                            def PUMP_OPTİON_START():
                                                while True:
                                                    try:
                                                        BALANCE = Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)
                                                        NEW_BALANCE = float(BALANCE)
                                                        EMİR = Intelence.ROB_SELL_MARKET(symbol=self.SORUMLU_COİN_ONE, quantity=float(NEW_BALANCE))
                                                    except:
                                                        break
                                                    break

                                            def PUMP_OPTİON_ONE():
                                                while True:
                                                    try:
                                                        BUSD = Intelence.ROB_ACCOUNT_GET_BALANCE(symbol='BUSD')
                                                        ANLIK = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])
                                                        QUANTİTY = math.floor(float(BUSD)) / float(ANLIK)
                                                        STEP = get_round_step_quantity(qty=QUANTİTY)
                                                        PRİCE = float(ANLIK) - ((float(ANLIK * 0.5) / 100))
                                                        EMİR = Intelence.ROB_BUY_LİMİT(symbol=self.SORUMLU_COİN_ONE, quantity=float(STEP), price=str(PRİCE))
                                                    except:
                                                        break
                                                    break

                                        while True:
                                            try:
                                                time.sleep(1)
                                                if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)) <= 0.001:
                                                    break
                                                else:
                                                    PUMP_TWO_BUSD.PUMP_OPTİON_START()
                                                    print("Try Again PUMP Sell Order...")
                                            except:
                                                print("Tekrardan Bağlantı Sağlanıyor.")

                                        while True:
                                            try:
                                                if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol='BUSD')) <= 10:
                                                    PUMP -= 15
                                                    STOP_TRY_TİME_EX += True
                                                    break
                                                else:
                                                    time.sleep(1)
                                                    PUMP_TWO_BUSD.PUMP_OPTİON_ONE()
                                                    print("Try Again PUMP Buy Order...")
                                            except:
                                                print("Tekrardan Bağlantı Sağlanıyor.")
                                        break

                                    elif float(PUMP_DEGİSEN_FİYAT) >= (STOP_MultiChain_ONE[0] * 101) / 100:
                                        print("EXCEPT BLOCK PUMP OPTİON II TRUE")

                                        class PUMP_TWO_BUSD():
                                            def PUMP_OPTİON_START():
                                                while True:
                                                    try:
                                                        BALANCE = Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)
                                                        NEW_BALANCE = float(BALANCE)
                                                        EMİR = Intelence.ROB_SELL_MARKET(symbol=self.SORUMLU_COİN_ONE, quantity=float(NEW_BALANCE))
                                                    except:
                                                        break
                                                    break

                                            def PUMP_OPTİON_ONE():
                                                while True:
                                                    try:
                                                        BUSD = Intelence.ROB_ACCOUNT_GET_BALANCE(symbol='BUSD')
                                                        ANLIK = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])
                                                        QUANTİTY = math.floor(float(BUSD)) / float(ANLIK)
                                                        STEP = get_round_step_quantity(qty=QUANTİTY)
                                                        PRİCE = float(ANLIK) - ((float(ANLIK * 0.5) / 100))
                                                        EMİR = Intelence.ROB_BUY_LİMİT(symbol=self.SORUMLU_COİN_ONE, quantity=float(STEP), price=str(PRİCE))
                                                    except:
                                                        break
                                                    break

                                        while True:
                                            try:
                                                time.sleep(1)
                                                if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)) <= 0.001:
                                                    break
                                                else:
                                                    PUMP_TWO_BUSD.PUMP_OPTİON_START()
                                                    print("Try Again PUMP Sell Order...")
                                            except:
                                                print("Tekrardan Bağlantı Sağlanıyor.")

                                        while True:
                                            try:
                                                if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol='BUSD')) <= 10:
                                                    PUMP -= 15
                                                    STOP_TRY_TİME_EX += True
                                                    break
                                                else:
                                                    time.sleep(1)
                                                    PUMP_TWO_BUSD.PUMP_OPTİON_ONE()
                                                    print("Try Again PUMP Buy Order...")
                                            except:
                                                print("Tekrardan Bağlantı Sağlanıyor.")
                                        break

                                    elif float(PUMP_DEGİSEN_FİYAT) <= (STOP_MultiChain_ONE[0] * 98.5) / 100:
                                        print("EXCEPT BLOCK PUMP OPTİON III TRUE")
                                        TİME_ZONE.append(float(PUMP_DEGİSEN_FİYAT))
                                        TİME_ZONE_SECOND_PUMP = 14400

                                        PUMP_OPTİON_START_ORDER_ID = ""

                                        class PUMP_TWO_BUSD():
                                            def PUMP_OPTİON_START():
                                                while True:
                                                    try:
                                                        BALANCE = Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)
                                                        ANLIK = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])
                                                        PRİCE = float(ANLIK) + ((float(ANLIK) * 0.6) / 100)
                                                        NEW_BALANCE = float(BALANCE)
                                                        EMİR = Intelence.ROB_SELL_LİMİT(symbol=self.SORUMLU_COİN_ONE, quantity=float(NEW_BALANCE), price=str(PRİCE))
                                                    except:
                                                        break
                                                    break

                                            def PUMP_OPTİON_ONE():
                                                while True:
                                                    try:
                                                        BUSD = Intelence.ROB_ACCOUNT_GET_BALANCE(symbol='BUSD')
                                                        ANLIK = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])
                                                        QUANTİTY = math.floor(float(BUSD)) / float(ANLIK)
                                                        STEP = get_round_step_quantity(qty=QUANTİTY)
                                                        PRİCE = float(ANLIK) - ((float(ANLIK * 0.7) / 100))
                                                        EMİR = Intelence.ROB_BUY_LİMİT(symbol=self.SORUMLU_COİN_ONE, quantity=float(STEP), price=str(PRİCE))
                                                    except:
                                                        break
                                                    break

                                            def PUMP_OPTİON_TWO():
                                                try:
                                                    Intelence.ROB_CANCEL(symbol=self.SORUMLU_COİN_ONE, orderID=str(PUMP_OPTİON_START_ORDER_ID))
                                                except:
                                                    pass
                                                while True:
                                                    try:
                                                        BALANCE = Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)
                                                        NEW_BALANCE = float(BALANCE)
                                                        ANLIK = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])
                                                        PRİCE = float(ANLIK) + ((float(ANLIK) * 0.8) / 100)
                                                        Intelence.ROB_SELL_LİMİT(symbol=self.SORUMLU_COİN_ONE, quantity=float(NEW_BALANCE), price=str(PRİCE))
                                                    except:
                                                        break
                                                    break

                                        while True:
                                            try:
                                                if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)) <= 0.001:
                                                    break
                                                else:
                                                    time.sleep(1)
                                                    PUMP_TWO_BUSD.PUMP_OPTİON_START()
                                                    print("Try Again PUMP Sell Order...")
                                            except:
                                                print("Tekrardan Bağlantı Sağlanıyor.")

                                        orders = ROB.get_open_orders(symbol=self.SORUMLU_COİN_ONE)
                                        orders_ID = orders[0]['orderId']
                                        PUMP_OPTİON_START_ORDER_ID += str(orders_ID)
                                        while TİME_ZONE_SECOND_PUMP >= 0:
                                            time.sleep(2)
                                            TİME_ZONE_SECOND_PUMP -= 1
                                            TİME_ZONE_DEGİSEN_FIYAT_PUMP = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])

                                            if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol='BUSD')) > 10:
                                                while True:
                                                    try:
                                                        if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol='BUSD')) <= 10:
                                                            PUMP -= 15
                                                            STOP_TRY_TİME_EX += True
                                                            break
                                                        else:
                                                            time.sleep(1)
                                                            PUMP_TWO_BUSD.PUMP_OPTİON_ONE()
                                                            print("Try Again PUMP Buy Order...")
                                                    except:
                                                        print("Tekrardan Bağlantı Sağlanıyor.")
                                                break

                                            elif float(TİME_ZONE_DEGİSEN_FIYAT_PUMP) <= float(TİME_ZONE[0] * 98.5) / 100:
                                                while True:
                                                    try:
                                                        if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)) <= 0.001:
                                                            PUMP -= 15
                                                            STOP_TRY_TİME_EX += True
                                                            break
                                                        else:
                                                            time.sleep(1)
                                                            PUMP_TWO_BUSD.PUMP_OPTİON_TWO()
                                                            print("Try Again PUMP Sell Order...")
                                                    except:
                                                        print("Tekrardan Bağlantı Sağlanıyor.")
                                                break

                                            elif TİME_ZONE_SECOND_PUMP == 1:
                                                PUMP -= 15
                                                STOP_TRY_TİME_EX += True
                                                break

                        def PUMP():
                            try:
                                print("PUMP DETECTED I !")
                                TRY_TİME = 0
                                STOP_TRY_TİME = False
                                STOP_MultiChain_ONE = list()

                                TRY_ANLIK = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])
                                STOP_MultiChain_ONE.append(float(TRY_ANLIK))

                                orders = ROB.get_open_orders(symbol=self.SORUMLU_COİN_ONE)
                                orders_ID = orders[0]['orderId']
                                Intelence.ROB_CANCEL(symbol=self.SORUMLU_COİN_ONE, orderID=orders_ID)

                                while TRY_TİME < 14400:
                                    time.sleep(1)
                                    PUMP = 15
                                    TRY_TİME += 1
                                    PUMP_DEGİSMEYEN_FİYAT = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])
                                    print("PUMP CONTROL I !")

                                    if STOP_TRY_TİME == True:
                                        break

                                    while PUMP > 0:
                                        print("PUMP CONTROL II !")
                                        time.sleep(1)
                                        PUMP -= 1
                                        PUMP_DEGİSEN_FİYAT = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])

                                        if (float(PUMP_DEGİSEN_FİYAT) >= STOP_MultiChain_ONE[0]) and (float(PUMP_DEGİSMEYEN_FİYAT) - ((float(PUMP_DEGİSMEYEN_FİYAT * 0.35) / 100)) >= float(PUMP_DEGİSEN_FİYAT)):
                                            print("PUMP OPTİON I TRUE")

                                            class PUMP_TWO_BUSD():
                                                def PUMP_OPTİON_START():
                                                    while True:
                                                        try:
                                                            BALANCE = Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)
                                                            NEW_BALANCE = float(BALANCE)
                                                            EMİR = Intelence.ROB_SELL_MARKET(symbol=self.SORUMLU_COİN_ONE, quantity=float(NEW_BALANCE))
                                                        except:
                                                            break
                                                        break

                                                def PUMP_OPTİON_ONE():
                                                    while True:
                                                        try:
                                                            BUSD = Intelence.ROB_ACCOUNT_GET_BALANCE(symbol='BUSD')
                                                            ANLIK = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])
                                                            QUANTİTY = math.floor(float(BUSD)) / float(ANLIK)
                                                            STEP = get_round_step_quantity(qty=QUANTİTY)
                                                            PRİCE = float(ANLIK) - ((float(ANLIK * 0.3) / 100))
                                                            EMİR = Intelence.ROB_BUY_LİMİT(symbol=self.SORUMLU_COİN_ONE, quantity=float(STEP), price=str(PRİCE))
                                                        except:
                                                            break
                                                        break

                                            while True:
                                                try:
                                                    time.sleep(1)
                                                    if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)) <= 0.001:
                                                        break
                                                    else:
                                                        PUMP_TWO_BUSD.PUMP_OPTİON_START()
                                                        print("Try Again PUMP Sell Order...")
                                                except:
                                                    print("Tekrardan Bağlantı Sağlanıyor.")

                                            while True:
                                                try:
                                                    if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol='BUSD')) <= 10:
                                                        PUMP -= 15
                                                        STOP_TRY_TİME += True
                                                        break
                                                    else:
                                                        time.sleep(1)
                                                        PUMP_TWO_BUSD.PUMP_OPTİON_ONE()
                                                        print("Try Again PUMP Buy Order...")
                                                except:
                                                    print("Tekrardan Bağlantı Sağlanıyor.")
                                            break

                                        elif float(PUMP_DEGİSEN_FİYAT) >= (STOP_MultiChain_ONE[0] * 100.5) / 100:
                                            print("PUMP OPTİON II TRUE")

                                            class PUMP_TWO_BUSD():
                                                def PUMP_OPTİON_START():
                                                    while True:
                                                        try:
                                                            BALANCE = Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)
                                                            NEW_BALANCE = float(BALANCE)
                                                            EMİR = Intelence.ROB_SELL_MARKET(symbol=self.SORUMLU_COİN_ONE, quantity=float(NEW_BALANCE))
                                                        except:
                                                            break
                                                        break

                                                def PUMP_OPTİON_ONE():
                                                    while True:
                                                        try:
                                                            BUSD = Intelence.ROB_ACCOUNT_GET_BALANCE(symbol='BUSD')
                                                            ANLIK = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])
                                                            QUANTİTY = math.floor(float(BUSD)) / float(ANLIK)
                                                            STEP = get_round_step_quantity(qty=QUANTİTY)
                                                            PRİCE = float(ANLIK) - ((float(ANLIK * 0.3) / 100))
                                                            EMİR = Intelence.ROB_BUY_LİMİT(symbol=self.SORUMLU_COİN_ONE, quantity=float(STEP), price=str(PRİCE))
                                                        except:
                                                            break
                                                        break

                                            while True:
                                                try:
                                                    time.sleep(1)
                                                    if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)) <= 0.001:
                                                        break
                                                    else:
                                                        PUMP_TWO_BUSD.PUMP_OPTİON_START()
                                                        print("Try Again PUMP Sell Order...")
                                                except:
                                                    print("Tekrardan Bağlantı Sağlanıyor.")
                                            while True:
                                                try:
                                                    if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol='BUSD')) <= 10:
                                                        PUMP -= 15
                                                        STOP_TRY_TİME += True
                                                        break
                                                    else:
                                                        time.sleep(1)
                                                        PUMP_TWO_BUSD.PUMP_OPTİON_ONE()
                                                        print("Try Again PUMP Buy Order...")
                                                except:
                                                    print("Tekrardan Bağlantı Sağlanıyor.")
                                            break

                                        elif float(PUMP_DEGİSEN_FİYAT) <= float(STOP_MultiChain_ONE[0] * 99) / 100:
                                            print("PUMP OPTİON III TRUE")
                                            TİME_ZONE.append(float(PUMP_DEGİSEN_FİYAT))
                                            TİME_ZONE_SECOND_PUMP = 14400

                                            PUMP_OPTİON_START_ORDER_ID = ""

                                            class PUMP_TWO_BUSD():
                                                def PUMP_OPTİON_START():
                                                    while True:
                                                        try:
                                                            BALANCE = Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)
                                                            ANLIK = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])
                                                            PRİCE = float(ANLIK) + ((float(ANLIK) * 0.4) / 100)
                                                            NEW_BALANCE = float(BALANCE)
                                                            EMİR = Intelence.ROB_SELL_LİMİT(symbol=self.SORUMLU_COİN_ONE, quantity=float(NEW_BALANCE), price=str(PRİCE))
                                                        except:
                                                            break
                                                        break

                                                def PUMP_OPTİON_ONE():
                                                    while True:
                                                        try:
                                                            BUSD = Intelence.ROB_ACCOUNT_GET_BALANCE(symbol='BUSD')
                                                            ANLIK = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])
                                                            QUANTİTY = math.floor(float(BUSD)) / float(ANLIK)
                                                            STEP = get_round_step_quantity(qty=QUANTİTY)
                                                            PRİCE = float(ANLIK) - ((float(ANLIK * 0.5) / 100))
                                                            EMİR = Intelence.ROB_BUY_LİMİT(symbol=self.SORUMLU_COİN_ONE, quantity=float(STEP), price=str(PRİCE))
                                                        except:
                                                            break
                                                        break

                                                def PUMP_OPTİON_TWO():
                                                    try:
                                                        Intelence.ROB_CANCEL(symbol=self.SORUMLU_COİN_ONE, orderID=str(PUMP_OPTİON_START_ORDER_ID))
                                                    except:
                                                        pass
                                                    while True:
                                                        try:
                                                            BALANCE = Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)
                                                            NEW_BALANCE = float(BALANCE)
                                                            ANLIK = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])
                                                            PRİCE = float(ANLIK) + ((float(ANLIK) * 0.6) / 100)
                                                            Intelence.ROB_SELL_LİMİT(symbol=self.SORUMLU_COİN_ONE, quantity=float(NEW_BALANCE), price=str(PRİCE))
                                                        except:
                                                            break
                                                        break

                                            while True:
                                                try:
                                                    if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)) <= 0.001:
                                                        break
                                                    else:
                                                        time.sleep(1)
                                                        PUMP_TWO_BUSD.PUMP_OPTİON_START()
                                                        print("Try Again PUMP Sell Order...")
                                                except:
                                                    print("Tekrardan Bağlantı Sağlanıyor.")

                                            orders = ROB.get_open_orders(symbol=self.SORUMLU_COİN_ONE)
                                            orders_ID = orders[0]['orderId']
                                            PUMP_OPTİON_START_ORDER_ID += str(orders_ID)
                                            while TİME_ZONE_SECOND_PUMP >= 0:
                                                print("Balance PUMP Loop !")
                                                time.sleep(2)
                                                TİME_ZONE_SECOND_PUMP -= 1
                                                TİME_ZONE_DEGİSEN_FIYAT_PUMP = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])

                                                if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol='BUSD')) > 10:
                                                    while True:
                                                        try:
                                                            if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol='BUSD')) <= 10:
                                                                PUMP -= 15
                                                                STOP_TRY_TİME += True
                                                                break
                                                            else:
                                                                time.sleep(1)
                                                                PUMP_TWO_BUSD.PUMP_OPTİON_ONE()
                                                                print("Try Again PUMP Buy Order...")
                                                        except:
                                                            print("Tekrardan Bağlantı Sağlanıyor.")
                                                    break

                                                elif float(TİME_ZONE_DEGİSEN_FIYAT_PUMP) <= float(TİME_ZONE[0] * 99) / 100:
                                                    while True:
                                                        try:
                                                            if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)) <= 0.001:
                                                                PUMP -= 15
                                                                STOP_TRY_TİME += True
                                                                break
                                                            else:
                                                                time.sleep(1)
                                                                PUMP_TWO_BUSD.PUMP_OPTİON_TWO()
                                                                print("Try Again PUMP Sell Order...")
                                                        except:
                                                            print("Tekrardan Bağlantı Sağlanıyor.")
                                                    break

                                                elif TİME_ZONE_SECOND_PUMP == 1:
                                                    PUMP -= 15
                                                    STOP_TRY_TİME += True
                                                    break
                            except:
                                PUMP_EX()

                        def KAARLILIK_KURTARICISI():
                            ekle = 0.0
                            close = SAT_MultiChain_ONE[0] + self.SORUMLU_COİN_ONE_SAT
                            opens = SAT_MultiChain_ONE[0]
                            while True:
                                value = (opens * (ekle)) / 100
                                if (float(opens) + float(value)) >= float(close):
                                    ekle += float(ekle)
                                    break
                                else:
                                    ekle += 0.005
                            return ekle

                        while WARNİNG > 0:
                            try:
                                time.sleep(1)
                                WARNİNG -= 1
                                CANCEL_SAYAC_BALANCE += 1
                                UCUNCU_ANLIK_FIYAT = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])
                                print("Multi C-ROB (I) Waiting !")
                                print("--------------------------------------")
                                print("Multi C-ROB (I) Coin: ", self.SORUMLU_COİN_ONE)
                                print("Multi C-ROB (I) Buy: ", round(float(self.SORUMLU_COİN_ONE_AL), 1))
                                print("Multi C-ROB (I) Sell: ", round(float(self.SORUMLU_COİN_ONE_SAT), 1))
                                print("Multi C-ROB (I) Genel Piyasa: ", Proposal.Market_STR)
                                print("Multi C-ROB (I) Anlık Piyasa: ", NOW_MARKETİNG_STR_DATA())
                                print("Toplam İşlem Ücretiniz : ", round(self.Fee, 4), end="$\n")
                                print("--------------------------------------")
                                print("Geçen Süre : ", CANCEL_SAYAC_BALANCE, end="\n\n\n\n")

                                # 1 = Dalgalı / 2 = Yuksek Dalgalı / 3 = Notr / 4 = Yuksek Notr / 5 = PUMP / 6 = Yuksek PUMP / 7 = DUMP / 8 = Yuksek DUMP /

                                if (self.NOTR_STOP == False) and float(UCUNCU_ANLIK_FIYAT) - float(IKINCI_ANLIK_FIYAT) >= float(self.SORUMLU_COİN_ONE_SAT) - (float(self.SORUMLU_COİN_ONE_SAT * 7.5) / 100):
                                    PUMP()
                                    WARNİNG = 0
                                    STOP = True
                                    LOOP_RETURN += True
                                    print("Pump Function Activate !")
                                    Return_Fee()
                                    time.sleep(1)
                                    break
                                elif (self.NOTR_STOP == False) and float(IKINCI_ANLIK_FIYAT) - float(UCUNCU_ANLIK_FIYAT) >= (float(IKINCI_ANLIK_FIYAT) * 0.8) / 100:
                                    DUMP()
                                    WARNİNG = 0
                                    STOP = True
                                    LOOP_RETURN += True
                                    print("Dump Function Activate !")
                                    Return_Fee()
                                    time.sleep(1)
                                    break
                                elif float(UCUNCU_ANLIK_FIYAT) > float(SAT_MultiChain_ONE[0]) + float(self.SORUMLU_COİN_ONE_SAT):
                                    self.SELL_Opportunity += 1
                                    WARNİNG = 0
                                    STOP = True
                                    LOOP_RETURN += True
                                    print("Normal Selling Function Activate !")
                                    Return_Fee()
                                    time.sleep(1)
                                    break
                                elif float(UCUNCU_ANLIK_FIYAT) <= float(SAT_MultiChain_ONE[0]) - (float(SAT_MultiChain_ONE[0] * 0.5) / 100):
                                    # Sorunsuz Çalışıyor
                                    print("Selling Zarardan Kurtarma Function I !")
                                    try:
                                        Intelence.ROB_CANCEL(symbol=self.SORUMLU_COİN_ONE, orderID=ORDER_ID)
                                        time.sleep(1)
                                    except:
                                        pass

                                    def ZARAR_KURTARMA(Price=SAT_MultiChain_ONE[0]):
                                        while True:
                                            try:
                                                BALANCE = Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)
                                                NEW_BALANCE = float(BALANCE)
                                                ANLIK = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])
                                                PRİCE = Price
                                                Intelence.ROB_SELL_LİMİT(symbol=self.SORUMLU_COİN_ONE, quantity=float(NEW_BALANCE), price=str(PRİCE))  # SAT LİMİT EMRİ # HEDEFE GÖRE AYARLANACAK
                                            except:
                                                break
                                            break

                                    while True:
                                        if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)) < 0.001:
                                            break
                                        else:
                                            time.sleep(1)
                                            ZARAR_KURTARMA()

                                    while True:
                                        print("Zarar Kurtarma Fonksiyon I Activated")
                                        if float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice']) > SAT_MultiChain_ONE[0]:
                                            WARNİNG = 0
                                            STOP = True
                                            LOOP_RETURN += True
                                            print("Normal Selling Function Activate !")
                                            break

                                        elif float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice']) <= (float(SAT_MultiChain_ONE[0] * 99.0) / 100):
                                            LOW_PRİCE()
                                            WARNİNG = 0
                                            STOP = True
                                            LOOP_RETURN += True
                                            print("Low Price Function Activate !")
                                            break

                                        else:
                                            time.sleep(1)
                                elif float(UCUNCU_ANLIK_FIYAT) > float(MAX_MultiChain_ONE[0]) * ((KAARLILIK_KURTARICISI() - 0.2 + 100) / 100):
                                    print("Selling Zarardan Kurtarma Function II !")
                                    self.SELL_Opportunity += 1
                                    WARNİNG = 0
                                    STOP = True
                                    LOOP_RETURN += True
                                    KAAR_STOP = False
                                    WARNİNG_KAAR_STOP = False
                                    while True:
                                        DORDUNCU_ANLIK_FIYAT = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])
                                        WARNİNG_KAAR = 40
                                        if KAAR_STOP == True:
                                            break

                                        while (WARNİNG_KAAR > 0):
                                            time.sleep(1)
                                            print("Düşüş Kaarı Modu Aktif !\n")
                                            print("Start Referans Noktası : ", UCUNCU_ANLIK_FIYAT)
                                            print("Stop  Referans Noktası : ", float(SAT_MultiChain_ONE[0]) * ((KAARLILIK_KURTARICISI() - 0.3) + 100) / 100)
                                            WARNİNG_KAAR -= 1
                                            BESİNCİ_ANLIK_FIYAT = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])

                                            if WARNİNG_KAAR_STOP == True:
                                                break

                                            if float(BESİNCİ_ANLIK_FIYAT) < (float(SAT_MultiChain_ONE[0]) * ((KAARLILIK_KURTARICISI() - 0.3) + 100) / 100):
                                                print("Düşüş Kaarı Modu Aktif !")
                                                try:
                                                    Cancel_STOP = ROB.get_open_orders(symbol=self.SORUMLU_COİN_ONE)
                                                    Cancel_STOP_ID = Cancel_STOP[0]['orderId']
                                                    Intelence.ROB_CANCEL(symbol=self.SORUMLU_COİN_ONE, orderID=Cancel_STOP_ID)
                                                    time.sleep(1)
                                                except:
                                                    print("Tekrardan Bağlantı Sağlanılıyor.")
                                                time.sleep(1)

                                                def DÜŞÜŞ_KAARI():
                                                    while True:
                                                        try:
                                                            BALANCE = Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)
                                                            NEW_BALANCE = float(BALANCE)
                                                            ANLIK = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])
                                                            PRİCE = (float(ANLIK) * 100.045) / 100
                                                            Intelence.ROB_SELL_LİMİT(symbol=self.SORUMLU_COİN_ONE, quantity=float(NEW_BALANCE), price=str(PRİCE))  # SAT LİMİT EMRİ # HEDEFE GÖRE AYARLANACAK
                                                        except:
                                                            break
                                                        break

                                                while True:
                                                    try:
                                                        if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)) < 0.001:
                                                            break
                                                        else:
                                                            DÜŞÜŞ_KAARI()
                                                            print("Try Again Düşüş Kaarı Function !")
                                                            time.sleep(1)
                                                    except:
                                                        print("Tekrardan Bağlantı Sağlanılıyor.")

                                                PRİCE = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice']) * 100.045 / 100
                                                while True:
                                                    try:
                                                        print("Zarardan Kurtarma Fonksiyon II Activated")
                                                        time.sleep(1)
                                                        if float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice']) > PRİCE:
                                                            print("Düşüş Kaarı Successful")
                                                            self.SELL_Opportunity += 1
                                                            WARNİNG = 0
                                                            STOP = True
                                                            LOOP_RETURN += True
                                                            KAAR_STOP += True
                                                            WARNİNG_KAAR_STOP += True
                                                            Return_Fee()
                                                            break
                                                        elif float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice']) < (PRİCE * 98.5) / 100:
                                                            def MAXİMUM_ZARAR():
                                                                while True:
                                                                    try:
                                                                        BALANCE = Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)
                                                                        NEW_BALANCE = float(BALANCE)
                                                                        EMİR = Intelence.ROB_SELL_MARKET(symbol=self.SORUMLU_COİN_ONE, quantity=float(NEW_BALANCE))
                                                                    except:
                                                                        break
                                                                    break

                                                            while True:
                                                                try:
                                                                    if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)) < 0.001:
                                                                        print("Maksimum Zarar Algılandı !")
                                                                        sys.exit()
                                                                        break
                                                                    else:
                                                                        MAXİMUM_ZARAR()
                                                                        time.sleep(1)
                                                                except:
                                                                    print("Tekrardan Bağlantı Sağlanılıyor.")
                                                    except:
                                                        print("Tekrardan Bağlantı Sağlanılıyor.")
                                            elif (self.NOTR_STOP == False) and float(BESİNCİ_ANLIK_FIYAT) - float(DORDUNCU_ANLIK_FIYAT) >= float(self.SORUMLU_COİN_ONE_SAT) - (float(self.SORUMLU_COİN_ONE_SAT * 7.5) / 100):
                                                KAAR_STOP += True
                                                break
                                            elif (self.NOTR_STOP == False) and float(DORDUNCU_ANLIK_FIYAT) - float(BESİNCİ_ANLIK_FIYAT) >= (float(DORDUNCU_ANLIK_FIYAT) * 0.8) / 100:
                                                KAAR_STOP += True
                                                break
                                            elif float(BESİNCİ_ANLIK_FIYAT) > float(SAT_MultiChain_ONE[0]) + float(self.SORUMLU_COİN_ONE_SAT):
                                                KAAR_STOP += True
                                                break
                                            elif float(BESİNCİ_ANLIK_FIYAT) <= float(SAT_MultiChain_ONE[0]) - (float(SAT_MultiChain_ONE[0] * 1.0) / 100):
                                                KAAR_STOP += True
                                                break
                                            elif float(BESİNCİ_ANLIK_FIYAT) <= float(SAT_MultiChain_ONE[0]) - (float(SAT_MultiChain_ONE[0] * 0.5) / 100):
                                                KAAR_STOP += True
                                                break
                                    Return_Fee()
                                    print("Ödeme Tutarı : ", round(self.Fee, 4), end="$\n")
                                    break
                                elif WARNİNG == 30:
                                    if self.NOTR_STOP == False and float(IKINCI_ANLIK_FIYAT) - float(UCUNCU_ANLIK_FIYAT) >= (float(IKINCI_ANLIK_FIYAT) * 0.5) / 100:  # DUMP
                                        DUMP()
                                        WARNİNG = 0
                                        STOP = True
                                        LOOP_RETURN += True
                                        print("Dump Function Activate !")
                                        Return_Fee()
                                        time.sleep(1)
                                        break
                                    if self.NOTR_STOP == False and float(UCUNCU_ANLIK_FIYAT) - float(IKINCI_ANLIK_FIYAT) >= float(self.SORUMLU_COİN_ONE_SAT) - (float(self.SORUMLU_COİN_ONE_SAT * 9.0) / 100):
                                        PUMP()
                                        WARNİNG = 0
                                        STOP = True
                                        LOOP_RETURN += True
                                        print("Pump Function Activate !")
                                        Return_Fee()
                                        time.sleep(1)
                                        break
                                elif WARNİNG == 20:
                                    if self.NOTR_STOP == False and float(IKINCI_ANLIK_FIYAT) - float(UCUNCU_ANLIK_FIYAT) >= (float(IKINCI_ANLIK_FIYAT) * 0.6) / 100:
                                        DUMP()
                                        WARNİNG = 0
                                        STOP = True
                                        LOOP_RETURN += True
                                        print("Dump Function Activate !")
                                        Return_Fee()
                                        time.sleep(1)
                                        break
                                    if self.NOTR_STOP == False and float(UCUNCU_ANLIK_FIYAT) - float(IKINCI_ANLIK_FIYAT) >= float(self.SORUMLU_COİN_ONE_SAT) - (float(self.SORUMLU_COİN_ONE_SAT * 8.5) / 100):
                                        PUMP()
                                        WARNİNG = 0
                                        STOP = True
                                        LOOP_RETURN += True
                                        print("Pump Function Activate !")
                                        Return_Fee()
                                        time.sleep(1)
                                        break
                                elif WARNİNG == 10:
                                    if self.NOTR_STOP == False and float(IKINCI_ANLIK_FIYAT) - float(UCUNCU_ANLIK_FIYAT) >= (float(IKINCI_ANLIK_FIYAT) * 0.7) / 100:
                                        DUMP()
                                        WARNİNG = 0
                                        STOP = True
                                        LOOP_RETURN += True
                                        print("Dump Function Activate !")
                                        Return_Fee()
                                        time.sleep(1)
                                        break
                                    if self.NOTR_STOP == False and float(UCUNCU_ANLIK_FIYAT) - float(IKINCI_ANLIK_FIYAT) >= float(self.SORUMLU_COİN_ONE_SAT) - (float(self.SORUMLU_COİN_ONE_SAT * 8.0) / 100):
                                        PUMP()
                                        WARNİNG = 0
                                        STOP = True
                                        LOOP_RETURN += True
                                        print("Pump Function Activate !")
                                        Return_Fee()
                                        time.sleep(1)
                                        break
                                elif WARNİNG == 1:
                                    if self.NOTR_STOP == False and float(IKINCI_ANLIK_FIYAT) - float(UCUNCU_ANLIK_FIYAT) >= (float(IKINCI_ANLIK_FIYAT) * 0.8) / 100:
                                        DUMP()
                                        WARNİNG = 0
                                        STOP = True
                                        LOOP_RETURN += True
                                        print("Dump Function Activate !")
                                        Return_Fee()
                                        time.sleep(1)
                                        break
                                    if self.NOTR_STOP == False and float(UCUNCU_ANLIK_FIYAT) - float(IKINCI_ANLIK_FIYAT) >= float(self.SORUMLU_COİN_ONE_SAT) - (float(self.SORUMLU_COİN_ONE_SAT * 7.5) / 100):
                                        PUMP()
                                        WARNİNG = 0
                                        STOP = True
                                        LOOP_RETURN += True
                                        print("Pump Function Activate !")
                                        Return_Fee()
                                        time.sleep(1)
                                        break
                                elif CANCEL_SAYAC_BALANCE == 900 or CANCEL_SAYAC_BALANCE == 1800 or CANCEL_SAYAC_BALANCE == 2700 or CANCEL_SAYAC_BALANCE == 3600 or CANCEL_SAYAC_BALANCE == 4500 or CANCEL_SAYAC_BALANCE == 5400 or CANCEL_SAYAC_BALANCE == 6300 or CANCEL_SAYAC_BALANCE == 7200 or CANCEL_SAYAC_BALANCE == 8100 or CANCEL_SAYAC_BALANCE == 9000 or CANCEL_SAYAC_BALANCE == 9900 or CANCEL_SAYAC_BALANCE == 10798:
                                    if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol='BUSD')) >= 10:
                                        WARNİNG = 0
                                        STOP += True
                                        LOOP_RETURN += True
                                        SAT_MultiChain_ONE.clear()
                                        MAX_MultiChain_ONE.clear()
                                        Return_Fee()
                                elif LossAlgorithm == True and CANCEL_SAYAC_BALANCE == 10800:
                                    try:
                                        orders = ROB.get_open_orders(symbol=self.SORUMLU_COİN_ONE)
                                        orders_ID = orders[0]['orderId']
                                        Intelence.ROB_CANCEL(symbol=self.SORUMLU_COİN_ONE, orderID=orders_ID)
                                        time.sleep(1)
                                    except:
                                        pass
                                    STOP += True
                                    LOOP_RETURN += True
                                    self.CANCEL_CONTROL += 1
                                    WARNİNG -= 40
                                    CANCEL_SAYAC_BALANCE -= CANCEL_SAYAC_BALANCE
                                    SAT_MultiChain_ONE.clear()
                                    MAX_MultiChain_ONE.clear()
                                    break
                            except:
                                print("Tekrardan Bağlantı Sağlanıyor.")

        def MultiChain_ONE():
            while True:
                try:
                    if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol='BUSD')) > 10:
                        self.MultiChain_START_CONTROL()
                except:
                    print("Tekrardan Bağlantı Sağlanılıyor.")

                self.MultiChain_OPTİON()
                print("Multi Chain Loop Returns !")
                print("-------------------------------------\n\n")
                print("Piyasa Durumu : ", self.PİYASA_DURUMU)
                print("-------------------------------------\n\n")
                time.sleep(2)

                if self.PİYASA_DURUMU == 1:
                    MultiChain_Algorithm(LossAlgorithm=True, ControlAlgorithm=True, SELL_OpportunityAlgorithm=True, BUY_OpportunityAlgorithm=True, WavyAlgorithm=True)
                elif self.PİYASA_DURUMU == 2:
                    MultiChain_Algorithm(LossAlgorithm=True, ControlAlgorithm=True, SELL_OpportunityAlgorithm=True, BUY_OpportunityAlgorithm=True, WavyAlgorithm=True)
                elif self.PİYASA_DURUMU == 3:
                    MultiChain_Algorithm(LossAlgorithm=True, ControlAlgorithm=True, SELL_OpportunityAlgorithm=True, BUY_OpportunityAlgorithm=True, WavyAlgorithm=True)
                elif self.PİYASA_DURUMU == 4:
                    MultiChain_Algorithm(LossAlgorithm=True, ControlAlgorithm=True, SELL_OpportunityAlgorithm=True, BUY_OpportunityAlgorithm=True, WavyAlgorithm=True)
                elif self.PİYASA_DURUMU == 5:
                    MultiChain_Algorithm(LossAlgorithm=True, ControlAlgorithm=True, SELL_OpportunityAlgorithm=True, BUY_OpportunityAlgorithm=True, WavyAlgorithm=True)
                elif self.PİYASA_DURUMU == 6:
                    MultiChain_Algorithm(LossAlgorithm=True, ControlAlgorithm=True, SELL_OpportunityAlgorithm=True, BUY_OpportunityAlgorithm=True, WavyAlgorithm=True)
                elif self.PİYASA_DURUMU == 7:
                    MultiChain_Algorithm(LossAlgorithm=True, ControlAlgorithm=True, SELL_OpportunityAlgorithm=True, BUY_OpportunityAlgorithm=True, WavyAlgorithm=True)
                elif self.PİYASA_DURUMU == 8:
                    MultiChain_Algorithm(LossAlgorithm=True, ControlAlgorithm=True, SELL_OpportunityAlgorithm=True, BUY_OpportunityAlgorithm=True, WavyAlgorithm=True)
                else:
                    MultiChain_Algorithm(LossAlgorithm=True, ControlAlgorithm=True, SELL_OpportunityAlgorithm=True, BUY_OpportunityAlgorithm=True, WavyAlgorithm=True)

        MultiChain = threading.Thread(target=MultiChain_ONE)
        MultiChain.start()


Constructor = Constructor()
Constructor.__str__()
MMChain = MultiChainAutoSystem()
