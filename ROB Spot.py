import time
import math
import threading
from binance import Client
from decimal import Decimal
from colorama import Fore, Back, Style, init
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
secret = "ODEf7glIbPeKg7Ec4eDTxX7LtVhWv2FAANMIGLEYwSVBIJf4tbnZ5jPVk2X07OC4"
ap?? = "YkB8jMJK2KZI4nwvHpKMtd13VNIKRytxiTaKHJF5fU9JVM77WEHjm6JCSHdzwmrH"
ROB = Client(ap??,secret)



class Intelence():
    # ROB EM??R FONKS??YONLARI
    def ROB_CANCEL(symbol,orderID):
        ROB.cancel_order(
            symbol=symbol,
            orderId=orderID)
        print("Cancel Order")
        print("Coin : ",symbol)
    def ROB_BUY_L??M??T(symbol,quantity,price):
        ROB.order_limit_buy(
            symbol=str(symbol),
            quantity=float(quantity),
            price=str(price))
        print("Order Successful !")
        print("Coin : ",symbol,"\nQuantity : ",quantity,"\nPrice : ",price)
    def ROB_SELL_L??M??T(symbol,quantity,price):
        ROB.order_limit_sell(
            symbol=str(symbol),
            quantity=float(quantity),
            price=str(price))
        print("Order Successful !")
        print("Coin : ",symbol,"\nQuantity : ",quantity,"\nPrice : ",price)
    def ROB_BUY_MARKET(symbol,quantity):
        ROB.order_market_buy(
            symbol=str(symbol),
            quantity=float(quantity))
        print("Market Order Successful !")
        print("Coin : ",symbol,"\nQuantity : ",quantity)
    def ROB_SELL_MARKET(symbol,quantity):
        ROB.order_market_sell(
            symbol=str(symbol),
            quantity=float(quantity))
        print("Market Order Successful !")
        print("Coin : ",symbol,"\nQuantity : ",quantity)

    # ACCOUNT FONKS??YONLARI
    def ROB_ACCOUNT_GET_BALANCE(symbol):
        balance = ROB.get_asset_balance(asset=symbol)
        balance_free = balance["free"]
        return balance_free
    def ROB_ACCOUNT_GET_TRADES_H??STORY(symbol):
        trades = ROB.get_my_trades(symbol=symbol)
        for i in trades:
            print(i["qty"])
    def ROB_ACCOUNT_STATUS():
        status = ROB.get_account_status()
        return status["data"]
    def ROB_ACCOUNT_SNAPSHOT(params):      #TYPE = SPOT / MARGIN / FUTURES
        snapshot = ROB.get_account_snapshot(type=params)
        return snapshot


    # MARKET FONKS??YONLARI
    def ROB_SPOT_ORDER_BOOK(symbol):
        depth = ROB.get_order_book(symbol=symbol)
        indexing = 0
        history = list()
        order = list()
        amount = list()

        indexing_sell = 0
        history_sell = list()
        order_sell = list()
        amount_sell = list()


        for i in depth.get('bids'):
            indexing += 1
            if indexing == 11:
                break
            else:
                history.append(i)

        for i in history:
            order.append(i[0])
            amount.append(i[1])
        #--------------------------------
        for i in depth.get('asks'):
            indexing_sell += 1
            if indexing_sell == 11:
                break
            else:
                history_sell.append(i)

        for i in history_sell:
            order_sell.append(i[0])
            amount_sell.append(i[1])

        return order,amount,order_sell,amount_sell



    def ROB_SPOT_H??STORY_BOOK(symbol):
        price = list()
        amount = list()
        trades = ROB.get_recent_trades(symbol=symbol)
        for i in trades:
            price.append(i["price"])
            amount.append(i["qty"])
        price.reverse()
        amount.reverse()
        return price,amount



class ROB_SPOT():
    def __init__(self):
        self.BUY = 0
        self.SELL = 0

        self.RETURNS_BUY_ORDER_PR??CE = 0
        self.RETURNS_SELL_ORDER_PR??CE = 0

        self.CRYPTO_BUSD = str
        self.CRYPTO_CANCEL_ID = str

        self.CRYPTO_AMOUNT_BUY = list()
        self.CRYPTO_PR??CE_BUY = list()

        self.CRYPTO_AMOUNT_SELL = list()
        self.CRYPTO_PR??CE_SELL = list()

        self.CRYPTO()
        self.CRYPTO_BUSD_REPLACE = self.CRYPTO_BUSD.replace("BUSD","")

        Thread_I = threading.Thread(target=self.CRYPTO_SPOT_PR??CE)
        Thread_II = threading.Thread(target=self.CRYPTO_ROB_SPOT_ENG??NNER)
        Thread_III = threading.Thread(target=self.__str__)
        Thread_I.start()
        Thread_II.start()
        #Thread_III.start()


    def __str__(self):
        while True:
            time.sleep(1)
            print("Buy Return : ",self.RETURNS_BUY_ORDER_PR??CE)
            print("Sell Return : ",self.RETURNS_SELL_ORDER_PR??CE)
    def CRYPTO_SPOT_SELL(self):
        while True:
            try:
                BALANCE = math.floor(float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=self.CRYPTO_BUSD_REPLACE)))
                ANLIK = float(ROB.get_ticker(symbol=str(self.CRYPTO_BUSD))['lastPrice'])
                PR??CE = self.SELL
                Intelence.ROB_SELL_L??M??T(symbol=self.CRYPTO_BUSD, quantity=float(BALANCE), price=str(PR??CE))  # SAT L??M??T EMR?? # HEDEFE G??RE AYARLANACAK
                self.RETURNS_SELL_ORDER_PR??CE = float(PR??CE)
                return float(PR??CE)
            except:
                break
            break
    def CRYPTO_SPOT_BUY(self):
        while True:
            try:
                ANLIK = float(ROB.get_ticker(symbol=self.CRYPTO_BUSD)['lastPrice'])
                BUSD = float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol="BUSD"))
                Quantity = math.floor(BUSD) / float(ANLIK)
                PR??CE = self.BUY
                Intelence.ROB_BUY_L??M??T(symbol=self.CRYPTO_BUSD, quantity=math.floor(float(Quantity)) - 1, price=str(PR??CE))
                self.RETURNS_BUY_ORDER_PR??CE = float(PR??CE)
                return float(PR??CE)
            except:
                break
            break
    def CRYPTO_SPOT_ITERATOR_PR??CE(self):
        try:
            self.CRYPTO_PR??CE_BUY.append(float(self.CRYPTO_SPOT_ORDER_BOOK()[0][0]))
            self.CRYPTO_PR??CE_SELL.append(float(self.CRYPTO_SPOT_ORDER_BOOK()[2][0]))

            BUYS = self.CRYPTO_PR??CE_BUY[0]
            SELLS = self.CRYPTO_PR??CE_SELL[0]
            self.CRYPTO_PR??CE_SELL = list()
            self.CRYPTO_PR??CE_BUY = list()
            return float(BUYS),float(SELLS)
        except:
            pass
    def CRYPTO_ROB_SPOT_ENG??NNER(self):
        while True:
            try:
                time.sleep(1)
                BUSD = float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol="BUSD"))
                CRYPTO = float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=self.CRYPTO_BUSD_REPLACE))
                print("SPOT ENG??NNER Loading !")
                if BUSD > 15:
                    while True:
                        if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol="BUSD")) < 15:
                            break
                        else:
                            time.sleep(1)
                            self.CRYPTO_SPOT_BUY()
                elif CRYPTO > 0.99:
                    while True:
                        if float(Intelence.ROB_ACCOUNT_GET_BALANCE(symbol=self.CRYPTO_BUSD_REPLACE)) < 0.99:
                            break
                        else:
                            time.sleep(1)
                            self.CRYPTO_SPOT_SELL()

                elif (self.RETURNS_BUY_ORDER_PR??CE > 0) and self.CRYPTO_SPOT_ITERATOR_PR??CE()[0] < self.RETURNS_BUY_ORDER_PR??CE:
                    print("sa")
                    self.CRYPTO_SPOT_CANCEL_ORDER(Cancel_ORDER=self.CRYPTO_SPOT_CANCEL_ORDER_ID())
                    self.RETURNS_BUY_ORDER_PR??CE = 0
                elif (self.RETURNS_SELL_ORDER_PR??CE > 0) and self.CRYPTO_SPOT_ITERATOR_PR??CE()[1] < self.RETURNS_SELL_ORDER_PR??CE:
                    print("as")
                    self.CRYPTO_SPOT_CANCEL_ORDER(Cancel_ORDER=self.CRYPTO_SPOT_CANCEL_ORDER_ID())
                    self.RETURNS_SELL_ORDER_PR??CE = 0
            except:
                pass


    def CRYPTO_SPOT_CANCEL_ORDER_ID(self):
        orders = ROB.get_open_orders(symbol=self.CRYPTO_BUSD)
        orders_ID = orders[0]['orderId']
        return str(orders_ID)
    def CRYPTO_SPOT_CANCEL_ORDER(self,Cancel_ORDER):
        while True:
            try:
                time.sleep(1)
                Intelence.ROB_CANCEL(symbol=self.CRYPTO_BUSD,orderID=Cancel_ORDER)
            except:
                break
    def CRYPTO_SPOT_PR??CE(self):
        while True:
            try:
                time.sleep(1)
                self.BUY = round(float(list(self.CRYPTO_SPOT_ITERATOR_PR??CE())[0]) + 0.0001,5)
                self.SELL = round(self.CRYPTO_SPOT_ITERATOR_PR??CE()[1] - 0.0001,5)
            except:
                pass
    def CRYPTO_SPOT_ORDER_BOOK(self):
        CRYPTO_PR??CE_BUY, CRYPTO_AMOUNT_BUY, CRYPTO_PR??CE_SELL, CRYPTO_AMOUNT_SELL = Intelence.ROB_SPOT_ORDER_BOOK(symbol=self.CRYPTO_BUSD)
        return CRYPTO_PR??CE_BUY,CRYPTO_AMOUNT_BUY,CRYPTO_PR??CE_SELL,CRYPTO_AMOUNT_SELL
    def CRYPTO(self):
        print("""
1. LAZIO / BUSD
        """)

        CRYPTO = input("????lem Yapaca????n??z Kripto Paray?? Se??iniz : ")
        if int(CRYPTO) == 1:
            self.CRYPTO_BUSD = "LAZIOBUSD"
        print("Se??ilen Kripto Para : ",self.CRYPTO_BUSD)

Object = ROB_SPOT()