# #1st Oldest Age
# x,y,z=int(input("Enter age for x: ")),int(input("Enter age for y: ")),int(input("Enter age for z: "))
# print(max((x,y,z)))

# #2nd C to F
# c=float(input("Enter Celsius: "))
# print((9/5)*c+32)

# #3rd Swap
# a,b=int(input("Enter a: ")),int(input("Enter b: "))
# print("Before:",a,b)
# b,a=a,b
# print("After:",a,b)

# #4th Digit Sum
# x=int(input("Enter x: "))
# sum=0
# while x>0:
#     sum+=(x%10)
#     x//=10
# print("Sum:",sum)

# #5th Palindrome numebr
# x=int(input("Enter x: "))
# y=int(str(x)[::-1])
# print("Reversed:",y)
# if x==y:
#     print("Palindrome")
# else:
#     print("Not a plaindrome")

# #6th Odd Even Check
# x=int(input("Enter x: "))
# print("Even") if x%2==0 else print("Odd")

# #7th Leap year 
# x=int(input("Enter Year: "))
# print("Leap") if x%4==0 else print("Not Leap")

# #8th Eucllidean Distance
# x1,x2=int(input("Enter x1: ")),int(input("Enter x2: "))
# y1,y2=int(input("Enter y1: ")),int(input("Enter y2: "))
# print("Distance:",((x2-x1)**2+(y2-y1)**2)**0.5)

# #9th Triangle Formation check
# x,y,z=int(input("Enter Angle x: ")),int(input("Enter Angle y: ")),int(input("Enter Angle z: "))

# for i in range(3):
#     if x<y+z:
#         pass
#     else:
#         print("Can't form Triangle")
#         break
#     if y<x+z:
#         pass
#     else:
#         print("Can't form Triangle")
#         break
#     if z<x+y:
#         pass
#     else:
#         print("Can't form Triangle")
#         break
# else:
#     print("Can form triangle")

# #10th Profit loss
# cost=float(input("Enter Cost Price: "))
# sell=float(input("Enter Selling Price: "))
# if sell>cost:
#     print(f"{sell-cost} Profit")
# elif cost>sell:
#     print(f"{cost-sell} loss")
# else:
#     print("Niether Loss nor Profit")

# #11th Simple Interest
# p,r,t=float(input("Enter Base Price: ")),float(input("Enter Interest Rate: ")),float(input("Enter Interest Time Period: "))
# print("Interest Price:",p*r*t)

# #12th Cost/Volume of Cylinder
# r,h=float(input("Enter Cylinder Radius in cm: ")),float(input("Enter Cylinder Height in cm: "))
# v=3.14*r**2*h*0.001
# print("Cost:",v*40)

# #13th Divisible from 6
# x=int(input("Enter Number: "))
# print(f"{x} is Divisible by 3 and 6") if x%6==0 else print("Not divisible")

# #14th 
# t,h=int(input("Enter Temperature: ")),int(input("Enter Humidity: "))
# if t>=30 and h>=90:
#     print("Hot and Humid")
# elif t>=30 and h<90:
#     print("Hot")
# elif t<30 and h>=90:
#     print("Cool and Humid")
# else:
#     print("Cool")

# #15th sum of digit squares
# x=int(input("Enter Number: "))
# sum=0
# while x>0:
#     sum+=(x%10)**2
#     x//=10
# print("Sum:",sum)

# #16th &17th  Narcisistic / Armstrong Number
# x=int(input("Enter Number: "))
# digits=len(str(x))
# sum=0
# while x>0:
#     sum+=(x%10)**digits
#     x//=10
# print("Narcistic and Armstrong") if x

# #18th Tax Slabs
# before=float(input("Enter Salary: "))
# if before<100000:
#     print(f"{int(before/1000)}k")
# elif before<=500000:
#     print(before-before*0.18)
# elif before<=1000000:
#     print(before-before*.28)
# elif before<=2000000:
#     print(before-before*.38)
# else:
#     print(before-before*0.48)

# #19th Conversion
# while True:
#     print("""1. cm to ft
#     2. km to miles
#     3. USD to INR
#     4. Exit""")
#     option=int(input("Enter option: "))
#     if option==4:
#         break
#     elif option==1:
#         cm=float(input("Enter cm: "))
#         print("Ft:",cm*0.0328084)
#     elif option==2:
#         km=float(input("Enter km: "))
#         print("miles:",km*0.621371)
#     elif option==3:
#         usd=float(input("Enter USD: "))
#         print("INR:",usd*94.91)
#     else:
#         print("chose from given choices")

# #20th dogs and chickens
# heads=int(input("Enter Number of Heads: "))
# legs=int(input("Enter Numebr of Legs: "))
# print("Number of Dogs:",(legs-2*heads)/2) if (legs-2*heads)%2==0 else print("Not defined")
# print("Number of Chickens:",(4*heads-legs)/2) if (4*heads-legs)%2 else print("Not defined")

#21st Already done 

# #22nd N sum
# n=int(input("Enter N: "))
# sum=0
# for i in range(n+1):
#     sum+=i
# print("Sum:",sum)

#23rd too easy

# #24 factorial
# total=1
# n=int(input("Enter N: "))
# for i in range(1,n+1):
#     total*=i
# print("Factorial:",total)

# #25th first n odd numbers
# n=int(input("Enter number of odds: "))
# for i in range(2*n):
#     if i%2!=0:
#         print(i,end=" ")

#26th prime check
n=int(input("Enter Number: "))
for i in range(2,(n//2)+1):
    if n%i==0:
        print("Not a prime Number")
        break
else:
    print("Prime Number")