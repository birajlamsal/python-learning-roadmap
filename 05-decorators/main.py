def main_function(func):
    def wrapper():
        apple = 69
        print(apple)
        return func()
    return wrapper

@main_function
def random_function():
    print(" Apple pie ")

random_function()
