from doctest import FAIL_FAST
from importlib.metadata import pass_none

i = 1000
b = 2000
x = 12312.2323
z = "Applee"
good = False
group = [1,3,4,5]

if i < b:
    print(" I is smaller than B")
else:
    print("B is smaller than I")


math_exam = True

if math_exam == False:
    print("Failed in math exam")
else:
    print("Success in math exam")
print(math_exam)