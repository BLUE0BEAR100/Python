r=int(input("Put a number for cheak tuple: "))
#function to cheak wether palidromme or not
def palind(r):
    l=len(r)-1
    f=0
    while(f<l):
        if(r[f]!=r[l]):
            return False
        f+=1
        l-=1
    return True


if(palind(r)):
    print("The Tuple is Flip-Flop")
else:
    print("The Tuple Is not Flip-Flop")