#define fucntion to calculate cube 
def cube(number):
    return number*number*number

#define a fucntion which will execute cube fuction if the user entered number is divisible by 3
def by_three(number):
    if number %3 == 0:
      return cube(number)
    else:
       return False
#display result 
print(by_three(9))
print(by_three(4))