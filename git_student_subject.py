students = [] 
   
flag = "y"
while (flag == "y"):
    student = {}
    studentName = input("Enter Student Name: ")
    student["name"] = studentName
    subjectFlag = "y"
    # subject list
    subjects = []
    # taking the inputs for marks
    totalMarks = 0
    while (subjectFlag == "y"):
        subject = {}
        subjectName = (input("Please enter the name of the subject"))
        marks = int(input("enter the marks for the subjec"))
        subject["name"] = subjectName
        subject["marks"] = marks
        subjects.append(subject)
        totalMarks = totalMarks+marks
        subjectFlag = input("do you have any other subject data y/n")

