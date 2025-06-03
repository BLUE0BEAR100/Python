#taking an input of alphabet
print("Enter a character: ",end="")
c=(input("Enter A alphabet: "))
if len(c)>1:
    print("Invalid Input")
else:
    if c>='a' and c<='z':
        print(c," is an alphabet")
    elif c>='A' and c<='Z':
        print(c," is an alphabet")
    else:
        print(c," is not an alphabet")