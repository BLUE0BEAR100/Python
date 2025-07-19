L=[2,5,3,6,7,5,8,69]
print('Orginal List :',L)

#var to store the sum of 
#the list
count=0

#finding sum
for i in L:
    count+= i
#divide the total elements by
#number of elements
avg=count/len(L)

print("sum =",count)
print("average =",avg)

#sorting the elements of the list 
L.sort()

#printing the first element
print("Smallest element is:",L[0])

#printung the last element
print("Largest element is:",L[-1])