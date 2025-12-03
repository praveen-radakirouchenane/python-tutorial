from functools import wraps
def hello_decorator(func):
    
    @wraps(func)
    def wrapper():
        print("Before Decorator")
        func()
        print("After decorator")
    return wrapper


@hello_decorator
def call_decorator():
    print('Hi Decorator!!!')

call_decorator()
print(call_decorator.__name__)