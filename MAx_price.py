class max_pricce:
    def __init__(self):
        self.__max_price = 900
    def sell(self):
        print("selling price is {}".format(self.__max_price))
    def setmaxeprice(self,price):
        self.__max_price = price
c = max_pricce()
c.sell()
c.__max_price = 1000
c.sell()
c.setmaxeprice(1000)
c.sell()