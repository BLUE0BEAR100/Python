#create class
class Parrot:

    #class attribute
    species = 'bird'

    #intance attribute
    def __init__(self,name,age,color):
        self.name=name
        self.age=age
        self.color=color

#instaniate the parrot class
blu=Parrot("Blu",5,'Blue')
woo=Parrot('Woo',7,'Red')

#access the class attributes
print("blu is a {}".format(blu.species))
print("woo is a {}".format(woo.species))

# access the instance attributes
print("{} is {} years old and color is {}".format(blu.name,blu.age,blu.color))
print("{} is {} years old and color is {}".format(woo.name,woo.age,woo.color))