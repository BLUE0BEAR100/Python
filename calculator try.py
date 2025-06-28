def add(P , Q):
    return P + Q

def sub(P , Q):
    return P - Q

def mul(P , Q):
    return P * Q

def div(P , Q):
    return P / Q
#Now we will take inputs from the user
print("Please select operation")
print("a.Add")
print("b.sub")
print("c.mul")
print("d.div")

choice = input("Please enter choice (a/b/c/d): ")

num_1 = int(input("Please enter the first number: "))
num_2 = int(input("Please enter the second number: "))

if choice == "a":
    print(num_1,"+" ,num_2,"=",add(num_1 ,num_2))
elif choice =="b":
    print(num_1,"-" ,num_2,"=",sub(num_1 ,num_2))
elif choice =="c":
    print(num_1,"*" ,num_2,"=",mul(num_1 ,num_2))
elif choice =="d":
    print(num_1,"/" ,num_2,"=",div(num_1 ,num_2))
else:
    print("This is an invaild input")
