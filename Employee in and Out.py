#create class 
class Employee:

    #initializing
    def __init__(self,name):
        self.name=name
        print("Employee created")
    
    #calling destructor
    def __del__(self):
        print("Destructor called")


obj = Employee("newton")
print(obj.name)
print('program end. . .')

#expicitly
del obj 
print(obj.name)