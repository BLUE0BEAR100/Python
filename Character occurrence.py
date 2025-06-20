#take input of word 
string = input("Please enter your word :-")
#take input of character
char = input("Please enter your Character that you want to find : -") 
i=0
count = 0
#loop will to find the occurence of character 
while(i<len(string)):#string operation
    
    if(string[i]==char): #condition 1
        count=count+1
    i = i+1
#display the result
print("TheTotal Number of times ",char,"has Occured :- " , count) 