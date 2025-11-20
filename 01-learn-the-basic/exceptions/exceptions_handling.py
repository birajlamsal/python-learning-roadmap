try:
    number = int(input("Enter a number: "))
    print(1000/number)
except ZeroDivisionError:
     print("You can't divide by zero")
except ValueError:
    print("You can't divide a string")
