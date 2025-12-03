numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers)

for i in range (len(numbers)):
    print(numbers[i])

print("using itterator")

it = iter(numbers)
print(it)
for i in range (len(numbers)):
    print(it.__next__())