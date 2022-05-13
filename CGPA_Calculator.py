semesters = ["1-1", "1-2", "2-1", "2-2", "3-1", "3-2", "4-1", "4-2"]
def calculate_CGPA(nos):
    global semesters
    sgpa = []
    for i in range(nos):
        sgpa.append(float(input("Enter the SGPA of " + semesters[i] + " Semester : ")))
    print("=========================================================")
    return sum(sgpa)/len(sgpa)


name=str(input("Enter your Name : "))
roll_no=str(input("Enter your Roll Number : "))
nos=int(input("Enter Number of Semesters : "))
# print("The SGPA of all the semesters till",semesters[nos-1],":",calculate_CGPA(nos))


print("=========================================================")
print("*********************CGPA CALCULATOR*********************")
print("=========================================================")
print("Name          : ",name)
print("Roll Number   : ",roll_no)
print("The CGPA of all the semesters till",semesters[nos-1],":",calculate_CGPA(nos))
print("=========================================================")
print("*****Application Developed by Pusthakala Dharan Tej******")
print("############### github id : dharantej1 ##################")
print("######## Thank You ",name," for using this App! ########")
print("=========================================================")
