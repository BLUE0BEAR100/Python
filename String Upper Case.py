#create class
class IOString():

    #construtor to set default value
    def __init__(self):
        self.str1=""

    #function to get input
    def get_String(self):
        self.str1=input("Enter String : ")

        #function to print the string in upper case
    def print_String(self):
        print("Result is :", self.str1.upper())

#obj creation 
str1 = IOString()

#call func
str1.get_String()
str1.print_String()