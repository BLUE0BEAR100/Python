#Initialize dictionary 
test_dict = {'Codingal' : 2,'is': 2,'best':2,'for' :2,'Coding' : 1}

#printing org dict
print("The original dictonary : "+ str(test_dict))

#initialize value
K = 2

#Using loop
#Slective key vaules
res=0
for  key in test_dict:
    if test_dict[key]==K:
        res=res+1

print("Frequency of K is "+str (res))