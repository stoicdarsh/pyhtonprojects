#Answer 1
n=-5
if n>0:
    print("Positive")
elif n<0:
    print("Negative")
else:
    print("Zero")

#Answer 2
sides=(3,3,5)
a,b,c=sides
if a==b==c:
    print("Equilateral")
elif a==b or b==c or a==c:
    print("Isosceles")
else:
    print("Scalene")

#3rd Answer
day_number=3
days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
for i in range(len(days)):
    if day_number==i+1:
        print(f"{days[i]}")

#4th Answer
a=8
op="/"
b=2
if op=="+":
    print(a+b)
elif op=="-":
    print(a-b)
elif op=="*":
    print(a*b)
elif op=="/" and b==0:
    print("Can't divide by zero")
elif op =="/":
    print(a/b)
else:
    print("Invalid operator")

#5th Answer
n=10
sum=0
for i in range(1,n+1):
    if i%2==0:
        sum+=i
print(sum)

#6th Answer
n=5
while n>0:
    print(n,end=" ")
    n-=1
print()

#7th Answer
number=1234
digit_sum=0
while number>0:
    digit_sum+=number%10
    number//=10
print(digit_sum)

#8th Answer
base=3
exponent=4
power=1
for i in range(exponent):
    power*=base
print(power)

#9th Answer
text="banana"
ch="a"
count=0
for i in text:
    if i==ch:
        count+=1
print(count)

#10th Answer
n=4
for i in range(1,n+1):
    print(i*i,end=" ")
print()

#11th Answer
number=4829
digits=[]
while number>0:
    digits.append(number%10)
    number//=10
print(max(digits))

#12th Answer
n=12
for i in range(1,n+1):
    if n%i==0:
        print(i,end=" ")
print()

#13th Answer
n=28
sum=0
for i in range(1,n//2+1):
    if n%i==0:
        sum+=i
if sum==n:
    print("Yes")
else:
    print("No")

#14th Answer
n=7
a,b=0,1
for i in range(n):
    sum=a+b
    print(a,end=" ")
    a=b
    b=sum