class Person:
    def __init__(self, name, age, spouse, children):
        self.name = name
        self.age = age
        self.spouse = spouse
        self.children = children
    
class Child(Person):
    def __init__(self, name, age, spouse, children, parents):
        super().__init__(name, age, spouse, children)
        self.parents = parents

jim = Person("Jim Brown", 45, None, [None])

suzy = Person("Suzy Brown", 42, jim, [None])

martha = Child("Martha Brown", 18, None, [], [jim, suzy])

jim.spouse = suzy
jim.children[0] = martha
suzy.children[0] = martha