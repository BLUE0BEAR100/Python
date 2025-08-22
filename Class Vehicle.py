#Create class
class Vehicle:

    #create init method
    def  __init__(self,max_speed, mileage,name ):
        #blind the arguments
        self.max_speed = max_speed
        self.mileage = mileage
        self.name = name
#obj creation 
Bugatti=Vehicle(490,8,'Bugatti')
print("Car name",Bugatti.name,"Max speed",Bugatti.max_speed)
