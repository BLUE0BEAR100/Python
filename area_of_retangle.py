#create class 
class Rectangle():
    def __init__(self,l,w):
        self.length=l
        self.width=w

    def rectangle_area(self):
        return self.length*self.width


length=int(input("Please enter length :"))
width=int(input("Please enter width :"))
newRectangle = Rectangle(length,width)
print(newRectangle.rectangle_area())