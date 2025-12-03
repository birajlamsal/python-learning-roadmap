def repeater(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeater(3)
def hello(name):
    print(f'Hello ,{name}')

hello("Biraj")