class Descriptor:
    def __get__(self, instance, owner):
        return "Got value"
    def __set__(self, instance, value):
        print(f"Set value {value}")

class MyClass:
    attr = Descriptor()

obj = MyClass()
print(obj.attr)
obj.attr = 42


#context manager defines setup and teardown logic using __enter__ and __exit__ methods.

class MyContext:
    def __enter__(self):
        print("Entering context")
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting context")

with MyContext():
    print("Inside block")

# __slots__ is used to limit the attributes that an object can have, saving memory.

class MyClass:
    __slots__ = ['x', 'y']
    def __init__(self, x, y):
        self.x = x
        self.y = y

obj = MyClass(1,2)
# obj.z = 3  # AttributeError

## Duck typing in python

def quack(obj):
    obj = quack()

class Duck:
    def quack(self): print("quacky...")
class person:
    def quack(self) : print("am quacking like a duck")

import pickle

data = {'x': 1}
s = pickle.dumps(data)
print(pickle.loads(s))