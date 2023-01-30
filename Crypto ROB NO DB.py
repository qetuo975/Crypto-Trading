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


class Intelence():
    # ROB EMİR FONKSİYONLARI
    def ROB_CANCEL(symbol,orderID):
        result = ROB.cancel_order(
            symbol=symbol,
            orderId=orderID)
        print("Cancel Order")
        print("Coin : ",symbol)
    def ROB_BUY_LİMİT(symbol,quantity,price):
        order = ROB.order_limit_buy(
            symbol=str(symbol),
            quantity=float(quantity),
            price=str(price))
        print("Order Successful !")
        print("Coin : ",symbol,"\nQuantity : ",quantity,"\nPrice : ",price)
    def ROB_SELL_LİMİT(symbol,quantity,price):
        order = ROB.order_limit_sell(
            symbol=str(symbol),
            quantity=float(quantity),
            price=str(price))
        print("Order Successful !")
        print("Coin : ",symbol,"\nQuantity : ",quantity,"\nPrice : ",price)
    def ROB_BUY_MARKET(symbol,quantity):
        order = ROB.order_market_buy(
            symbol=str(symbol),
            quantity=float(quantity))
        print("Market Order Successful !")
        print("Coin : ",symbol,"\nQuantity : ",quantity)
    def ROB_SELL_MARKET(symbol,quantity):
        order = ROB.order_market_sell(
            symbol=str(symbol),
            quantity=float(quantity))
        print("Market Order Successful !")
        print("Coin : ",symbol,"\nQuantity : ",quantity)

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
    def ROB_ACCOUNT_SNAPSHOT(params):      #TYPE = SPOT / MARGIN / FUTURES
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
        return order,amount
    def ROB_SPOT_HİSTORY_BOOK(symbol):
        price = list()
        amount = list()
        trades = ROB.get_recent_trades(symbol=symbol)
        for i in trades:
            price.append(i["price"])
            amount.append(i["qty"])
        price.reverse()
        amount.reverse()
        return price,amount
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
        print("Crypto ROB Private Version :",self.ACTİVE)
        print("\n\n\n")

    def Coin_Analysis(self):
        Coin,Value = self.Coin_Return()
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
        for i,j in Data:
            Coins_Values.append(j)
            Coins.append(i)
        return Coins, Coins_Values
class Transpitor():
    def __init__(self):
        self.Transpitor = Constructor.ACTİVE
        self.Transpitor.clear()
        self.Transpitor.append('BTCBUSD')

        #-------------------------------------
        #GEÇMİŞ HAFTALAR
        #-------------------------------------
        self.Bitcoin_PRİCE = 0
        self.Bitcoin_BUY = 0
        self.Bitcoin_SELL = 0
        self.Bitcoin_HİGHT = 0
        self.Bitcoin_LOW = 0
        self.Bitcoin_OPEN = 0
        self.Bitcoin_CLOSE = 0

        #------------------------------------
        #ŞUANKİ ZAMAN
        #------------------------------------
        self.NOW_Bitcoin_PRİCE = 0
        self.NOW_Bitcoin_BUY = 0
        self.NOW_Bitcoin_SELL = 0
        self.NOW_Bitcoin_HİGHT = 0
        self.NOW_Bitcoin_LOW = 0
        self.NOW_Bitcoin_OPEN = 0
        self.NOW_Bitcoin_CLOSE = 0

        #------------------------------------
        #Enginner
        #------------------------------------
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
                        btc = HistoricalData('BTC-USD', 900,("{}-{}-{}-{}-{}".format(years, month, days, hour, "00")),verbose=False).retrieve_data()
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
                        btc = HistoricalData('BTC-USD', 900,("{}-{}-{}-{}-{}".format(years, month, days, hour, "00")),verbose=False).retrieve_data()
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
                        btc = HistoricalData('BTC-USD', 900,("{}-{}-{}-{}-{}".format(years, month, days, hour, "00")),verbose=False).retrieve_data()
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
                        btc = HistoricalData('BTC-USD', 900,("{}-{}-{}-{}-{}".format(years, month, days, hour, "00")),verbose=False).retrieve_data()
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
                    print("Crypto ROB Private Core Versiyon !")
                    print("-----------------------------------------------------")
                    print("Acil PUMP Piyasa Yapılandırılıyor")
                    print("Bitcoin")
                    print("-----------------------------------------------------")
                    print("\n\n")
                    #self.BTC_KARMA_SELL += (self.BTC_KARMA_SELL * 40) / 100
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
                    #self.BTC_KARMA_SELL -= (self.BTC_KARMA_SELL * 40) / 100
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
                    #self.BTC_KARMA_SELL -= (self.BTC_KARMA_SELL * 50) / 100
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
                    #self.BTC_KARMA_SELL -= (self.BTC_KARMA_SELL * 30) / 100
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
                    #self.BTC_KARMA_SELL -= (self.BTC_KARMA_SELL * 50) / 100
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
                    #self.BTC_KARMA_SELL -= (self.BTC_KARMA_SELL * 30) / 100
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
            btc = HistoricalData('BTC-USD', 900, ("{}-{}-{}-{}-{}".format(years_new, month_new, days_new, "00", "00")),verbose=False).retrieve_data()
            self.NOW_Bitcoin_LOW += btc['low'][-1]
            self.NOW_Bitcoin_HİGHT += btc['high'][-1]
            self.NOW_Bitcoin_OPEN += btc['open'][-1]
            self.NOW_Bitcoin_CLOSE += btc['close'][-1]
    def NOW_Coins_PRİCE(self):
        for j in self.Transpitor:
            if j == "BTCBUSD":
                btc_price = LiveCryptoData('BTC-USD',verbose=False).return_data()
                btc_return = btc_price["price"][0]
                self.NOW_Bitcoin_PRİCE += float(btc_return)
    def NOW_Coins_HOUR(self):
        for j in self.Transpitor:
            if j == "BTCBUSD":
                def Data(params):
                    data = LiveCryptoData(params,verbose=False).return_data()
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
                    self.NOW_Bitcoin_SELL -=  (float(btc_price) * 0.40) / 100
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
                    self.NOW_Bitcoin_SELL -=  (float(btc_price) * 0.35) / 100
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
                    self.NOW_Bitcoin_SELL -=  (float(btc_price) * 0.30) / 100
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
                    self.NOW_Bitcoin_SELL -=  (float(btc_price) * 0.30) / 100
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
                    self.NOW_Bitcoin_SELL -=  (float(btc_price) * 0.20) / 100
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
                    self.NOW_Bitcoin_SELL -=  (float(btc_price) * 0.15) / 100
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
                    data = LiveCryptoData(params,verbose=False).return_data()
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
            btc = HistoricalData('BTC-USD', 86400,("{}-{}-{}-{}-{}".format(years, month, days, "00", "00")),verbose=False).retrieve_data()
            self.Bitcoin_LOW += btc['low'][0]
            self.Bitcoin_HİGHT += btc['high'][0]
            self.Bitcoin_OPEN += btc['open'][0]
            self.Bitcoin_CLOSE += btc['close'][0]
    def OLD_Coins_PRİCE(self):
        for j in self.Transpitor:
            if j == "BTCBUSD":
                btc_price = LiveCryptoData('BTC-USD',verbose=False).return_data()
                btc_return = btc_price["price"][0]
                self.Bitcoin_PRİCE += float(btc_return)
    def OLD_GENEL_PİYASA_DURUMU(self):
        def Data(params):
            data = LiveCryptoData(params,verbose=False).return_data()
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
        self.AFTER_ROB_BOOLEAN = False
        self.Hedef = 0
        self.MARKET_CONTROL()
        self.BUSD_CONTROL()
        self.CONTROL_SORGU()

        self.START_BALANCE = float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol='BUSD'))
        self.HEDEF()
        self.AFTER_ROB()

    def CONTROL_SORGU(self):
        CONTROL_İNPUT = input("Kontrol Sistemini Çalıştırmak İster Misiniz ? 'E' ya da 'Y' Yazınız. : ")
        if CONTROL_İNPUT == "e" or  CONTROL_İNPUT == "E":
            self.CONTROL_SYSTEMS += True
    def MARKET_CONTROL(self):
        if Proposal.Market_INT == 1 or Proposal.Market_INT == 2 or Proposal.Market_INT == -1 or  Proposal.Market_INT == -2:
            print("Bu Tür Piyasalarda Çalıştırmak Çok Risklidir.")
            Select = input("Yine de Çalıştırıacaksanız ' E ' | Yoksa ' Y ' Yazınız : ")
            if Select == "E" or Select == "e":
                pass
            if Select == "Y" or Select == "y":
                print("ROB Sonlanıyor.")
                time.sleep(2)
                sys.exit()
    def HEDEF(self):
        try:
            Reload = input("Hedefinizi Manuel Olarak Girmek İstermisiniz ? 'E' / 'Y' : ")
            if Reload == "E" or Reload == "e":
                self.AFTER_ROB_BOOLEAN += True
                Reload_NUMBER = int(input("Hedefiniz : "))
                self.Hedef = Reload_NUMBER
                print("Yeni Hedefiniz : ", self.Hedef, end="$\n")
            else:
                if Proposal.Market_INT == 1 or Proposal.Market_INT == -1 or Proposal.Market_INT == 2 or Proposal.Market_INT == -2:
                    BALANCE = Intelence.ROB_ACCOUNT_GET_BALANCE(symbol='BUSD')
                    self.Hedef = (float(BALANCE) * 100.5) / 100
                elif Proposal.Market_INT == 3 or Proposal.Market_INT == -3 or Proposal.Market_INT == 4 or Proposal.Market_INT == -4:
                    BALANCE = Intelence.ROB_ACCOUNT_GET_BALANCE(symbol='BUSD')
                    self.Hedef = (float(BALANCE) * 100.7) / 100
                elif Proposal.Market_INT == 5 or Proposal.Market_INT == -5 or Proposal.Market_INT == 6 or Proposal.Market_INT == -6 or Proposal.Market_INT == 7 or Proposal.Market_INT == -7:
                    BALANCE = Intelence.ROB_ACCOUNT_GET_BALANCE(symbol='BUSD')
                    self.Hedef = (float(BALANCE) * 100.9) / 100
                else:
                    BALANCE = Intelence.ROB_ACCOUNT_GET_BALANCE(symbol='BUSD')
                    self.Hedef = (float(BALANCE) * 100.5) / 100
                print("Hedefiniz Crypto ROB Tarafından Otomatik Olarak Ayarlandı : {}".format(round(self.Hedef,3)),end="$\n")
        except:
            print("Hedef Ayarlar Hatası.")
            print("Lütfen Hata Ayıklama Metnini Okuyunuz...")
    def AFTER_ROB(self):
        After_ROB = input("İlk Alım Emrini Siz Vermek İstiyor Musunuz ? 'E' / 'Y' : ")
        if After_ROB == "E" or After_ROB == "e":
            STEP = 0
            print("Seçilen Kripto Para Anlık Fiyat : {}".format(float(ROB.get_ticker(symbol="BTCBUSD")['lastPrice'])))
            After_ROB_ORDER = int(input("Alım Emri Fiyatı : "))

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
                        BALANCE = float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol="BUSD"))
                        Quantity = math.floor(float(BALANCE)) / float(ANLIK)
                        STEP = get_round_step_quantity(qty=Quantity)
                        PRİCE = After_ROB_ORDER
                        Intelence.ROB_BUY_LİMİT(symbol="BTCBUSD", quantity=float(STEP), price=str(PRİCE))
                    except:
                        break
                    break

            while True:
                try:
                    if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol="BUSD")) < 10:
                        break
                    else:
                        time.sleep(1)
                        After_ROB_ORDER_FUNCTİON()
                        print("After ROB Try Again...")
                except:
                    print("After ROB Loop Error I")
            while True:
                try:
                    if float(ROB.get_ticker(symbol="BTCBUSD")['lastPrice']) < int(After_ROB_ORDER):
                        break
                    else:
                        time.sleep(1)
                        print("Waiting Buy.")
                except:
                    print("After ROB Loop Error II")
            print("ROB Başlatılıyor. !")
    def BUSD_CONTROL(self):
        try:
            if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol='BUSD')) <= 10:
                print("BUSD Bakiyenizi En Az 10 BUSD Olarak Yapılandırınız.")
                time.sleep(5)
                sys.exit()
        except:
            print("Kontrol Ayarlar Hatası.")
            print("Lütfen Hata Ayıklama Metnini Okuyunuz...")
            time.sleep(20)
            sys.exit()

class MultiChainAutoSystem(Setting):
    def __init__(self):
        super().__init__()

        self.HEDEF = self.Hedef
        self.KAZANC_BALANCE = self.START_BALANCE
        self.AFTER_ROB = self.AFTER_ROB_BOOLEAN
        self.Fee = 0
        self.Fee_CONTROL = False

        self.SORUMLU_COİN_ONE = "None"
        self.SORUMLU_COİN_ONE_AL = 0
        self.SORUMLU_COİN_ONE_SAT = 0
        self.SORUMLU_COİN_ONE_DUSEN_DOLAR = 0

        self.PİYASA_DURUMU = 0
        self.CANCEL_CONTROL = 0
        
        #Opportunity Algorithm
        #-------------------------
        self.SELL_Opportunity = 0
        self.BUY_Opportunity = 0
        self.Opportunity_TETİKLE = 0
        # -------------------------
        
        #Wavy Algorithm
        #-------------------------
        self.WAVY_STOP = False
        #-------------------------

        #Notr Algorithm
        #-------------------------
        self.NOTR_STOP = False
        #-------------------------

        #Control Algorithm
        #-------------------------
        self.CONTROL_SYSTEM = self.CONTROL_SYSTEMS
        #-------------------------


        self.MultiChain_OPTİON()
        self.MultiChain_After_ROB()
        self.MultiChain()

        # 1 = Dalgalı / 2 = Yuksek Dalgalı / 3 = Notr / 4 = Yuksek Notr / 5 = PUMP / 6 = Yuksek PUMP / 7 = DUMP / 8 = Yuksek DUMP /
    def MultiChain_After_ROB(self):
        if self.AFTER_ROB == True:
            pass
        else:
            self.MultiChain_Fee_CONTROL()
            self.MultiChain_Fee_Configuration()
    def MultiChain_START_CONTROL(self):
        if self.CONTROL_SYSTEM == True:
            def CONTROL_SYSTEM(Crypto=Constructor.ACTİVE[0]):
                DATA_CRYPTO = ""
                SECOND = 0
                if Crypto == "BTCBUSD":
                    DATA_CRYPTO += "BTC-USD"


                while True:
                    if SECOND == 900:
                        break

                    else:
                        time.sleep(3)
                        SECOND += 3
                        print("Kontrol Sistemi Sonlanmasına : {} Saniye Kaldı.\n\n".format(int(900-SECOND)))
                        times = time.gmtime()
                        years = times[0]
                        month = times[1]
                        days = times[2]
                        hour = times[3] - 3

                        CRYPTO_DATA = HistoricalData(DATA_CRYPTO, 900, ("{}-{}-{}-{}-{}".format(years, month, days, "00", "00")),verbose=False).retrieve_data()
                        NOW_CRYPTO_LOW = CRYPTO_DATA['low'][-1]
                        NOW_CRYPTO_HİGHT = CRYPTO_DATA['high'][-1]
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

                        print("\nKontrol Sistemi Aktif !\n------------------------------")
                        print("Data Price : ", round(YUZDE, 7), end="%\n")
                        print("------------------------------")

                        if YUZDE > 0.10:
                            print("Kontrol Sistemi Sonlandırıldı, ROB Start !\n\n")
                            break

                        elif YUZDE < -0.35:
                            print("Warning Market Control I")
                            sys.exit()

                        elif YUZDE < -0.25:
                            SECOND += 3
                            print("Warning Market Control II")

                        elif YUZDE < -0.15:
                            STEP = 0
                            def get_round_step_quantity(qty):
                                global STEP
                                info = ROB.get_symbol_info(Constructor.ACTİVE[0])
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
                            def LOW_CONTROL_BUY(Oran):
                                while True:
                                    try:
                                        ANLIK = float(ROB.get_ticker(symbol=Constructor.ACTİVE[0])['lastPrice'])
                                        Quantity = math.floor(float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol='BUSD'))) / float(ANLIK)
                                        STEP = get_round_step_quantity(qty=Quantity)
                                        PRİCE = float(ANLIK) - (float(ANLIK * Oran) / 100)
                                        Intelence.ROB_BUY_LİMİT(symbol=Constructor.ACTİVE[0], quantity=float(STEP), price=str(PRİCE))
                                    except:
                                        break
                                    break
                            def LOW_CONTROL_SELL(Oran):
                                while True:
                                    try:
                                        SORUMLU_COİN = Constructor.ACTİVE[0]
                                        SORUMLU_COİN_BALANCE = SORUMLU_COİN.replace("BUSD", "")
                                        BALANCE = Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)
                                        NEW_BALANCE = float(BALANCE)
                                        ANLIK = float(ROB.get_ticker(symbol=SORUMLU_COİN)['lastPrice'])
                                        PRİCE = float(ANLIK) + (float(ANLIK * Oran) / 100)
                                        Intelence.ROB_SELL_LİMİT(symbol=SORUMLU_COİN, quantity=float(NEW_BALANCE), price=str(PRİCE))
                                    except:
                                        break
                                    break

                            VUR_KAC_STOPED = False
                            while True:
                                time.sleep(1)
                                if VUR_KAC_STOPED == True:
                                    SECOND += 1000
                                    break

                                else:
                                    CRYPTO = HistoricalData('BTC-USD', 3600, ("{}-{}-{}-{}-{}".format(years, month, days, str(hour), "00")),verbose=False).retrieve_data()
                                    OPEN = CRYPTO['open'][-2]
                                    CLOSE = CRYPTO['close'][-2]
                                    YUZDE_LOW = 0
                                    STEP = 0
                                    def POZİTİF_LOW():
                                        nonlocal YUZDE_LOW
                                        ekle = 0
                                        close = float(CLOSE)
                                        open = float(OPEN)
                                        while True:
                                            value = (open * (ekle)) / 100
                                            if (float(open) + float(value)) >= float(close):
                                                YUZDE_LOW += float(ekle)
                                                break
                                            else:
                                                ekle += 0.005
                                    def NEGATİF_LOW():
                                        nonlocal YUZDE_LOW
                                        ekle = 0
                                        close = float(CLOSE)
                                        open = float(OPEN)
                                        while True:
                                            value = (close * (ekle)) / 100
                                            if (float(close) + float(value)) >= float(open):
                                                YUZDE_LOW -= float(ekle)
                                                break
                                            else:
                                                ekle += 0.005
                                    POZİTİF_LOW()
                                    NEGATİF_LOW()

                                    if YUZDE_LOW > 0:
                                        break

                                    elif YUZDE_LOW < -0.30 or YUZDE_LOW < -0.25:
                                        CRYPTO_ACTİVE = "BTCBUSD"
                                        REPLACE = CRYPTO_ACTİVE.replace("BUSD","")
                                        print("Vur Kaç Yapılandırılıyor...")


                                        while True:
                                            try:
                                                if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol='BUSD')) < 10:
                                                    break
                                                else:
                                                    time.sleep(1)
                                                    LOW_CONTROL_BUY(Oran=0.10)
                                                    print("Vur Kaç Alım Loop.")
                                            except:
                                                print("Tekrardan Bağlantı Sağlanıyor.")
                                        BUY_ANLIK = float(ROB.get_ticker(symbol=CRYPTO_ACTİVE)['lastPrice'])


                                        orders = ROB.get_open_orders(symbol=CRYPTO_ACTİVE)
                                        orders_ID = orders[0]['orderId']


                                        STOP = False
                                        while True:
                                            try:
                                                time.sleep(2)

                                                if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=REPLACE)) > 0.0001:
                                                    break

                                                elif float(ROB.get_ticker(symbol=Constructor.ACTİVE[0])['lastPrice']) > float(BUY_ANLIK * 101) / 100:
                                                    Intelence.ROB_CANCEL(symbol=Constructor.ACTİVE[0],orderID=orders_ID)
                                                    STOP += True
                                                    break
                                            except:
                                                print("Tekrardan Bağlantı Sağlanıyor.")
                                        while True:
                                            try:
                                                if STOP == True:
                                                    break

                                                elif float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=REPLACE)) < 0.0001:
                                                    break

                                                else:
                                                    time.sleep(1)
                                                    LOW_CONTROL_SELL(Oran=0.10)
                                            except:
                                                print("Tekrardan Bağlantı Sağlanıyor.")
                                        SELL_ANLIK = (float(ROB.get_ticker(symbol=Constructor.ACTİVE[0])['lastPrice']) * 100.10) / 100


                                        orders = ROB.get_open_orders(symbol=Constructor.ACTİVE[0])
                                        orders_ID = orders[0]['orderId']


                                        while True:
                                            try:
                                                if STOP == True:
                                                    break


                                                elif float(ROB.get_ticker(symbol=Constructor.ACTİVE[0])['lastPrice']) > float(SELL_ANLIK):
                                                    VUR_KAC_STOPED += True
                                                    STOP += True
                                                    break


                                                elif (float(ROB.get_ticker(symbol=Constructor.ACTİVE[0])['lastPrice']) * 98.5) / 100 > float(SELL_ANLIK):
                                                    Intelence.ROB_CANCEL(symbol=Constructor.ACTİVE[0],orderID=orders_ID)
                                                    time.sleep(2)
                                                    def LOW_CONTROL_MARKETİNG():
                                                        while True:
                                                            try:
                                                                SORUMLU_COİN = Constructor.ACTİVE[0]
                                                                SORUMLU_COİN_BALANCE = SORUMLU_COİN.replace("BUSD","")
                                                                BALANCE = float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE))
                                                                EMİR = Intelence.ROB_SELL_MARKET(symbol=Constructor.ACTİVE[0], quantity=BALANCE)
                                                            except:
                                                                break
                                                            break
                                                    while True:
                                                        try:
                                                            if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=REPLACE)) < 0.0005:
                                                                sys.exit()
                                                                break
                                                            else:
                                                                time.sleep(1)
                                                                LOW_CONTROL_MARKETİNG()
                                                        except:
                                                            print("Tekrardan Bağlantı Sağlanıyor.")
                                            except:
                                                print("Tekrardan Bağlantı Sağlanıyor.")

                                    else:
                                        print("Vur Kaç Bekleniyor.")

                        elif YUZDE < -0.01:
                            if True:
                                print("Düşüş Devam Ediyor ! Lütfen ROB Başlatılmasını Bekleyin.\n\n")
                        elif YUZDE > 0.01:
                            if True:
                                print("Yükseliş Devam Ediyor ! Lütfen ROB Başlatılmasını Bekleyin.\n\n")
            CONTROL_SYSTEM()
        else:
            print("Kontrol Sistemi Zaten İptal Edildi !")
    def MultiChain_Fee_CONTROL(self):
        try:
            SORUMLU_COİN_BALANCE = self.SORUMLU_COİN_ONE.replace("BUSD", "")
            if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)) > 0.0001:
                print("Lütfen ' BTC ' Bakiyenizi BUSD Çeviriniz !")
                self.Fee_CONTROL = True

            if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol='BUSD')) <= 10:
                print("Lütfen BUSD Bakiyenizi En Az 10.00 Olacak Şekilde Yapılandırınız !")
                self.Fee_CONTROL = True
        except:
            print("Fee Ayarlar Hatası.")
            print("Lütfen Hata Ayıklama Metnini Okuyunuz...")
            time.sleep(10)
            sys.exit()
    def MultiChain_Fee_Configuration(self):
        if self.Fee_CONTROL == True:
            time.sleep(10)
            sys.exit()
    def MultiChain_OPTİON(self):
        TST = Transpitor()
        TST.__copy__()
        PİYASA_DURUMU = TST.__str__()
        def MultiChain_COİN_YERLESTIR():
            if TST.MultiChain_INT == 1:
                self.SORUMLU_COİN_ONE = Constructor.ACTİVE[0]
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
        def MultiChain_DUSEN_DOLAR_YERLESTIR():
            if TST.MultiChain_INT == 1:
                BUSD = Intelence.ROB_ACCOUNT_GET_BALANCE('BUSD')
                self.SORUMLU_COİN_ONE_DUSEN_DOLAR = float(BUSD)
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
        MultiChain_DUSEN_DOLAR_YERLESTIR()
        MultiChain_STOP_FUNCTİON()
    def MultiChain(self):
        def MultiChain_Algorithm(LossAlgorithm = bool, ControlAlgorithm = bool, SELL_OpportunityAlgorithm = bool, BUY_OpportunityAlgorithm = bool, WavyAlgorithm = bool):
            print("Crypto ROB (I) ON")
            STEP = 0
            SORUMLU_COİN_BALANCE = self.SORUMLU_COİN_ONE.replace("BUSD", "")
            def get_round_step_quantity(qty):
                global STEP
                info = ROB.get_symbol_info(self.SORUMLU_COİN_ONE)
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
            def Return_Fee():
                try:
                    KAAR = float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol='BUSD'))
                    KAAR_HESAPLAYICISI = round(float(self.KAZANC_BALANCE),2)

                    KAZANC = KAAR - KAAR_HESAPLAYICISI
                    KAZANC_NEW = float(KAZANC * 40) / 100

                    self.Fee += KAZANC_NEW
                    self.KAZANC_BALANCE = KAAR
                except:
                    print("Fee Error")
            def Multi_Chain_Hedef_Options():
                try:
                    RETURN_BUSD = ROB.get_asset_balance(asset='BUSD')
                    TOPLAM_BUSD = float(RETURN_BUSD['free']) + float(RETURN_BUSD['locked'])
                    if float(TOPLAM_BUSD) >= float(self.HEDEF):
                        try:
                            orders_one = ROB.get_open_orders(symbol=self.SORUMLU_COİN_ONE)
                            orders_ID = orders_one[0]['orderId']
                            Intelence.ROB_CANCEL(symbol=self.SORUMLU_COİN_ONE, orderID=str(orders_ID))
                        except:
                            pass
                        print("""
                                    Crypto ROB The Best Trading !
    
                                    Aim Succesful ! Setting Goals for the Game Again !
    
    
    
                                    Crypto ROB The Best Trading !
    
                                    Hedef Tamamlandı ! Tekrar Soyguna Başlamak İçin Hedefinizi Belirleyin !
                                                                                                                        """)

                        print("\nCrypto ROB The Best Trading !")
                        time.sleep(1)
                        sys.exit()
                        #os.system("shutdown /s /t 2")
                except:
                    print("Hedef Options Error")
            def Multi_Chain_BUY_START():
                while True:
                    try:
                        self.Opportunity_TETİKLE -= self.Opportunity_TETİKLE
                        ANLIK = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])
                        Quantity = math.floor(float(self.SORUMLU_COİN_ONE_DUSEN_DOLAR)) / float(ANLIK)
                        STEP = get_round_step_quantity(qty=Quantity)
                        PRİCE = float(ANLIK) - round(float(self.SORUMLU_COİN_ONE_AL), 1)
                        Intelence.ROB_BUY_LİMİT(symbol=self.SORUMLU_COİN_ONE, quantity=float(STEP), price=str(PRİCE))
                        self.Opportunity_TETİKLE += PRİCE
                    except:
                        break
                    break
            def Multi_Chain_SELL_START():
                while True:
                    try:
                        BALANCE = Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)
                        NEW_BALANCE = float(BALANCE)
                        ANLIK = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])
                        PRİCE = float(ANLIK) + round(float(self.SORUMLU_COİN_ONE_SAT), 1)
                        Intelence.ROB_SELL_LİMİT(symbol=self.SORUMLU_COİN_ONE, quantity=float(NEW_BALANCE), price=str(PRİCE))  # SAT LİMİT EMRİ # HEDEFE GÖRE AYARLANACAK
                    except:
                        break
                    break

            LOOP_RETURN = False
            while True:
                COİN_BALANCE = Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)
                BUSD_BALANCE = Intelence.ROB_ACCOUNT_GET_BALANCE(symbol='BUSD')
                BALANCE = float(COİN_BALANCE)
                BUSD = float(BUSD_BALANCE)
                Multi_Chain_Hedef_Options()

                time.sleep(3)
                if LOOP_RETURN == True:
                    time.sleep(1)
                    break
                elif ControlAlgorithm == True and self.CANCEL_CONTROL == 1:
                    time.sleep(2)
                    if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)) > 0.0001:
                        time.sleep(2)

                        if (float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice']) * 98.5) / 100 > float(self.Opportunity_TETİKLE):
                            time.sleep(2)
                            print("Control Algorithm I")
                            def ControlAlgorithm_I():
                                while True:
                                    try:
                                        BALANCE = Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)
                                        NEW_BALANCE = float(BALANCE)
                                        ANLIK = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])
                                        PRİCE = float(ANLIK) + (float(ANLIK * 100.7) / 100)
                                        Intelence.ROB_SELL_LİMİT(symbol=self.SORUMLU_COİN_ONE, quantity=float(NEW_BALANCE), price=str(PRİCE))
                                    except:
                                        break
                                    break
                            while True:
                                try:
                                    if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)) < 0.0001:
                                        break
                                    else:
                                        time.sleep(1)
                                        print("Try Again Sell Control Algorithm !")
                                        ControlAlgorithm_I()
                                except:
                                    print("Tekrardan Bağlantı Sağlanılıyor.")

                            MAX_ZARAR_DEG = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])
                            MAX_PRİCE_I = (float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice']) * 100.7) / 100
                            time.sleep(1)
                            while True:
                                try:
                                    print("Control Algorithm I")
                                    time.sleep(1)
                                    if float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice']) > MAX_PRİCE_I:
                                        self.CANCEL_CONTROL -= 1
                                        self.CANCEL_CONTROL -= self.CANCEL_CONTROL
                                        break
                                    elif (MAX_ZARAR_DEG * 99) / 100 > float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice']):
                                        def MAX_ZARAR():
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
                                                if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)) < 0.0001:
                                                    self.CANCEL_CONTROL -= 1
                                                    self.CANCEL_CONTROL -= self.CANCEL_CONTROL
                                                    break
                                                else:
                                                    time.sleep(1)
                                                    MAX_ZARAR()
                                                    print("Control Algorithm I")
                                                    print("Max Low Price !")
                                            except:
                                                print("Tekrardan Bağlantı Sağlanılıyor.")
                                except:
                                    print("Tekrardan Bağlantı Sağlanılıyor.")
                        elif (float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice']) * 99) / 100 > float(self.Opportunity_TETİKLE):
                            time.sleep(2)
                            print("Control Algorithm II")
                            def ControlAlgorithm_II():
                                while True:
                                    try:
                                        BALANCE = Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)
                                        NEW_BALANCE = float(BALANCE)
                                        ANLIK = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])
                                        PRİCE = float(ANLIK) + (float(ANLIK * 100.5) / 100)
                                        Intelence.ROB_SELL_LİMİT(symbol=self.SORUMLU_COİN_ONE, quantity=float(NEW_BALANCE), price=str(PRİCE))
                                    except:
                                        break
                                    break
                            while True:
                                try:
                                    if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)) < 0.0001:
                                        break
                                    else:
                                        time.sleep(1)
                                        print("Try Again Sell Control Algorithm !")
                                        ControlAlgorithm_II()
                                except:
                                    print("Tekrardan Bağlantı Sağlanılıyor.")
                            MAX_ZARAR_DEG_II = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])
                            MAX_PRİCE_II = (float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice']) * 100.5) / 100
                            time.sleep(1)
                            while True:
                                try:
                                    print("Control Algorithm II")
                                    time.sleep(1)
                                    if float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice']) > MAX_PRİCE_II:
                                        self.CANCEL_CONTROL -= 1
                                        self.CANCEL_CONTROL -= self.CANCEL_CONTROL
                                        break
                                    elif (MAX_ZARAR_DEG_II * 99) / 100 > float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice']):
                                        def MAX_ZARAR():
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
                                                if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)) < 0.0001:
                                                    self.CANCEL_CONTROL -= 1
                                                    self.CANCEL_CONTROL -= self.CANCEL_CONTROL
                                                    break
                                                else:
                                                    time.sleep(1)
                                                    MAX_ZARAR()
                                                    print("Control Algorithm I")
                                                    print("Max Low Price !")
                                            except:
                                                pass
                                except:
                                    print("Tekrardan Bağlantı Sağlanılıyor.")
                        elif (float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice']) * 99.5) / 100 > float(self.Opportunity_TETİKLE):
                            time.sleep(2)
                            print("Control Algorithm III")
                            def ControlAlgorithm_III(Price = self.Opportunity_TETİKLE):
                                while True:
                                    try:
                                        BALANCE = Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)
                                        NEW_BALANCE = float(BALANCE)
                                        ANLIK = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])
                                        PRİCE = Price
                                        EMİR_SELL_START = Intelence.ROB_SELL_LİMİT(symbol=self.SORUMLU_COİN_ONE, quantity=float(NEW_BALANCE), price=str(PRİCE))
                                    except:
                                        break
                                    break
                            while True:
                                try:
                                    if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)) < 0.0001:
                                        print("Try Again Sell Control Algorithm !")
                                        break
                                    else:
                                        time.sleep(1)
                                        ControlAlgorithm_III()
                                except:
                                    pass

                            MAX_ZARAR_DEG_III = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])
                            MAX_PRİCE_III = self.Opportunity_TETİKLE
                            time.sleep(1)
                            while True:
                                try:
                                    print("Control Algorithm III")
                                    time.sleep(1)
                                    if float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice']) > MAX_PRİCE_III:
                                        self.CANCEL_CONTROL -= 1
                                        self.CANCEL_CONTROL -= self.CANCEL_CONTROL
                                        break
                                    elif (MAX_ZARAR_DEG_III * 98.5) / 100 > float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice']):
                                        def MAX_ZARAR():
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
                                                if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)) < 0.0001:
                                                    self.CANCEL_CONTROL -= 1
                                                    self.CANCEL_CONTROL -= self.CANCEL_CONTROL
                                                    break
                                                else:
                                                    time.sleep(1)
                                                    MAX_ZARAR()
                                                    print("Control Algorithm I")
                                                    print("Max Low Price !")
                                            except:
                                                print("Tekrardan Bağlantı Sağlanılıyor.")
                                except:
                                    print("Tekrardan Bağlantı Sağlanılıyor.")
                        else:
                            self.CANCEL_CONTROL -= 1
                            print("SELL ControlAlgorithm STOP !")
                    elif float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol='BUSD')) > 10:
                        time.sleep(2)

                        if (self.Opportunity_TETİKLE * 101.5) / 100 < (float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])):
                            time.sleep(2)
                            print("Control Algorithm I")
                            def ControlAlgorithm_I():
                                while True:
                                    try:
                                        BALANCE = float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol='BUSD'))
                                        ANLIK = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])
                                        Quantity = math.floor(float(BALANCE)) / float(ANLIK)
                                        STEP = get_round_step_quantity(qty=Quantity)
                                        PRİCE = float(ANLIK * 99.3) / 100
                                        START_BUY = Intelence.ROB_BUY_LİMİT(symbol=self.SORUMLU_COİN_ONE, quantity=float(STEP), price=str(PRİCE))
                                    except:
                                        break
                                    break
                            while True:
                                try:
                                    if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol='BUSD')) < 10:
                                        self.CANCEL_CONTROL -= 1
                                        break
                                    else:
                                        time.sleep(1)
                                        print("Try Again Buy Control Algorithm !")
                                        ControlAlgorithm_I()
                                except:
                                    print("Tekrardan Bağlantı Sağlanılıyor.")
                        elif (self.Opportunity_TETİKLE * 101) / 100 < (float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])):
                            time.sleep(2)
                            print("Control Algorithm II")
                            def ControlAlgorithm_II():
                                while True:
                                    try:
                                        BALANCE = float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol='BUSD'))
                                        ANLIK = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])
                                        Quantity = math.floor(float(BALANCE)) / float(ANLIK)
                                        STEP = get_round_step_quantity(qty=Quantity)
                                        PRİCE = float(ANLIK * 99.5) / 100
                                        START_BUY = Intelence.ROB_BUY_LİMİT(symbol=self.SORUMLU_COİN_ONE, quantity=float(STEP), price=str(PRİCE))
                                    except:
                                        break
                                    break
                            while True:
                                try:
                                    if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol='BUSD')) < 10:
                                        self.CANCEL_CONTROL -= 1
                                        break
                                    else:
                                        time.sleep(1)
                                        print("Try Again Buy Control Algorithm !")
                                        ControlAlgorithm_II()
                                except:
                                    print("Tekrardan Bağlantı Sağlanılıyor.")
                        elif (self.Opportunity_TETİKLE * 100.5) / 100 < (float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])):
                            time.sleep(2)
                            print("Control Algorithm II")
                            def ControlAlgorithm_III(Price = self.Opportunity_TETİKLE):
                                while True:
                                    try:
                                        BALANCE = float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol='BUSD'))
                                        ANLIK = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])
                                        Quantity = math.floor(float(BALANCE)) / float(ANLIK)
                                        STEP = get_round_step_quantity(qty=Quantity)
                                        PRİCE = Price
                                        START_BUY = Intelence.ROB_BUY_LİMİT(symbol=self.SORUMLU_COİN_ONE, quantity=float(STEP), price=str(PRİCE))
                                    except:
                                        break
                                    break
                            while True:
                                try:
                                    if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol='BUSD')) < 10:
                                        self.CANCEL_CONTROL -= 1
                                        break
                                    else:
                                        time.sleep(1)
                                        print("Try Again Buy Control Algorithm !")
                                        ControlAlgorithm_III()
                                except:
                                    print("Tekrardan Bağlantı Sağlanılıyor.")
                        else:
                            self.CANCEL_CONTROL -= 1
                            print("BUY ControlAlgorithm STOP !")
                elif WavyAlgorithm == True and self.WAVY_STOP == True and BUSD > 10 and (self.BUY_Opportunity == 2 or self.SELL_Opportunity == 2):
                    print("Special WavyAlgorithm Activate !")
                    BUY_ORDER_PRİCE = 0
                    # ------------------------
                    BALANCE = float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol='BUSD'))
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
                            BUY_WAVY_CRYPTO_GENERATOR = float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol='BUSD')) / float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])
                            ANLIK = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])
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
                            print("Center Price : ",BUY_ORDER_PRİCE)

                    # ORDERS CENTER
                    CONTROLLER_FEE = 0
                    Wavy_STOP = False
                    Wavy_Default = False
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
                    class Wavy:
                        def WavyAlgorithm_I_BUY(Balance=BALANCE_ONE):
                            nonlocal BUY_ORDER_ONE, BUY_ONE_CONTROL, SELL_ONE_CONTROL
                            while True:
                                try:
                                    ANLIK = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])
                                    Quantity = math.floor(float(Balance)) / float(ANLIK)
                                    STEP = get_round_step_quantity(qty=Quantity)
                                    PRİCE = int(BUY_ORDER_ONE)
                                    Intelence.ROB_BUY_LİMİT(symbol=self.SORUMLU_COİN_ONE, quantity=float(STEP), price=str(PRİCE))

                                    BUY_ONE_CONTROL += True
                                    SELL_ONE_CONTROL += True
                                    print("Wavy Buy I ON")
                                    time.sleep(1)
                                except:
                                    break
                                break
                        def WavyAlgorithm_II_BUY(Balance=BALANCE_TWO):
                            nonlocal BUY_ORDER_TWO, BUY_TWO_CONTROL, SELL_TWO_CONTROL
                            while True:
                                try:
                                    ANLIK = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])
                                    Quantity = math.floor(float(Balance)) / float(ANLIK)
                                    STEP = get_round_step_quantity(qty=Quantity)
                                    PRİCE = int(BUY_ORDER_TWO)
                                    Intelence.ROB_BUY_LİMİT(symbol=self.SORUMLU_COİN_ONE, quantity=float(STEP), price=str(PRİCE))

                                    BUY_TWO_CONTROL += True
                                    SELL_TWO_CONTROL += True
                                    print("Wavy Buy II ON")
                                    time.sleep(1)
                                except:
                                    break
                                break
                        def WavyAlgorithm_III_BUY(Balance=BALANCE_THREE):
                            nonlocal BUY_ORDER_THREE, BUY_THREE_CONTROL, SELL_THREE_CONTROL
                            while True:
                                try:
                                    ANLIK = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])
                                    Quantity = math.floor(float(Balance)) / float(ANLIK)
                                    STEP = get_round_step_quantity(qty=Quantity)
                                    PRİCE = int(BUY_ORDER_THREE)
                                    Intelence.ROB_BUY_LİMİT(symbol=self.SORUMLU_COİN_ONE, quantity=float(STEP), price=str(PRİCE))

                                    BUY_THREE_CONTROL += True
                                    SELL_THREE_CONTROL += True
                                    print("Wavy Buy III ON")
                                    time.sleep(1)
                                except:
                                    break
                                break
                        def WavyAlgorithm_IV_BUY(Balance=BALANCE_FOUR):
                            nonlocal BUY_ORDER_FOUR, BUY_FOUR_CONTROL, SELL_FOUR_CONTROL
                            while True:
                                try:
                                    ANLIK = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])
                                    Quantity = math.floor(float(Balance)) / float(ANLIK)
                                    STEP = get_round_step_quantity(qty=Quantity)
                                    PRİCE = int(BUY_ORDER_FOUR)
                                    Intelence.ROB_BUY_LİMİT(symbol=self.SORUMLU_COİN_ONE, quantity=float(STEP), price=str(PRİCE))

                                    BUY_FOUR_CONTROL += True
                                    SELL_FOUR_CONTROL += True
                                    print("Wavy Buy IV ON")
                                    time.sleep(1)
                                except:
                                    break
                                break

                        def WavyAlgorithm_I_SELL(Price=SELL_ORDER_ONE):
                            nonlocal BUY_ONE_CONTROL, SELL_ONE_CONTROL, Wavy_Default
                            while True:
                                try:
                                    BALANCE = Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)
                                    NEW_BALANCE = float(BALANCE)
                                    PRİCE = int(Price)
                                    Intelence.ROB_SELL_LİMİT(symbol=self.SORUMLU_COİN_ONE, quantity=float(NEW_BALANCE), price=str(PRİCE))

                                    BUY_ONE_CONTROL += False
                                    SELL_ONE_CONTROL += False
                                    Wavy_Default += True
                                    print("Wavy Sell I ON")
                                except:
                                    break
                                break
                        def WavyAlgorithm_II_SELL(Price=SELL_ORDER_TWO):
                            nonlocal BUY_TWO_CONTROL, SELL_TWO_CONTROL, Wavy_Default
                            while True:
                                try:
                                    BALANCE = Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)
                                    NEW_BALANCE = float(BALANCE)
                                    PRİCE = int(Price)
                                    Intelence.ROB_SELL_LİMİT(symbol=self.SORUMLU_COİN_ONE, quantity=float(NEW_BALANCE), price=str(PRİCE))

                                    BUY_TWO_CONTROL += False
                                    SELL_TWO_CONTROL += False
                                    Wavy_Default += True
                                    print("Wavy Sell II ON")
                                except:
                                    break
                                break
                        def WavyAlgorithm_III_SELL(Price=SELL_ORDER_THREE):
                            nonlocal BUY_THREE_CONTROL, SELL_THREE_CONTROL, Wavy_Default
                            while True:
                                try:
                                    BALANCE = Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)
                                    NEW_BALANCE = float(BALANCE)
                                    PRİCE = int(Price)
                                    Intelence.ROB_SELL_LİMİT(symbol=self.SORUMLU_COİN_ONE, quantity=float(NEW_BALANCE), price=str(PRİCE))

                                    BUY_THREE_CONTROL += False
                                    SELL_THREE_CONTROL += False
                                    Wavy_Default += True
                                    print("Wavy Sell III ON")
                                except:
                                    break
                                break
                        def WavyAlgorithm_IV_SELL(Price=SELL_ORDER_FOUR):
                            nonlocal BUY_FOUR_CONTROL, SELL_FOUR_CONTROL, Wavy_Default
                            while True:
                                try:
                                    BALANCE = Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)
                                    NEW_BALANCE = float(BALANCE)
                                    PRİCE = int(Price)
                                    Intelence.ROB_SELL_LİMİT(symbol=self.SORUMLU_COİN_ONE, quantity=float(NEW_BALANCE), price=str(PRİCE))

                                    BUY_FOUR_CONTROL += False
                                    SELL_FOUR_CONTROL += False
                                    Wavy_Default += True
                                    print("Wavy Sell IV ON")
                                except:
                                    break
                                break

                    class Wavy_Default:
                        def Wavy_NORMAL_BUYİNG():
                            while True:
                                try:
                                    ANLIK = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])
                                    Quantity = math.floor(float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol='BUSD'))) / float(ANLIK)
                                    STEP = get_round_step_quantity(qty=Quantity)
                                    PRİCE = float(ANLIK * 99.75) / 100
                                    Intelence.ROB_BUY_LİMİT(symbol=self.SORUMLU_COİN_ONE, quantity=float(STEP), price=str(PRİCE))
                                except:
                                    break
                                break
                        def Wavy_NORMAL_SELLİNG():
                            while True:
                                try:
                                    BALANCE = Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)
                                    NEW_BALANCE = float(BALANCE)
                                    ANLIK = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])
                                    PRİCE = float(ANLIK * 100.15) / 100
                                    Intelence.ROB_SELL_LİMİT(symbol=self.SORUMLU_COİN_ONE, quantity=float(NEW_BALANCE), price=str(PRİCE))  # SAT LİMİT EMRİ # HEDEFE GÖRE AYARLANACAK
                                except:
                                    break
                                break


                    while True:
                        Loss_SECOND = 0

                        if Wavy_STOP == True:
                            break

                        if CONTROLLER_FEE == 5:
                            ONE_CANCEL = 0
                            TWO_CANCEL = 0
                            THREE_CANCEL = 0
                            FOUR_CANCEL = 0
                            for i in range(4):
                                try:
                                    if i == 1:
                                        orders = ROB.get_open_orders(symbol=self.SORUMLU_COİN_ONE)
                                        orders_ID = orders[i]['orderId']
                                        ONE_CANCEL += int(orders_ID)
                                        sleep(0.6)
                                    if i == 2:
                                        orders = ROB.get_open_orders(symbol=self.SORUMLU_COİN_ONE)
                                        orders_ID = orders[i]['orderId']
                                        TWO_CANCEL += int(orders_ID)
                                        sleep(0.6)
                                    if i == 3:
                                        orders = ROB.get_open_orders(symbol=self.SORUMLU_COİN_ONE)
                                        orders_ID = orders[i]['orderId']
                                        THREE_CANCEL += int(orders_ID)
                                        sleep(0.6)
                                    if i == 4:
                                        orders = ROB.get_open_orders(symbol=self.SORUMLU_COİN_ONE)
                                        orders_ID = orders[i]['orderId']
                                        FOUR_CANCEL += int(orders_ID)
                                except:
                                    pass
                            for i in range(4):
                                try:
                                    if ONE_CANCEL != 0:
                                        Intelence.ROB_CANCEL(symbol=self.SORUMLU_COİN_ONE, orderID=ONE_CANCEL)
                                        ONE_CANCEL -= ONE_CANCEL
                                        time.sleep(1)

                                    if TWO_CANCEL != 0:
                                        Intelence.ROB_CANCEL(symbol=self.SORUMLU_COİN_ONE, orderID=TWO_CANCEL)
                                        TWO_CANCEL -= TWO_CANCEL
                                        time.sleep(1)

                                    if THREE_CANCEL != 0:
                                        Intelence.ROB_CANCEL(symbol=self.SORUMLU_COİN_ONE, orderID=THREE_CANCEL)
                                        THREE_CANCEL -= THREE_CANCEL
                                        time.sleep(1)

                                    if FOUR_CANCEL != 0:
                                        Intelence.ROB_CANCEL(symbol=self.SORUMLU_COİN_ONE, orderID=FOUR_CANCEL)
                                        FOUR_CANCEL -= FOUR_CANCEL
                                        time.sleep(1)
                                except:
                                    print("Try Again Cancel Order !")

                            def Wavy_STOP_FUNCTİON():
                                while True:
                                    try:
                                        BALANCE = Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)
                                        NEW_BALANCE = float(BALANCE)
                                        ANLIK = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])
                                        PRİCE = float(ANLIK * 100.1) / 100
                                        Intelence.ROB_SELL_LİMİT(symbol=self.SORUMLU_COİN_ONE, quantity=float(NEW_BALANCE), price=str(PRİCE))
                                    except:
                                        break
                                    break


                            while True:
                                try:
                                    if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)) < 0.0001:
                                        break
                                    else:
                                        time.sleep(1)
                                        Wavy_STOP_FUNCTİON()
                                except:
                                    print("Tekrardan Bağlantı Sağlanılıyor.")


                            STOP_PRİCE = (float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice']) * 100.1) / 100
                            while True:
                                time.sleep(2)
                                if float(STOP_PRİCE * 98.4) / 100 > float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice']):
                                    def Wivy_MARKET():
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
                                            if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)) < 0.0001:
                                                break
                                            else:
                                                time.sleep(1)
                                                Wivy_MARKET()
                                                sys.exit()
                                        except:
                                            print("Tekrardan Bağlantı Sağlanılıyor.")


                                elif STOP_PRİCE < float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice']):
                                    Return_Fee()
                                    Wavy_STOP += True
                                    break


                        while True:
                            time.sleep(1)
                            Loss_SECOND += 1

                            if Loss_SECOND == 2:
                                break

                            try:
                                if Wavy_Default == False:

                                    if BUY_ONE_CONTROL != True:
                                        Wavy.WavyAlgorithm_I_BUY()
                                        print("Wavy Buy Try Again I")
                                        break

                                    elif float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)) > 0.0001:
                                        Wavy.WavyAlgorithm_I_SELL()
                                        print("Wavy Sell Try Again I")
                                        CONTROLLER_FEE += 1
                                        break

                                elif Wavy_Default == True:

                                    if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol="BUSD")) > 10:
                                        Wavy_Default.Wavy_NORMAL_BUYİNG()
                                        print("Wavy_DEF Buy Try Again I")
                                        break

                                    elif float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)) > 0.0001:
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
                                print("Toplam İşlem Ücretiniz : ", self.Fee,end="$\n")
                                print("--------------------------------------")
                        while True:
                            time.sleep(1)
                            Loss_SECOND += 1
                            if Loss_SECOND == 4:
                                break

                            try:
                                if Wavy_Default == False:

                                    if BUY_TWO_CONTROL != True:
                                        Wavy.WavyAlgorithm_II_BUY()
                                        print("Wavy Buy Try Again II")
                                        break

                                    elif float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)) > 0.0001:
                                        Wavy.WavyAlgorithm_II_SELL()
                                        print("Wavy Sell Try Again II")
                                        CONTROLLER_FEE += 1
                                        break

                                elif Wavy_Default == True:

                                    if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol="BUSD")) > 10:
                                        Wavy_Default.Wavy_NORMAL_BUYİNG()
                                        print("Wavy_DEF Buy Try Again II")
                                        break

                                    elif float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)) > 0.0001:
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
                                print("Toplam İşlem Ücretiniz : ", self.Fee,end="$\n")
                                print("--------------------------------------")
                        while True:
                            time.sleep(1)
                            Loss_SECOND += 1
                            if Loss_SECOND == 6:
                                break

                            try:
                                if Wavy_Default == False:

                                    if BUY_THREE_CONTROL != True:
                                        Wavy.WavyAlgorithm_III_BUY()
                                        print("Wavy Buy Try Again III")
                                        break

                                    elif float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)) > 0.0001:
                                        Wavy.WavyAlgorithm_III_SELL()
                                        print("Wavy Sell Try Again III")
                                        CONTROLLER_FEE += 1
                                        break

                                elif Wavy_Default == True:

                                    if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol="BUSD")) > 10:
                                        Wavy_Default.Wavy_NORMAL_BUYİNG()
                                        print("Wavy_DEF Buy Try Again III")
                                        break

                                    elif float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)) > 0.0001:
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
                                print("Toplam İşlem Ücretiniz : ", self.Fee,end="$\n")
                                print("--------------------------------------")
                        while True:
                            time.sleep(1)
                            Loss_SECOND += 1
                            if Loss_SECOND == 8:
                                break
                                
                            try:
                                if Wavy_Default == False:

                                    if BUY_ONE_CONTROL != True:
                                        Wavy.WavyAlgorithm_IV_BUY()
                                        print("Wavy Buy Try Again IV")
                                        break

                                    elif float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)) > 0.0001:
                                        Wavy.WavyAlgorithm_IV_SELL()
                                        print("Wavy Sell Try Again IV")
                                        CONTROLLER_FEE += 1
                                        break

                                elif Wavy_Default == True:

                                    if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol="BUSD")) > 10:
                                        Wavy_Default.Wavy_NORMAL_BUYİNG()
                                        print("Wavy_DEF Buy Try Again IV")
                                        break


                                    elif float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)) > 0.0001:
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
                                print("Toplam İşlem Ücretiniz : ", self.Fee,end="$\n")
                                print("--------------------------------------")
                elif BUY_OpportunityAlgorithm == True and self.BUY_Opportunity == 3 and float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol='BUSD')) > 10:
                    time.sleep(1)
                    while True:
                        try:
                            print("Buy OpportunityAlgorithm Activate !")
                            BUY_OpportunityAlgorithm_PRİCE = 0
                            BUY_OpportunityAlgorithm_CRYPTO_GENERATOR = float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol='BUSD')) / float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])
                            ANLIK = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])

                            #---------------------------------------------------------------
                            if BUY_OpportunityAlgorithm_CRYPTO_GENERATOR * ((ANLIK * 100.1) / 100) >= self.HEDEF:
                                BUY_OpportunityAlgorithm_PRİCE += (ANLIK * 99.8) / 100
                            elif BUY_OpportunityAlgorithm_CRYPTO_GENERATOR * ((ANLIK * 100.2) / 100) >= self.HEDEF:
                                BUY_OpportunityAlgorithm_PRİCE += (ANLIK * 99.7) / 100
                            #---------------------------------------------------------------
                            elif BUY_OpportunityAlgorithm_CRYPTO_GENERATOR * ((ANLIK * 100.3) / 100) >= self.HEDEF:
                                BUY_OpportunityAlgorithm_PRİCE += (ANLIK * 99.6) / 100
                            elif BUY_OpportunityAlgorithm_CRYPTO_GENERATOR * ((ANLIK * 100.4) / 100) >= self.HEDEF:
                                BUY_OpportunityAlgorithm_PRİCE += (ANLIK * 99.5) / 100
                            #---------------------------------------------------------------
                            elif BUY_OpportunityAlgorithm_CRYPTO_GENERATOR * ((ANLIK * 100.5) / 100) >= self.HEDEF:
                                BUY_OpportunityAlgorithm_PRİCE += (ANLIK * 99.4) / 100
                            elif BUY_OpportunityAlgorithm_CRYPTO_GENERATOR * ((ANLIK * 100.6) / 100) >= self.HEDEF:
                                BUY_OpportunityAlgorithm_PRİCE += (ANLIK * 99.3) / 100
                            #---------------------------------------------------------------
                            elif BUY_OpportunityAlgorithm_CRYPTO_GENERATOR * ((ANLIK * 100.7) / 100) >= self.HEDEF:
                                BUY_OpportunityAlgorithm_PRİCE += (ANLIK * 99.2) / 100
                            elif BUY_OpportunityAlgorithm_CRYPTO_GENERATOR * ((ANLIK * 100.8) / 100) >= self.HEDEF:
                                BUY_OpportunityAlgorithm_PRİCE += (ANLIK * 99.1) / 100
                            #-------------------------------------------------------------
                            elif BUY_OpportunityAlgorithm_CRYPTO_GENERATOR * ((ANLIK * 100.9) / 100) >= self.HEDEF:
                                BUY_OpportunityAlgorithm_PRİCE += (ANLIK * 99.0) / 100
                            elif BUY_OpportunityAlgorithm_CRYPTO_GENERATOR * ((ANLIK * 101.0) / 100) >= self.HEDEF:
                                BUY_OpportunityAlgorithm_PRİCE += (ANLIK * 98.9) / 100
                            #-------------------------------------------------------------
                            print("Buy Opportunity Price : ",BUY_OpportunityAlgorithm_PRİCE)
                            print("Generator : ",BUY_OpportunityAlgorithm_CRYPTO_GENERATOR)
                            if BUY_OpportunityAlgorithm_PRİCE != 0:
                                def OpportunityAlgorithm(Price = BUY_OpportunityAlgorithm_PRİCE):
                                    while True:
                                        try:
                                            ANLIK = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])
                                            BUSD = float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol='BUSD'))
                                            Quantity = math.floor((float(BUSD))) / float(ANLIK)
                                            STEP = get_round_step_quantity(qty=Quantity)
                                            Intelence.ROB_BUY_LİMİT(symbol=self.SORUMLU_COİN_ONE, quantity=float(STEP), price=int(Price))
                                        except:
                                            break
                                        break
                                while True:
                                    try:
                                        if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol='BUSD')) < 10:
                                            self.BUY_Opportunity -= 3
                                            break
                                        else:
                                            time.sleep(1)
                                            OpportunityAlgorithm()
                                            print("Try Again Buy OpportunityAlgorithm")
                                    except:
                                        print("Tekrardan Bağlantı Sağlanıyor.")
                            else:
                                self.BUY_Opportunity -= 3
                            break
                        except:
                            print("BUY_OpportunityAlgorithm Error ! ")
                elif SELL_OpportunityAlgorithm == True and self.SELL_Opportunity == 3 and float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)) > 0.0001:
                    try:
                        print("Sell OpportunityAlgorithm Activate !")
                        time.sleep(1)
                        SELL_ORDER_PRİCE = 0
                        BALANCE = float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE))
                        ANLIK = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])
                        #-------------------------------------------------
                        if ((ANLIK * 100.1) / 100) * BALANCE >= self.HEDEF:
                            SELL_ORDER_PRİCE += (ANLIK * 100.1) / 100
                        elif ((ANLIK * 100.2) / 100) * BALANCE >= self.HEDEF:
                            SELL_ORDER_PRİCE += (ANLIK * 100.2) / 100
                        #-------------------------------------------------
                        elif ((ANLIK * 100.3) / 100) * BALANCE >= self.HEDEF:
                            SELL_ORDER_PRİCE += (ANLIK * 100.3) / 100
                        elif ((ANLIK * 100.4) / 100) * BALANCE >= self.HEDEF:
                            SELL_ORDER_PRİCE += (ANLIK * 100.4) / 100
                        #-------------------------------------------------
                        elif ((ANLIK * 100.5) / 100) * BALANCE >= self.HEDEF:
                            SELL_ORDER_PRİCE += (ANLIK * 100.5) / 100
                        elif ((ANLIK * 100.6) / 100) * BALANCE >= self.HEDEF:
                            SELL_ORDER_PRİCE += (ANLIK * 100.6) / 100
                        # -------------------------------------------------
                        elif ((ANLIK * 100.7) / 100) * BALANCE >= self.HEDEF:
                            SELL_ORDER_PRİCE += (ANLIK * 100.7) / 100
                        elif ((ANLIK * 100.8) / 100) * BALANCE >= self.HEDEF:
                            SELL_ORDER_PRİCE += (ANLIK * 100.8) / 100
                        #-------------------------------------------------
                        elif ((ANLIK * 100.9) / 100) * BALANCE >= self.HEDEF:
                            SELL_ORDER_PRİCE += (ANLIK * 100.9) / 100
                        elif ((ANLIK * 101.0) / 100) * BALANCE >= self.HEDEF:
                            SELL_ORDER_PRİCE += (ANLIK * 101.0) / 100
                        #-------------------------------------------------
                        print("Sell Opportunity Price : ", SELL_ORDER_PRİCE)
                        if SELL_ORDER_PRİCE != 0:
                            def OpportunityAlgorithm(Price= SELL_ORDER_PRİCE):
                                while True:
                                    try:
                                        BALANCE = Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)
                                        NEW_BALANCE = float(BALANCE)
                                        PRİCE = int(Price)
                                        EMİR_SELL_START = Intelence.ROB_SELL_LİMİT(symbol=self.SORUMLU_COİN_ONE, quantity=float(NEW_BALANCE), price=int(Price))  # SAT LİMİT EMRİ # HEDEFE GÖRE AYARLANACAK
                                    except:
                                        break
                                    break
                            while True:
                                try:
                                    if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)) < 0.0001:
                                        break
                                    else:
                                        time.sleep(1)
                                        OpportunityAlgorithm()
                                        print("Try Again Sell OpportunityAlgorithm !")
                                except:
                                    print("Tekrardan Bağlantı Sağlanıyor.")

                            Opportunity_PRİCE = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])
                            while True:
                                time.sleep(2)
                                if float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice']) < (Opportunity_PRİCE * 98) / 100:
                                    def OpportunityAlgorithm_MARKET():
                                        while True:
                                            try:
                                                BALANCE = Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)
                                                NEW_BALANCE = float(BALANCE)
                                                Intelence.ROB_SELL_MARKET(symbol=self.SORUMLU_COİN_ONE, quantity=float(NEW_BALANCE))
                                            except:
                                                break
                                            break

                                    while True:
                                        try:
                                            if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)) < 0.0001:
                                                print("Maksimum Zarar Algılandı !")
                                                sys.exit()
                                            else:
                                                time.sleep(1)
                                                OpportunityAlgorithm_MARKET()
                                                print("Try Again Sell OpportunityAlgorithm !")
                                        except:
                                            print("Tekrardan Bağlantı Sağlanıyor.")

                                elif float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice']) > SELL_ORDER_PRİCE:
                                    try:
                                        print("Sell OpportunityAlgorithm Successful !")
                                        self.SELL_Opportunity -= 3
                                        Return_Fee()
                                        break
                                    except:
                                        print("Tekrardan Bağlantı Sağlanıyor.")
                        else:
                            self.SELL_Opportunity -= 3
                    except:
                        print("SELL_OpportunityAlgorithm Error")
                elif BUSD >= 10:
                    SORUMLU_COİN_BALANCE = self.SORUMLU_COİN_ONE.replace('BUSD', '')
                    AL_MultiChain_ONE = list()
                    TİME_ZONE = list()
                    STOP_BUSD = False
                    BUY_ZARAR_KURTARMA = False
                    CANCEL_SAYAC = 0

                    while True:
                        try:
                            if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol='BUSD')) <= 10:
                                break
                            else:
                                time.sleep(1)
                                Multi_Chain_BUY_START()
                                print("Try Again Buy Order...")
                        except:
                            print("Tekrardan Bağlantı Sağlanıyor.")


                    orders = ROB.get_open_orders(symbol=self.SORUMLU_COİN_ONE)
                    orders_ID = orders[0]['orderId']
                    START_BUY_ORDER_ID = str(orders_ID)


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
                            SORUMLU_COİN_ONE = self.SORUMLU_COİN_ONE
                            SORUMLU_COİN_BALANCE = self.SORUMLU_COİN_ONE.replace('BUSD', '')
                            SORUMLU_COİN_ONE_AL = self.SORUMLU_COİN_ONE_AL
                            SORUMLU_COİN_ONE_SAT = self.SORUMLU_COİN_ONE_SAT
                            STOP_FUNCTİON_BUY_PRİCE = round(float(SORUMLU_COİN_ONE_AL),1)
                            STOP_FUNCTİON_SELL_PRİCE = round(float(SORUMLU_COİN_ONE_SAT * 50) / 100,1)
                            STOP_FUNCTİON_SELL_ANLIK = 0

                            try:
                                orders_HİGHT = ROB.get_open_orders(symbol=self.SORUMLU_COİN_ONE)
                                orders_ID_HİGHT = orders_HİGHT[0]['orderId']
                                Intelence.ROB_CANCEL(symbol=self.SORUMLU_COİN_ONE, orderID=str(orders_ID_HİGHT))
                            except:
                                print("Tekrardan Bağlantı Sağlanıyor.")

                            time.sleep(1)
                            def STOP_FUNCTİON_BUY(Price=STOP_FUNCTİON_BUY_PRİCE):
                                while True:
                                    try:
                                        BUSD = float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol='BUSD'))
                                        ANLIK = float(ROB.get_ticker(symbol=SORUMLU_COİN_ONE)['lastPrice'])
                                        Quantity = math.floor(float(BUSD)) / float(ANLIK)
                                        STEP = get_round_step_quantity(qty=Quantity)
                                        PRİCE = float(ANLIK) - Price
                                        EMİR_BUY_ONE = Intelence.ROB_BUY_LİMİT(symbol=SORUMLU_COİN_ONE, quantity=float(STEP), price=str(PRİCE))
                                    except:
                                        break
                                    break
                            def STOP_FUNCTİON_SELL(Price=STOP_FUNCTİON_SELL_PRİCE):
                                while True:
                                    try:
                                        BALANCE = Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)
                                        NEW_BALANCE = float(BALANCE)
                                        ANLIK = float(ROB.get_ticker(symbol=SORUMLU_COİN_ONE)['lastPrice'])
                                        PRİCE = float(ANLIK) + float(Price)
                                        EMİR_SELL_START = Intelence.ROB_SELL_LİMİT(symbol=SORUMLU_COİN_ONE, quantity=float(NEW_BALANCE), price=str(PRİCE))  # SAT LİMİT EMRİ # HEDEFE GÖRE AYARLANACAK
                                    except:
                                        break
                                    break
                            def SECURTY_SELL():
                                def Securty_MARKET():
                                    while True:
                                        try:
                                            Sensor_CRYPTO_BALANCE = Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)
                                            Sensor_CRYPTO_PRİCE = float(Sensor_CRYPTO_BALANCE)
                                            Intelence.ROB_SELL_MARKET(symbol=SORUMLU_COİN_ONE, quantity=Sensor_CRYPTO_PRİCE)
                                        except:
                                            break
                                        break
                                try:
                                    Sensor_STOP_Orders = ROB.get_open_orders(symbol=SORUMLU_COİN_ONE)
                                    Sensor_STOP_Orders_ID = Sensor_STOP_Orders[0]['orderId']
                                    Intelence.ROB_CANCEL(symbol=SORUMLU_COİN_ONE, orderID=str(Sensor_STOP_Orders_ID))
                                except:
                                    print("Tekrardan Bağlantı Sağlanıyor.")

                                while True:
                                    try:
                                        if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)) <= 0.0001:
                                            break
                                        else:
                                            time.sleep(1)
                                            Securty_MARKET()
                                            print("Try Again Securty MARKET Order...")
                                    except:
                                        print("Tekrardan Bağlantı Sağlanıyor.")

                            while True:
                                try:
                                    if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol='BUSD')) <= 10:
                                        break
                                    else:
                                        time.sleep(1)
                                        STOP_FUNCTİON_BUY()
                                        print("Hight Price BUY Order...")
                                except:
                                    print("Tekrardan Bağlantı Sağlanıyor.")
                            while True:
                                try:
                                    if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)) <= 0.0001:
                                        break
                                    else:
                                        time.sleep(1)
                                        STOP_FUNCTİON_SELL()
                                        print("Hight Price SELL Order...")
                                except:
                                    print("Tekrardan Bağlantı Sağlanıyor.")

                            STOP_FUNCTİON_SELL_ANLIK += float(ROB.get_ticker(symbol=SORUMLU_COİN_ONE)['lastPrice'])
                            while True:
                                try:
                                    time.sleep(2)
                                    if float(STOP_FUNCTİON_SELL_ANLIK * 98.5) / 100 > float(ROB.get_ticker(symbol=SORUMLU_COİN_ONE)['lastPrice']):
                                        try:
                                            orders = ROB.get_open_orders(symbol=SORUMLU_COİN_ONE)
                                            orders_ID = orders_nine[0]['orderId']
                                            Intelence.ROB_CANCEL(symbol=SORUMLU_COİN_ONE,orderID=str(orders_ID))
                                        except:
                                            print("Tekrardan Bağlantı Sağlanıyor.")

                                        while True:
                                            try:
                                                if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)) <= 0.0001:
                                                    print("Maksimum Zarar Algılandı !")
                                                    sys.exit()
                                                    break
                                                else:
                                                    time.sleep(1)
                                                    SECURTY_SELL()
                                            except:
                                                print("Tekrardan Bağlantı Sağlanıyor.")
                                    elif float(STOP_FUNCTİON_SELL_ANLIK + STOP_FUNCTİON_SELL_PRİCE) < float(ROB.get_ticker(symbol=SORUMLU_COİN_ONE)['lastPrice']):
                                        break
                                except:
                                    print("Tekrardan Bağlantı Sağlanıyor.")
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
                                    if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)) < 0.0001:
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
                                                if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)) <= 0.0001:
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

                                            if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)) > 0.0001:
                                                while True:
                                                    try:
                                                        if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)) <= 0.0001:
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
                                                if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)) <= 0.0001:
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
                                                    if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)) <= 0.0001:
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

                                                if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)) > 0.0001:
                                                    while True:
                                                        try:
                                                            if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)) <= 0.0001:
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
                                                    if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)) <= 0.0001:
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
                                                if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)) <= 0.0001:
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
                                                if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)) <= 0.0001:
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
                                                if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)) <= 0.0001:
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
                                                        if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)) <= 0.0001:
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
                                print("Multi C-ROB (I) Waiting !")
                                print("--------------------------------------")
                                print("Multi C-ROB (I) Coin: ", self.SORUMLU_COİN_ONE)
                                print("Multi C-ROB (I) Buy: ", round(float(self.SORUMLU_COİN_ONE_AL), 1))
                                print("Multi C-ROB (I) Sell: ", round(float(self.SORUMLU_COİN_ONE_SAT), 1))
                                print("Multi C-ROB (I) Genel Piyasa: ", Proposal.Market_STR)
                                print("Multi C-ROB (I) Anlık Piyasa: ", NOW_MARKETİNG_STR_DATA())
                                print("Toplam İşlem Ücretiniz : ", round(self.Fee,4),end="$\n")
                                print("--------------------------------------")
                                print("Geçen Süre : ", CANCEL_SAYAC,end="\n\n\n\n")

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
                                    print("Buying Zarar Kurtarma Function !")
                                    try:
                                        Intelence.ROB_CANCEL(symbol=self.SORUMLU_COİN_ONE, orderID=START_BUY_ORDER_ID)
                                        time.sleep(1)
                                    except:
                                        pass
                                    def ZARAR_KURTARMA(Price=AL_MultiChain_ONE[0]):
                                        while True:
                                            try:
                                                ANLIK = float(ROB.get_ticker(symbol=self.SORUMLU_COİN_ONE)['lastPrice'])
                                                Quantity = math.floor(float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol='BUSD'))) / float(ANLIK)
                                                STEP = get_round_step_quantity(qty=Quantity)
                                                PRİCE = Price
                                                Intelence.ROB_BUY_LİMİT(symbol=self.SORUMLU_COİN_ONE, quantity=float(STEP), price=str(PRİCE))
                                            except:
                                                break
                                            break
                                    while True:
                                        if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol='BUSD')) < 10:
                                            BUY_ZARAR_KURTARMA += True
                                            break
                                        else:
                                            time.sleep(1)
                                            ZARAR_KURTARMA()
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
                                    if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)) >= 0.0001:
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
                elif BALANCE >= 0.0001:
                    SORUMLU_COİN_BALANCE = self.SORUMLU_COİN_ONE.replace('BUSD', '')
                    SAT_MultiChain_ONE = list()
                    MAX_MultiChain_ONE = list()
                    TİME_ZONE = list()
                    CANCEL_SAYAC_BALANCE = 0
                    STOP = False

                    while True:
                        try:
                            if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)) <= 0.0001:
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

                            STOP_FUNCTİON_BUY_PRİCE = round(float(SORUMLU_COİN_ONE_AL),1)
                            STOP_FUNCTİON_SELL_PRİCE = round((float(SORUMLU_COİN_ONE_SAT * 40) / 100),1)
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
                                        if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)) < 0.0001:
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
                                    if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)) <= 0.0001:
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
                                                if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)) <= 0.0001:
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
                                    if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)) <= 0.0001:
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
                                                if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)) <= 0.0001:
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

                                            if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)) > 0.0001:
                                                while True:
                                                    try:
                                                        if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)) <= 0.0001:
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
                                                if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)) <= 0.0001:
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
                                                if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)) <= 0.0001:
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
                                                if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)) <= 0.0001:
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
                                                if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)) <= 0.0001:
                                                    break
                                                else:
                                                    time.sleep(1)
                                                    PUMP_TWO_BUSD.PUMP_OPTİON_START()
                                                    print("Try Again PUMP Sell Order...")
                                            except:
                                                print("Tekrardan Bağlantı Sağlanıyor.")

                                        orders = ROB.get_open_orders(symbol=self.SORUMLU_COİN_ONE)
                                        orders_ID= orders[0]['orderId']
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
                                                        if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)) <= 0.0001:
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
                                                    if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)) <= 0.0001:
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
                                                    if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)) <= 0.0001:
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
                                                    if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)) <= 0.0001:
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
                                                            if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)) <= 0.0001:
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
                                print("Toplam İşlem Ücretiniz : ",round(self.Fee,4),end="$\n")
                                print("--------------------------------------")
                                print("Geçen Süre : ", CANCEL_SAYAC_BALANCE,end="\n\n\n\n")

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
                                        Intelence.ROB_CANCEL(symbol=self.SORUMLU_COİN_ONE,orderID=ORDER_ID)
                                        time.sleep(1)
                                    except:
                                        pass
                                    def ZARAR_KURTARMA(Price = SAT_MultiChain_ONE[0]):
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
                                        if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)) < 0.0001:
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
                                            print("Stop  Referans Noktası : ",float(SAT_MultiChain_ONE[0]) * ((KAARLILIK_KURTARICISI() - 0.3) + 100) / 100)
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
                                                        if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)) < 0.0001:
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
                                                                    if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=SORUMLU_COİN_BALANCE)) < 0.0001:
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
                                    print("Ödeme Tutarı : ",round(self.Fee,4),end="$\n")
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
                    MultiChain_Algorithm(LossAlgorithm= True, ControlAlgorithm= True, SELL_OpportunityAlgorithm= True, BUY_OpportunityAlgorithm= True, WavyAlgorithm= True)
                elif self.PİYASA_DURUMU == 2:
                    MultiChain_Algorithm(LossAlgorithm= True, ControlAlgorithm= True, SELL_OpportunityAlgorithm= True, BUY_OpportunityAlgorithm= True, WavyAlgorithm= True)
                elif self.PİYASA_DURUMU == 3:
                    MultiChain_Algorithm(LossAlgorithm= True, ControlAlgorithm= True, SELL_OpportunityAlgorithm= True, BUY_OpportunityAlgorithm= True, WavyAlgorithm= True)
                elif self.PİYASA_DURUMU == 4:
                    MultiChain_Algorithm(LossAlgorithm= True, ControlAlgorithm= True, SELL_OpportunityAlgorithm= True, BUY_OpportunityAlgorithm= True, WavyAlgorithm= True)
                elif self.PİYASA_DURUMU == 5:
                    MultiChain_Algorithm(LossAlgorithm= True, ControlAlgorithm= True, SELL_OpportunityAlgorithm= True, BUY_OpportunityAlgorithm= True, WavyAlgorithm= True)
                elif self.PİYASA_DURUMU == 6:
                    MultiChain_Algorithm(LossAlgorithm= True, ControlAlgorithm= True, SELL_OpportunityAlgorithm= True, BUY_OpportunityAlgorithm= True, WavyAlgorithm= True)
                elif self.PİYASA_DURUMU == 7:
                    MultiChain_Algorithm(LossAlgorithm= True, ControlAlgorithm= True, SELL_OpportunityAlgorithm= True, BUY_OpportunityAlgorithm= True, WavyAlgorithm= True)
                elif self.PİYASA_DURUMU == 8:
                    MultiChain_Algorithm(LossAlgorithm= True, ControlAlgorithm= True, SELL_OpportunityAlgorithm= True, BUY_OpportunityAlgorithm= True, WavyAlgorithm= True)
                else:
                    MultiChain_Algorithm(LossAlgorithm= True, ControlAlgorithm= True, SELL_OpportunityAlgorithm= True, BUY_OpportunityAlgorithm= True, WavyAlgorithm= True)
        MultiChain = threading.Thread(target=MultiChain_ONE)
        MultiChain.start()


Constructor = Constructor()
Constructor.__str__()
MMChain = MultiChainAutoSystem()
# ----------------------------------------------------------------------------------------------------------------------
