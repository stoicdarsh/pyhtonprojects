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

#4 remove duplicate
