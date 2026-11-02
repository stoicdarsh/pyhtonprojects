#1 Fizz Buzz
tests=[4,6,10,15]
for i in tests:
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
        print("Constraints is [1,100]")

#2 