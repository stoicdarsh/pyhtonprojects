while True:
    print("""
1. If Want to add your Data
2. If test from random Data""")
    try:
        test_option=int(input("Enter Option: "))
    except ValueError:
        print("Enter Valid Data")
        continue
    if test_option not in [1,2]:
        print("Enter From Given Options...")
        print()
    else:
        print("Option Accepted")
        print()
        break
if test_option==2:
    students = {"Aman": [85, 90, 78], "Riya": [92, 88, 95], "Zoya": [70, 65, 80]}
    subjects=3
else:
    students={}
    while True:
        try:
            subjects=int(input("Enter Number of Subjects: "))
            break
        except ValueError:
            print("Enter Valid Value")
            print()
    while True:
        name=input("Enter Student Name: ").strip().title()
        marks=[]
        for i in range(subjects):
            while True:
                try:
                    mark=float(input("Enter Marks for subject {i+1}: "))
                    if 0<=mark<=100:
                        marks.append(mark) 
                        break
                    else:
                        print("Enter In Range [0,100]")
                        print()
                except ValueError:
                    print("Enter Valid Data")
                    print()
                    continue
        students[name]=marks
        while True:
            choice=input("Want to add more [Y/N]: ").strip().lower()
            if choice=="y":
                break 
            elif choice=="n":
                break
            else:
                print("Enter From Given Choices...")
        if choice=="n":
            print('STUDENTS')
            for i in students:
                print(f"{i}: {students[i]}")
            print()
            break

#Menu
while True:
    print("""MENU
1. Add Student
2. View all
3. Show topper
4. Grades
5. Remove student
6. Exit""")
    print()
    while True:
        try:
            option=int(input("Enter option: "))
            break
        except ValueError:
            print("Enter Valid Value")
    if option==6:
        print("Goodbye!")
        break

    elif option==1:
        name=input("Enter Name: ").strip().title()
        if name not in students:
            marks=[]
            for i in range(subjects):
                while True:
                    try:
                        mark=float(input("Enter Marks for subject {i+1}: "))
                        if 0<=mark<=100:
                            marks.append(mark) 
                            break
                        else:
                            print("Enter In Range [0,100]")
                            print()
                    except ValueError:
                        print("Enter Valid Value")
                        print()
            students[name]=marks
            print()
        else:
            print("Student Already Exists")
            print()
    elif option==2:
        for i,j in students.items():
            print(f"Name: {i}, Marks: {j}")
        print()

    elif option==3:
        ranks={}
        keys=[]
        for i in students:
            keys.append(i)
            avg=round(sum(students[i])/subjects,2)
            ranks[i]=avg
        values=[v for k,v in ranks.items()]
        print("Topper:",keys[values.index(max(values))])
        print()

    elif option==4:
        for i in students:
            avg=round(sum(students[i])/subjects,2)
            if avg>=85:
                print(i,avg, "A")
            elif avg>=70:
                print(i, avg, "B")
            elif avg>=50:
                print(i,avg, "C")
            else:
                print(i,avg,"F")
        print()

    elif option==5:
        name=input("Enter Student Name: ").strip().title()
        del students[name] #completely delete
        print("Removed Successfully")
        print()
    else:
        print("Enter from the given options")
        print()
    