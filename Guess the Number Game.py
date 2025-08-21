#Import
import random
import time

#Pick a number between 1 and 100
number=random.randint(1,100)

def intro():
    print("Whats your name?")
    #name selecting
    global name 
    name=input() #ask for the name
    print(name+", we are going to play a game. I am thinking of a number between 1 and 100")
    if(number%2==0):
        x='even'
    else:
        x='odd'
    print("\nThis is an {} number".format(x))
    time.sleep(.5)
    print("Go ahead. Guess❓!")

def pick():
    guessesTaken = 0

    #if the number of guesses is less than 6
    while guessesTaken < 6:
        time.sleep(.25)
        #inserts the place to enter guess
        enter=input("Guess:")
        #cheak if a number was entered
        try:

            #stores the guess as an integer instead of a string
            guess = int(enter)

            if guess<=100 and guess>=1: #if they are in range
                guessesTaken=guessesTaken+1
                if guessesTaken<6:
                    if guess<number:
                        print("The guess of the number that you have entered is too low")
                    if guess>number:
                        print("The guess of the number that you have entered is too high")
                    if guess != number:
                        time.sleep(.5)
                        print("Try Again!")
                #if the guess is right then we are going to jump out of the while block
                    if guess==number:
                      break
            if guess>100 or guess<1:
                    print("Silly goose! That number isnt in the range!")
                    time.sleep(.25)
                    print("PLEASE ENTER A NUMBER BETWEEN 1 AND 100")

        except:
            print("I dont think that"+enter+"Is a number.Sorry")

    if guess==number:
            guessesTaken=str(guessesTaken)
            print("Good job, {}! You guessed my number in {} guesses!".format(name,guessesTaken))
    if guess != number:
            print("Nope. The number i waas thinking was "+ str(number))
playagain="yes"
while playagain=="yes" or playagain=="y" or playagain == "Yes":
    intro()
    pick()
    print("Do you want to play again?")
    playagain=input()