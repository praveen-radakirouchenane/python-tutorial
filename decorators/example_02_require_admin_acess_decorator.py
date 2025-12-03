from functools import wraps

def admin_access(func):
    @wraps(func)
    def wrapper(user_role):
        if(user_role != 'admin'):
            print("Your access is denied, please contact your admin.")
            return None
        else:
            return func(user_role)
    return wrapper

@admin_access
def login(role):
    print(f"Welcome to the admin portal, and your role is {role}")

#usecase_1
#login("user")

#usecase_2
login("admin")