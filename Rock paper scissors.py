import random #module

options = ["Rock","Paper","Scissors"]

user_choice = input("Choose Rock,Paper or Scissors: ")

computer_choice = random.choice(options)

print("You chose:",user_choice)
print("Computer chose:",computer_choice)

if user_choice==computer_choice:
    print("It's a tie!")
elif user_choice== "Rock" and computer_choice=="Scissors":
    print("Rock smashes scissors! You won!")
elif user_choice== "Papper" and computer_choice=="Rock":
    print("Paper covers rock! You won!")
elif user_choice== "Scissors" and computer_choice=="Paper":
    print("Scissors cuts paper! You won!")
else:
    print("You lose! ")