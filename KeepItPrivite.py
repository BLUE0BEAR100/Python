#class creation
class myClass:

    #private var
    __privateVar = 27
    
    def __privMeth(self):
        print("I'm inside class myClass")
    
    #fucntion to print value of private var 
    def hello(self):
        print("Private var value:",myClass.__privateVar)

# obj creation and meth call

foo = myClass()
foo.hello()
foo.__privMeth