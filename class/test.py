"""
#1st Question
cgpa=int(input("Enter CGPA: "))
attendance=int(input("Enter Attendance: "))
if cgpa>=8 and attendace>=90:
    print("Scholar")
else:
    print("Not a Scholar")
print("Tasks Completed")
"""
"""#2nd Qeustion
battery=int(input("Enter Battery: "))
if battery==100:
    print("FULLY CHARGED")
elif battery<5:
    print("PUT ON CHARGER")
elif battery<20:
    print("LOW BATTERY")
else:
    print("MEDIUM CHARGED")
"""

#3rd Question
password="py2026"
"""if password == "sitare@123":
    print("Login Succesfully")
else:
    print("Wrong Password")"""

"""#Diff Question
for i in range(2,-1,-1):
    e=input("Enter Password: ")
    if e==password:
        print("Succesful")
        break
    else:
        print(f"{i} chance remaining")"""

#3rd Answer
unit=int(input("Enter Unit: "))
if unit<=500:
    print(f"{unit}* 8 per unit = ${unit*8}")
else:
    print(f"{unit}* 12 per unit = ${unit*12}")



