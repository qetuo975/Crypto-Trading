import ROB_Piyasa
from tqdm import tqdm
from time import sleep


class Marketing_Analysis(ROB_Piyasa.Market):
    def __init__(self):
        super().__init__()

        # Generate Override
        #-------------------------------------
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

        self.Market_STR = str
        self.Market_INT = int


    def __str__(self):
        print("\n\n")
        for i in tqdm(range(15, unit="ROB Core", colour="#ff4040")):
            sleep(0.1)
        print("\n\n")
        print("Crypto ROB Private Core Versiyon !")
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




