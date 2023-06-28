#calculaitng percentage
percentage= (total/500)*100
print("Your percentage is: "percentage)

#grades
if (percentage>=30):
    print("Result: Congratulations! You have passed")
else:
    print("Sorry to say but you have failed")

if(0<percentage<=30):
    print("Grade: C")
elif(31<percentage<=60):
    print("Grade: B")
elif(61<percentage<=90):
    print("Grade: A")
elif(91<percentage<=100):
    print("Grade: A+")