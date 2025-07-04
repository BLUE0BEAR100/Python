factorial = int(input("Please enter a number for factorial"))
def factorial(x):
  if x==0 or x==1:
       return 1
  else:
    #calling funtion inside a function
      return x*factorial(x-1)

#display result
print(factorial.__doc__)
print("The factorial of 0: ",factorial(0))
print("The factorial of 1: ",factorial(1))
print("The factorial of 4: ",factorial(4))
print("The factorial of 5: ",factorial(5))
print("The factorial of 10: ",factorial(10))