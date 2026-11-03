#1 sum of a list
def list_sum(numbers):
    sum=0
    for i in numbers:
        sum+=i
    return sum
print(list_sum([2,4,6]))

#2 Even or Odd
def count_even_odd(numbers):
    even=0
    odd=0
    for i in numbers:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even,odd
print(count_even_odd([1,2,3,4,5]))

#3 Largest and smallest
def find_min_max(data):
    length=len(data)
    if data[0]<=data[1]:
        min=data[0]
        max=data[1]
    else:
        max=data[0]
        min=data[1]
    for i in range(2,length):
        if data[i]>=max:
            max=data[i]
        if data[i]<=min:
            min=data[i]
    return min,max
print(find_min_max([9,4,2,7]))

#4 Remove Duplicates
def unique_items(items):
    return list(set(items))
print(unique_items([1,2,2,3,3,3]))

#5 Common Elements
def common_elements(set1,set2):
    return set1 & set2
print(common_elements({1,2,3},{2,3,4}))

#6 Word Frequency
def word_count(sentence):
    data=sentence.split()
    dic={}
    for i in data:
        dic[i]=data.count(i)
    return dic
print(word_count("to be or not to be"))

#7 Student Grade
def get_grade(marks_dict):
    new_dict={}
    for key,val in marks_dict.items():
        if val>=80:
            new_dict[key]="A"
        elif val>=60:
            new_dict[key]="B"
        elif val>=40:
            new_dict[key]="C"
        else:
            new_dict[key]="Fail"
    return new_dict
print(get_grade({"Ravi": 85, "Sita": 62, "Amit": 38}))

#8 Default Argument
def power(base,exponent=2):
    return base**exponent
print(power(2,3))

#9 Keyword Argument
def student_info(name,age,city="Lucknow"):
    return f"Name: {name.title()}, Age: {age}, City: {city.title()}"
print(student_info("Darshan", 19, "Uttar pradesh"))
print(student_info(age=19,city="Delhi",name="Nitin"))
print(student_info("Shubham", 19))

#10 Combined Challenges
def analyze_scores(students):
    records={"passed":[],"failed":[],"topper":None}
    for key, val in students:
        marks=[]
        names=[]
        marks.append(val)
        names.append(key)
        if val>=40:
            records["passed"].append(key)
        else:
            records["failed"].append(key)
    records["topper"]=f"{names[marks.index(max(marks))]}"
    return records
print(analyze_scores([("Ravi", 85), ("Sita", 62), ("Amit", 38)]))