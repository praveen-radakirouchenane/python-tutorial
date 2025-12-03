from functools import wraps

def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Start of the function: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"End of the function: {func.__name__}")
        return result
    return wrapper

@logger
def call_logger(type, status="yes"):
    print(f"I am going to call the wrapper with this {type} function and approval status is {status}")


call_logger("Hello world")