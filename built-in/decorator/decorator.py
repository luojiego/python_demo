def a_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

def a_func():
    print("Hi, I am a_func!")

a_func()
a_decorator(a_func)

@a_decorator
def b_func():
    print("Hi, I am b_func!")

b_func()

def an_output():
    return "The quick brown fox jumps over the lazy dog."

print(an_output())

def uppercase(func):
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result
    return wrapper

@uppercase
def an_output():
    return "The quick brown fox jumps over the lazy dog."

print(an_output())

def strong(func):
    def wrapper():
        return "<strong>" + func() + "</strong>"
    return wrapper

@strong
@uppercase
def an_output():
    return "The quick brown fox jumps over the lazy dog."

print(an_output())

@uppercase
@strong
def an_output():
    return "The quick brown fox jumps over the lazy dog."

print(an_output())

def say_hi(greeting, name=None):
    return f"{greeting}! {name}."

print(say_hi("Hello", "Michael"))

def trace(func):
    def wrapper(*args, **kwargs):
        print(f"TRACE: calling {func.__name__}() with {args}, {kwargs}")
        original_result = func(*args, **kwargs)
        print(f"TRACE: {func.__name__}() returned {original_result}")
        return original_result
    return wrapper

@trace
def say_hi(greeting, name=None):
    return f"{greeting}! {name}."

print(say_hi("Hello", "Michael"))