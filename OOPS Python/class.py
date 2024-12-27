class Person: ## blueprint
    def __init__(self, name, age): ## dunder method or magic : self caall, __init__: runs when object create
        self.name = name
        self.age = age

    # def __init__(self):
    # pass
    # pass

Avipsha = Person("Avipsha", 19)

print(Avipsha.name)
print(Avipsha.age)