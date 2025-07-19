#function to cheak whether
#first and last char of words match
def match_words(words):
    count=0
    lst=[]
    for word in words :
     if len(word)>1 and word[0]==word[-1]:
        count+=1
        lst.append(word)

    print("List of words with first and last char same\n",lst)
    return count
count = match_words(['111','909','696','121'])
print("Number of words having first and last char same",count)