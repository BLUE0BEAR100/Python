#Take input for the student that he can attend the exam or not
medical_cause=input("Did you have a medical cause Y or N :-")
#take input of atten
atten=int(input("enter the attendance of the student:-"))

#cheaking
if medical_cause== 'Y' :
    print("You are allowed")
else:
  if atten>=75 : #2nd condition
    print("Allowed")
  else:
     print("No allowed")