#take input 
x=str(input("Please input the fiiller of the pyramid : "))
print("Half  Pyramid Pattern Of Starts (",x,") : ")
n= int(input("Enter the number of rows: "))
#outer loop handle number of rows
for i in range(n):
    #inner loop to handle number of columns
    for j in range(i+1):
        #display result
        print(x, end="")
    print()