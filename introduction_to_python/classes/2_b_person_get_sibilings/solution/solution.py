from operator import itemgetter, attrgetter, itemgetter

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
    
    def get_siblings(self):
        siblings = []
        for parent in self.parents:
            siblings.extend(parent.children)
        siblings = list(dict.fromkeys(siblings))      
        siblings.remove(self)
        siblings = sorted(siblings, key=attrgetter('age'))
        siblings_names = [sib.name for sib in siblings]
        return siblings_names      
        
        
        # siblings = []
        # for parent in self.parents:
        #     siblings = list(set(siblings) | set(parent.children))
        # siblings.remove(self)
        # siblings = sorted(siblings, key=attrgetter('age'))
        # siblings_names = [sib.name for sib in siblings]
        # return siblings_names

# Jonny = Person("Jonny", 32, None, [])
# Beth = Person("Beth", 28, Jonny, [])
# Jonny.spouse = Beth
# Max = Child("Max", 5, None, [], [Jonny])
# Annie = Child("Annie", 10, None, [], [Beth])
# Ron = Child("Ron", 7, None, [], [Beth, Jonny])
# Jonny.children.extend([Max, Ron])
# Beth.children.extend([Annie, Ron])

# Ron.get_siblings()