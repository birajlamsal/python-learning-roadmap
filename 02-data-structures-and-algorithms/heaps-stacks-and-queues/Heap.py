import heapq
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,100000]

print(numbers)
print(heapq.nlargest(2, numbers)[0])
print(heapq.heappop(numbers))