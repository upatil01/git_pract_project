subjects=[]
def taking_inputs(subjects):
    flag = "y"
    while (flag == "y" ):
        subject = {}
        subjectName= input("please input name of subject: ")
        subjectMarks=int(input("please enter marks : "))
        subject["Name"]=subjectName
        subject["marks"]=subjectMarks
        subjects.append(subject)
        flag = input("Do you have any other subject to add y/n")
    return subjects
taking_inputs(subjects)
print (subjects)

