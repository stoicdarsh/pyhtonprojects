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