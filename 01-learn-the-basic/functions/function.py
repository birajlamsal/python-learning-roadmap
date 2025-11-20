
def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b

def even_odd(num):
    if num % 2 == 0:
        return ("Even")
    else:
        return ("Odd")


print(add(1, 2))
print(sub(1, 2))
print(mul(1, 2))
print(even_odd(1))