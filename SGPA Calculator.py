def findGradeOf(number_of_subjects,list_of_grades_credits):
    dic={"O":10,"A+":9,"A":8,"B+":7,"B":6,"C":5,"F":0,"Ab":0}
    
    sub_grade_points=[]
    for i in list_of_grades_credits:
        sub_grade_points.append(dic[i[0]])
        
    grade_into_credits=[]
    for i in range(number_of_subjects):
        grade_into_credits.append(sub_grade_points[i]*float(list_of_grades_credits[i][1]))
    
    total_credits=0
    for i in range(len(list_of_grades_credits)):
        total_credits+=float(list_of_grades_credits[i][1])
    return sum(grade_into_credits)/total_credits


name=str(input("Enter your Name : "))
roll_no=str(input("Enter your Roll Number : "))
number_of_subjects=int(input("Enter Number of Subjects : "))
print("=============Enter 'Grade' <space> 'Credits'=============")
list_of_grades_credits=[]
for i in range(number_of_subjects):
    list_of_grades_credits.append(list(input("Enter Subject "+str(i+1)+" Grade and Credits : ").upper().split(" "))[:2])

print("=========================================================")
print("*********************SGPA CALCULATOR*********************")    
print("=========================================================")
print("Name          : ",name)
print("Roll Number   : ",roll_no)
print("Final SGPA is : ",findGradeOf(number_of_subjects,list_of_grades_credits))
print("=========================================================")
print("*****Application Developed by Pusthakala Dharan Tej******")
print("############### github id : dharantej1 ##################")
print("######## Thank You ",name," for using this App! ########")
print("=========================================================")
