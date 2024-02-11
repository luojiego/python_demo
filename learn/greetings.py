import sys
for f in dir(sys):
    print(f)

print in dir(sys)

def say_hi(greeting="Hello", *names, capitalized=False):
    for name in names:
        if capitalized:
            name = name.capitalize()
        print(f"{greeting}, {name}!")

say_hi("Hello", "Michael", "Jordan", "Tiger")
# 使用 *args 作为函数的参数，可以接受任意数量的参数。
# list 转换为 *args，使用 * 号。
say_hi("Hi", *["Tom", "Jerry"])

say_hi("Welcome", "tim", "jerry", "mike", capitalized=True)

# 同其他语言一样，Python 中的函数也可以有默认参数。
# 默认参数必须放在非默认参数的后面。
say_hi("John", "mike", "jerry", "tim")

type(say_hi)

say_hi("Hello", *list(range(1,5)))

def print_args(**names_greetings):
    for name, greeting in names_greetings.items():
        print(f"{greeting}, {name}!")

print_args(Michael="Hello", Jordan="Hi", Tiger="Good morning")

a_dict = {"Michael": "Hello", "Jordan": "Hi", "Tiger": "Good morning"}
print_args(**a_dict)