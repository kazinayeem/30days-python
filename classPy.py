class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
         return f"{self.name}({self.age})"

    def myfun(a):
        return f"my name is {a.name} and my age is ({a.age})"


p1 = Person("John", 36)
p2 = Person("John1", 37)

print(p1)
print(p1.myfun())
