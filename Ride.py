print("Select Your Destination :")
print("1. Inter Country")
print("2. Inter City")
print("3. Inter-District")

#Taking input of number 1 , 2 or 3
#Select Your Destination
choice = int(input("Enter Your Choice: "))

#User Selected option 1
if (choice==1): #condition 1 if statement
    print("Select Your Vehicle: ")
    print("1. Plane")
    print("2. Train")
    #Selecting the type  of Vehicle for inter country
    choice2=int(input("Enter Your Vehicle: "))
    if(choice2==1): #inner if statement print
        print("You Have Selected Plane")
    else:
        print("You Have Selected Train")

#user entered the second option
elif(choice==2): #elif statement
    print("Select Your Vehicle: ")
    print("1. Bus")
    print("2. Train")
    #Selecting the type  of Vehicle for inter country
    choice7=int(input("Enter Your Vehicle: "))
    if(choice7==1): #if statement
        print("Select Your Destination: ")
        print("1. Dhaka-Chattogram")
        print("2. Chattogram-Dhaka")
        print("3. Dhaka-Barishal")
        print("4. Barishal-Dhaka")
        print("5. Chattogram-Barishal")
        print("6. Barishal-Chattogram")
        choice8=int(input("Enter Your Destination Route: "))
        if(choice8==1):
            print("Your Destination Is Dhaka-Chattogram")
        elif(choice8==2):
            print("Your Destination Is Chattogram-Dhaka")
        elif(choice8==3):
            print("Your Destination Is Dhaka-Barishal")
        elif(choice8==4):
            print("Your Destination Is Barishal-Dhaka")
        elif(choice8==5):
            print("Your Destination Is Chattogram-Barishal")
        elif(choice8==6):
            print("Your Destination Is Barishal-Chattogram")
    elif(choice7==2): #if statement
        print("Select Your Destination: ")
        print("1. Dhaka-Chattogram")
        print("2. Chattogram-Dhaka")
        print("3. Dhaka-Barishal")
        print("4. Barishal-Dhaka")
        print("5. Chattogram-Barishal")
        print("6. Barishal-Chattogram")
        choice9=int(input("Enter Your Destination Route: "))
        if(choice9==1):
            print("Your Destination Is Dhaka-Chattogram")
        elif(choice9==2):
            print("Your Destination Is Chattogram-Dhaka")
        elif(choice9==3):
            print("Your Destination Is Dhaka-Barishal")
        elif(choice9==4):
            print("Your Destination Is Barishal-Dhaka")
        elif(choice9==5):
            print("Your Destination Is Chattogram-Barishal")
        elif(choice9==6):
            print("Your Destination Is Barishal-Chattogram")

#user entered the Third option
elif(choice==3): #elif statement
    print("Select Your Ride :")
    print("1. Car")
    print("2. Bike")
    print("3. Cycle")
    choice3=int(input("Enter Your Ride: ")) #selecting 1 2 or 3
    if(choice3==1): #if statement
        print("Which Type Of Car:")
        print("1. SUV")
        print("2. Sedan")
        print("3. SportsCar")
        choice4=int(input("Enter Your Car Type: "))  #selecting 1 2 or 3
        #selecting car type
        if (choice4==1):
            print("You Have Selected SUV")
        elif(choice4==2):
            print("You Have Selected Sedan")
        elif(choice4==3):
            print("You Have Selected SportsCar")
    if(choice3==2): #if statement
        print("Which Type Of Bike:")
        print("1. Scooter")
        print("2. SportBike")
        print("3. Moped")
        choice5=int(input("Enter Your Bike Type: "))  #selecting 1 2 or 3
        #selecting car type
        if (choice5==1):
            print("You Have Selected Scooter")
        elif(choice5==2):
            print("You Have Selected SportBike")
        elif(choice5==3):
            print("You Have Selected Moped")
    if(choice3==3): #if statement
        print("How many time you'll borrow the Cycle:")
        print("1. Rent or Borrow for 1 Hour")
        print("2. Rent or Borrow for 24 Hour")
        print("3. Rent or Borrow for 168 Hour")
        choice6=int(input("Enter Your Cycle Time: "))  #selecting 1 2 or 3
        #selecting car type
        if (choice6==1):
            print("You Have Selected 1 Hour")
        elif(choice6==2):
            print("You Have Selected 24 Hour")
        elif(choice6==3):
            print("You Have Selected 168 Hour")
