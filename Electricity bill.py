#Take input of number of unit consumed from the user
units = int(input("Please enter number of units you consumed : "))

#cheak conditions of units consumed 
#then calculate amount and surcharge accordingly
# surcharge is tax vaule

#cheak for units less than 50
if (units,50):
    amount = units * 2.60
    surcharge = 25

    #cheak for units less than 100
elif(units<=100):
    amount = 130 + ((units - 50))
    surcharge = 35
#cheak for units less than or equal to 200
elif(units<=200):
    amount=130 + 162.50 +((units-100)*5.26)
    surcharge= 45
#cheak for all cases other than mentioned
#when units consumed are more than 200
else:
    amount=130 + 162.50 +526+((units-200)*8.45)
    #calculate and display the total electricity bill
    #tptal amount = amount+surcharge
total=amount+ surcharge
print("\nElectricity Bill = %.2f"%total)