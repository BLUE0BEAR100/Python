#taking input from user N or the number which will be powered
n=int(input("Enter the base number: "))
p=int(input("Enter the power: "))

#Initialize sum
sum=0

for i in range(1,p+1): #for loop statement
    sum=n**i #actuall calculation
print(n,"**",p,"= ",sum) #printing the final ans
