class Comuputer:

    def __init__(self):
        self.__maxprice = 900
    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self,price):
        self.__maxprice = price

c = Comuputer()
c.sell()

#change the price
c.__maxprice = 1000
c.sell()

#using setter fucn
c.setMaxPrice(100000)
c.sell()