class numbers:
    def __init__(self):
        self.numbers = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.numbers <= 10:
            val = self.numbers
            self.numbers += 1
            return val
        else:
            raise StopIteration

values = numbers()
print(values)

for i in values:
    print(i)