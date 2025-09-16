#parent clas
class Person(object):


    #init is known as the constructor
    def __init__(self,name,idnumber):
        self.name = name
        self.idnumber=idnumber
    def display(self):
        print(self.name)
        print(self.idnumber)

#child class
class Employee(Person):
    def __init__(self, name, idnumber,salary,post):
        self.salary=salary
        self.post=post

        #invoking the __init__ of the parent class
        Person.__init__(self,name,idnumber)


#creation of an obj var
a = Employee('Rahul',69696,100000,"Intern")

a.display()