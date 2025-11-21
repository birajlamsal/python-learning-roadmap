class Queue:
    def __init__(self):
        self.apple = [10 , 20 , 40]   # queue storage

    def enqueue(self, value):
        self.apple.append(value)

    def dequeue(self):
        if len(self.apple) == 0:
            return "Queue is empty!"

        front = self.apple[0]
        self.apple = self.apple[1:]
        return front



q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print(q.apple)

print(q.dequeue())
print(q.apple)

print(q.dequeue())
print(q.apple)

print(q.dequeue())
print(q.apple)

print(q.dequeue())
