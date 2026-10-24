#1st Answer
subjects=["Math","Physics"]
subjects.append("Chemistry")
subjects.append("Biology")
print(subjects, len(subjects))

#2nd Answer
subjects=["Math","Physics"]
electives=["Art","Music"]
subjects.append(electives)
print(subjects, len(subjects))
subjects.remove(electives)
subjects.extend(electives)
print(subjects,len(subjects))

#3rd Answer
subjects=["Math","Physics","Chemistry"]
subjects.insert(1,"Biology")
subjects.insert(0,"English")
subjects.insert(100,"Computer")
print(subjects)

#4th Answer
marks=[85,90,78,90,88]
marks.remove(90)
print(marks)
marks.remove(78)
print(marks, len(marks))

#5th Answer
subjects=["Math","Physics","Chemistry","Biology"]
last,first,middle=subjects.pop(),subjects.pop(0),subjects.pop(1)
print(last,first,middle)
print(subjects,len(subjects))

#6th Answer
subjects=["Math","Physics","Chemistry"]
backup=subjects.copy()
subjects.clear()
print(subjects,len(subjects))
print(backup,len(backup))

#7th Answer
backup.remove("Chemistry")
a=backup.copy()
b=a
c=a.copy()
b.append("Chemistry")
c.append("Biology")
print(a,b,c,sep="\n")
print(a is b, a is c)

#8th Answer
marks=[85,90,78,90,88,90]
print(marks.count(90))
print(marks.count(100))
print((marks.count(90)*100//len(marks)))

#9th Answer
print(marks.index(90))
print(marks.index(90,marks.index(90)+1))
print(marks.index(90,marks.index(90,marks.index(90)+1)+1))

#10th Answer
backup.append("Chemistry")
subjects=backup
backup=subjects[:]
print(subjects.reverse())
print(subjects)
print(backup)

#11th Answer
marks=[85,90,78,92,88]
marks.sort()
print(marks)
marks.sort(reverse=True)
print(marks)
print(marks.sort())  #Sort always returns None 

#12th Answer
names=["Priya","aman","Rahul","neha","Om"]
names.sort()
print(names)
names.sort(key=str.lower)
print(names)
names.sort(key=len)
print(names)

#13th Answer
marks=[85,90,78,92]
cpy=sorted(marks,reverse=True)
print(cpy)
print(marks)
marks.sort(reverse=True)
print(marks)

#14th ANswer
subjects=["Math","Physics"]
subjects.append("Chemistry")
subjects.insert(1,"Biology")
subjects.extend(["English","History"])
subjects.remove("Physics")
last,first=subjects.pop(),subjects.pop(0)
print(subjects)
print(last,first,len(subjects))

#15th Answer
marks=[85,90,78,92,88]
rev=marks.copy()
rev.sort(reverse=True)
print(rev)
print(marks)
print(rev[:3],rev.index(88))

#16th Answer
semesters="Fall","Winter","Spring","Summer"
print(len(semesters),type(semesters))
print(semesters[0],semesters[-1])
print("Winter" in semesters, "Monsoon" in semesters)

#17th Answer
days="Mon","Tue","Wed","Thu","Fri","Sat","Sun"
print(days[:3],days[-2:],days[2:5],days[::-1],days[::2],sep="\n")

#18th Answer
marks=85,90,78,90,88,90
print(marks.count(90))
print(marks.count(100))
print(marks.count(90)*100//len(marks))

#19th Answer
print(marks.index(90))
print(marks.index(90,marks.index(90)+1))
print(marks.index(90,marks.index(90,marks.index(90)+1)+1))


#20th Answer
days="Mon","Tue","Wed"
print(days+("Thu","Fri"))
print(days+days)
print(days+("Sat",))
print(len(days)*3)

#21th Answer
x=("Fall")
y=("Fall",)
z=tuple("Fall")
print(type(x),len(x))
print(type(y),len(y))
print(z,len(z))

#22th Answer
record="Aman",20,"CSE",8.7
name,age,branch,cgpa=record
print(name,age,branch,cgpa)
name,branch=branch,name
print(name, branch)

#23th Answer
semesters=("Fall","Winter","Spring")
semesters=list(semesters)
semesters[1]="Autumn"
semesters.append("Summer")
semesters.remove("Spring")
semesters=tuple(semesters)
print(semesters,len(semesters))

students=(("Aman",88),("Priya",92),("Rahul",75))
print(students[1][0],students[1][1])
print(students[-1][1])
new=students[:2]+(("Neha",95),)
print(new)
print(len(new),new[-1][1])

#25th Answer
marks=85,90,78,92,88
print(min(marks),max(marks),sum(marks))
print(round(sum(marks)/len(marks),2))
print(sorted(marks))
print(tuple(sorted(marks,reverse=True)))

#26th Answer
marks=85,90,78,90,85
pairs=(("Aman",88),("Priya",92))
mark=list(marks)
mark.append(95)
print(tuple(mark))
print(sorted(set(marks)))
dic={pairs[0][0]:pairs[0][-1],pairs[-1][0]:pairs[-1][-1]}
print(dic)

#27th Answer
seats={}
seats[(1,"A")]="Aman"
seats[(1,"B")]="Priya"
seats[(2,"A")]="Rahul"
print(seats)
print(seats[(1,"B")],len(seats))
print(list(seats.keys()))

#28th Answer
classes={"CS101","CS102","CS103","CS101"}
print(len(classes),type(classes))
print("CS102" in classes, "CS104" not in classes)
print(sorted(classes))

#29th Answer
classes={"CS101","CS102"}
classes.add("CS103")
classes.add("CS101")
print(sorted(classes),len(classes))

#30th Answer
classes={"CS101"}
letters=set()
classes.update(["CS102","CS103"])
classes.update({"CS104","CS102"})
print(sorted(classes),len(classes))
letters.update("abc")
print(sorted(letters))

#31st Answer
classes={"CS101","CS102","CS103"}
classes.remove("CS102")
classes.discard("CS999")
classes.discard("CS103")
print(sorted(classes),len(classes))

#32nd Answer
nums={1,2,3,4,5}
taken=nums.pop()
print(taken)
print(sorted(nums),len(nums))

#33rd Answer
classes={"CS101","CS102","CS103"}
back=classes.copy()
classes.clear()
print(classes,len(classes))
print(sorted(back),len(back))

#34th Answer
a={"CS101","CS102"}
alias=a
duplicate=a.copy()
alias.add("CS103")
duplicate.add("CS999")
print(sorted(a),sorted(duplicate),sep="\n")
print(a is alias, a is duplicate)

#35th Answer
morning={"Aman","Priya"}
evening={"Priya","Karan"}
print(sorted(morning.union(evening)))
print(sorted(morning|evening))
print(sorted(morning.union(["Neha","Aman"])))
print(sorted(morning))

#36th Answer
morning.add("Rahul")
evening.add("Rahul")
print(sorted(morning.intersection(evening)))
print(sorted(morning&evening))
print(len(morning.intersection(evening)))

#37th Answer
morning={"Aman","Priya","Rahul"}
evening={"Priya","Karan"}
print(sorted(morning.difference(evening)))
print(sorted(evening.difference(morning)))
print(sorted(morning-evening),sorted(evening-morning))


#38th Answer
day1=morning.copy()
day2=evening.copy()
print(sorted(day1.symmetric_difference(day2)))
print(sorted(day1^day2))
print(len(day1^day2))

#39th Answer
club={"Aman","Priya"}
batch={"Aman","Priya","Rahul","Neha"}
guests={"Karan"}
print(club.issubset(batch))
print(batch.issuperset(club))
print(club.isdisjoint(guests))
print(club <= batch, batch>=club)

#40th Answer
a={"CS101","CS102"}
b={"CS101","CS103"}
print(sorted(a.union(b)),sorted(a))
b.update(b)
print(sorted(b),len(b))

#41st Answer
enrolled={"Aman","Priya","Rahul"}
attended={"Priya","Rahul","Karan"}
enrolled.intersection_update(attended)
print(sorted(enrolled),len(enrolled))
print(sorted(attended))

#42nd Answer
enrolled={"Aman","Priya","Rahul"}
dropped={"Priya"}
enrolled.difference_update(dropped)
print(sorted(enrolled),len(enrolled))
print(sorted(dropped))

#43rd Answer
day1={"Aman","Priya","Rahul"}
day2={"Priya","Karan"}
day1.symmetric_difference_update(day2)
print(sorted(day1),len(day1))
print(sorted(day2))

#44th Answer
rolls=[101,105,101,107,105,109,101]
print(len(set(rolls)))
print(len(rolls)-len(set(rolls)))
print(sorted(set(rolls)))
print(tuple(sorted(set(rolls))[:3]))

#45th Answer
math_set={"Aman","Priya","Rahul"}
physics_set={"Priya","Rahul","Karan"}
chem_set={"Priya","Neha"}
print(sorted(math_set & physics_set & chem_set))
print(len(math_set | physics_set | chem_set))
print(sorted((math_set-physics_set-chem_set)^(physics_set-math_set-chem_set)^(chem_set-physics_set-math_set)))

#46th Answer
student={"name":"Aman","roll_no":101,"branch":"CSE"}
print(list(student.keys()))
print(list(student.values()))
print(list(student.items()))
print(student.items())

#47th Answer
student={"name":"Aman","branch":"CSE"}
print(student.get("branch"))
print(student.get("cgpa"))
print(student.get("cgpa","Not avilable"))
print(student,len(student))

#48th Answer
student={"name":"Aman","cgpa":8.7}
print(student.setdefault("cgpa",0.0))
print(student.setdefault("hostel","Block A"))
print(student) #setdefault adds a new key:value hostel bcz it isn't exist before

#49th Answer
student.popitem()
student.update({"cgpa":9.1,"branch":"CSE"})
print(student)
student.update(hostel="Block A",cgpa=9.5)
print(student,len(student))

#50th Answer
student={"name":"Aman","roll_no":101,"branch":"CSE"}
print(student.pop("roll_no"))
print(student.pop("cgpa","No such key"))
print(student,len(student))

#51st Answer
student={"name":"Aman","roll_no":101,"branch":"CSE"}
print(student.popitem())
print(student.popitem())
print(student,len(student))

#52nd Answer
student={"name":"Aman","roll_no":101}
back=student.copy()
student.clear()
print(student,len(student))
print(back,len(back))

#53rd Answer
marks={"Math":90,"Physics":78}
alias=marks
duplicate=marks.copy()
alias["Chemistry"]=92
duplicate["English"]=85
print(marks,duplicate,marks is alias,marks is duplicate,sep="\n")

#54th Answer
subjects=["Math","Physics","Chemistry"]
attendance = dict.fromkeys(subjects,0)
print(attendance)
print(dict.fromkeys(subjects))
print(len(attendance),list(attendance.keys()))

#55th Answer
shared=dict.fromkeys(["Aman","Priya"],[])  #frpmkeys() store same object against every key
shared["Aman"].append(88)  
print(shared)  
shared={"Aman":[],"Priya":[]} #dic created through manual typing separate list each time
shared["Aman"].append(88)
print(shared)

#56th Answer
student={"name":"Aman","roll_no":101}
k,v=student.keys(),student.values()
print(list(k),list(v))
student["cgpa"]=8.7
print(list(k),list(v))
print(len(k))

#57th Answer
student={"name":"Aman"}
student.update({"roll_no":101,"branch":"CSE"})
student.setdefault("cgpa",8.7)
student.setdefault("branch","ECE") #branch here will be unaffected
student.pop("roll_no")
print(student,len(student),sep="\n")
print(list(student.keys()),list(student.values()))

#58th Answer
marks={"Aman":[88,92]}
marks["Aman"].append(79)
marks.setdefault("Priya",[95])
print(marks)
print(len(marks["Aman"]),sum(marks["Aman"]))
print(marks.get("Rahul",[]))

#59th Answer
records=[{"name":"Aman","cgpa":8.7},{"name":"Priya","cgpa":9.1}]
print(records[1]["name"])
records[0].update(cgpa=8.9,branch="CSE")
print(records[0])
records.append({"name":"Rahul","cgpa":7.5})
print(len(records),records[-1].get("branch","Not Set"))

#60th Answer
subjects=["Math","Physics","Chemistry"]
register=dict.fromkeys(subjects,0)
register.update(Math=42,Physics=38,Chemistry=45)
print(register)
print(sum(register.values()),max(register,key=register.get))
print(sorted(register.items()))