#1 Fizz Buzz
i=int(input("Enter a Number: "))
if 1<=i<=100:
    pattern=[]
    for j in range(1,i+1):
        if j%3==0 and j%5==0:
            pattern.append("FizzBuzz")
        elif j%3==0:
            pattern.append("Fizz")
        elif j%5==0:
            pattern.append("Buzz")
        else:
            pattern.append(j)
    print(pattern)
else:
    print("Constraint is [1,100]")

#2 Palindrome Number
x=int(input("Enter a Number: "))
if -1000000<=x<=1000000:
    x=str(x)
    if x[::-1]==x:
        print(True)
    else:
        print(False)
else:
    print("Constraint is [-1000000,1000000]")

#3 Contains Duplicate
tests=[[5,6,7],[4,4],[9,8,7,6,5,9],[1],[10,20,30,40,50,10]]
for lst in tests:
    if 1<=len(lst)<=100:
        print(not len(lst)==len(set(lst)))
    else:
        print('Length is out of constraint[1,100]')

#4 Two sum
tests=[([1,5,8,3],11),([10,2,7,15],9),([6,4,9,2],8),([-3,4,3,90],0)]
for lst,target in tests:
    length=len(lst)
    if 2<=length<=100:
        check=False
        for i in range(length):
            for j in range(i+1,length):
                if lst[i]+lst[j]==target:
                    print(i,j)
                    check=True
                    break
            if check:
                break
    else:
        print("Length is out of constraint")

#5 Best Time to buy and Sell Stock
tests=[[2, 4, 1], [3, 3, 5, 0, 0, 3, 1, 4], [1, 2, 3, 4, 5], [5], [10, 9, 8, 12]]
for lst in tests:
    length=len(lst)
    if 1<=length<=100:
        max=0
        for i in range(length):
            for j in range(i+1,length):
                if lst[j]-lst[i]>=max:
                    max=lst[j]-lst[i]
        print(max)
    else:
        print("length is out of constraint")

#6 Roman to integer
data={"I": 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D": 500, "M" : 1000}
roman=list(input("Enter Roman Number: ").strip())
if 1<=len(roman)<=15:
    list=[data[intgr] for intgr in roman]
    sum=list[0]
    for i in range(1,len(list)):
        if list[i]<=list[i-1]:
            sum+=list[i]
        else:
            sum+=list[i]-2*list[i-1]
    print(sum)
else:
    print("Out of Constraint[1,15]")