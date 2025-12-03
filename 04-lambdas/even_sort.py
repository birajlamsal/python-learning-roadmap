numbers = [1,2,3,4,5,6,7,8,9]
print(numbers)

def apple(y):
    return y % 2==0
even = filter(apple, numbers)
print(even)

# Using lamda
evens = list(filter(lambda x:x%2==0, numbers))
print(evens)