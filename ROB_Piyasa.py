import ROB_Crypto_GET

class Market():
    def __init__(self):
        self.Bitcoin = float
        self.Analysis = ROB_Crypto_GET.Crypto_GET()
        self.Analysis.Analysis()


        # Gündelik Bitcoin Oranları
        #-------------------------------------
        self.ONE_DAY_YUZDE = 0
        self.TWO_DAY_YUZDE = 0
        self.THREE_DAY_YUZDE = 0
        self.FOUR_DAY_YUZDE = 0
        self.FİVE_DAY_YUZDE = 0
        self.SİX_DAY_YUZDE = 0
        self.SEVEN_DAY_YUZDE = 0

        # Gündelik Bitcoin Kapanışları
        #-------------------------------------
        self.ONE_DAY_CLOSE = self.Analysis.BTC_CLOSE[0]
        self.TWO_DAY_CLOSE = self.Analysis.BTC_CLOSE[1]
        self.THREE_DAY_CLOSE = self.Analysis.BTC_CLOSE[2]
        self.FOUR_DAY_CLOSE = self.Analysis.BTC_CLOSE[3]
        self.FİVE_DAY_CLOSE = self.Analysis.BTC_CLOSE[4]
        self.SİX_DAY_CLOSE = self.Analysis.BTC_CLOSE[5]
        self.SEVEN_DAY_CLOSE = self.Analysis.BTC_CLOSE[6]


        # Gündelik Bitcoin Açılışları
        #-------------------------------------
        self.ONE_DAY_OPEN = self.Analysis.BTC_OPEN[0]
        self.TWO_DAY_OPEN = self.Analysis.BTC_OPEN[1]
        self.THREE_DAY_OPEN = self.Analysis.BTC_OPEN[2]
        self.FOUR_DAY_OPEN = self.Analysis.BTC_OPEN[3]
        self.FİVE_DAY_OPEN = self.Analysis.BTC_OPEN[4]
        self.SİX_DAY_OPEN = self.Analysis.BTC_OPEN[5]
        self.SEVEN_DAY_OPEN = self.Analysis.BTC_OPEN[6]


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


