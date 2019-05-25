def uppercase(func):
    def wrapper():
        original = func()
        modified = original.upper()
        return modified
    return wrapper


@uppercase
def justAFunction():
    return 'hello'



print(justAFunction())