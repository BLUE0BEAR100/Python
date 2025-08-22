class fruit:
    #class variable
    taste = 'Sweet'

    #Instance var
    def __init__(self,name,color):
        self.name=name
        self.color=color

#obj creation 
apple = fruit('Apple','Red')
banana=fruit('Banana','Yellow')

print(apple.taste)
print(apple.name,apple.color)
print(banana.name,banana.color)