#Talking total amout as input from user
Amount=int(int(input("Please Enter Amount For withdraw")))

#Calculating the number of notes
note_1=Amount//100
note_2=(Amount%100)
note_3=((Amount%100)%50)//10
note_4=(((Amount%100)%50)%10)//2

print("notes of 100 taka",note_1)
print("notes of 50 taka",note_2)
print("notes of 10 taka",note_3)
print("notes of 2 taka",note_4)