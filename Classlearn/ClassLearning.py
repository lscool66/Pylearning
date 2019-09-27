class Preson:
    def __init__(self, name, age = 18):
        self.name = name
        self.age = age

    def showage(self):
        print('{} is {}'.format(self.name,self.age))

a = Preson('tom', 18)
b = Preson('jerry', 19)
b = Preson('jerry', 19)

a.showage()
b.showage()

print(a.__class__, b.__class__)
print(a.__class__.__qualname__, a.__class__.__name__)

# print(isinstance(b, a.__class__))

print(Preson.__dict__)
print(a.__dict__)
print(b.__dict__)
print(a.__dict__['name'])