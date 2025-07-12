import random #importing module
playing = True #initialise
number=str(random.randint(10,20)) #random in-built fucntion

print("I'll generate a number from 10 to 20, you have to guess the number one digit at a time.")
print("The game ends when you get 1 hero!")
#iterate loop till the con is True
while playing:
    guess=input("Give me your best guess! : ")
    if number==guess:
        print("You won")
        print("The number was ",number)
        break
    else:
        print("Your guess isn't right, try again.\n")