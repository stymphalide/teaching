
import random

random.random()

print("hello world")

my_number = 1
my_number = "hello"
print(my_number)

my_list = [1,2,3,4,"string", my_number]
my_list[0]
my_list[-1]
print(my_list)
print(my_list[1:6:2])

my_list[2] = 5

my_tuple = (1,2,3)
#my_tuple[2] = 5

my_dict = {"key" : "value", "key_2" : 3}
my_dict["key"] # ==> value
print(my_dict)

my_bool = True
my_bool = not my_bool # ==> False

if my_bool:
    print("hello")
elif not my_bool:
    print("will not be printed 1")
else:
    print("will not be printed 2")

for e in my_list:
    print(e)

def my_func(arg1=10):
    print(arg1)

my_func(5) # ==> prints 5
my_func()  # ==> prints 10

class MyClass(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def my_method(self):
        print(self.a)

my_object = MyClass(2, 4)

my_object.my_method() # ==> 2
my_object.a = 6
my_object.my_method() # ==> 6


my_input = input("Type something: ")

print(type(my_input))
print(my_input)

my_int = int(my_input)
print(type(my_int))
print(my_int)




