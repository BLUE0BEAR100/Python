#Add two lists using map and lambda
numbers = (1,2,3,4,5,6,7,8,9,10)
result=map(lambda n:n*n,numbers)
print("two lists")
print(list(result))

#using map
nums=[1,2,3,4,5,6]
def sq(n):
    return n*n
sqaure=list(map(sq,nums))
print("Sqaure of this list numbers ")
print(sqaure)