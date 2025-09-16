#import necessary packages
from abc import ABC, abstractmethod
#create a base class
class Animal(ABC):

    @abstractmethod
    def move(self):
        print("walking")

class Human(Animal):
    def move(self):
        print("I can walk run sprint and crawl")
class Snake(Animal):
    def move(self):
        print("I can crawl")
class Dog(Animal):
    def move(self):
        print("I can run sprint and crawl")
class Lion(Animal):
    def move(self):
        print("I can run sprint and crawl + roar")

#Driver code


H = Human()
H.move()

K = Snake()
K.move()

F = Lion()
F.move()

D = Dog()
D.move()


