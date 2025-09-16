#Class 1
class Bangladesh():
    def capital(self):
        print("Dhaka is the capital of Bangladesh")

    def language(self):
        print("Bangla is the most widely and gourgias spoken language of Bangladesh")
        
    def type(self):
        print("Bangladesh is a not that fast developing country ")
    
#class 2
class UK():
    def capital(self):
        print("London is the captial city of UK")

    def language(self):
        print("Smooth English is primary language of UK ")

    def type(self):
        print("Uk is devloped country they once counqured the world")

#obj creation
obj_bd=Bangladesh()
obj_uk=UK()

#common interface
for country in (obj_bd,obj_uk):
    country.capital()
    country.language()
    country.type()