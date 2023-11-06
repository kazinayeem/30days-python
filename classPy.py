class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
         return f"{self.name}({self.age})"

    def myfun(self):
        return f"my name is {self.name} and my age is ({self.age})"


p1 = Person("John", 36)
p2 = Person("John1", 37)

print(p1)
print(p1.myfun())
