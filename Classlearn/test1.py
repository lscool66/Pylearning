
class Person:

    def __init__(self):
        pass

    @classmethod
    def classs_method(cls):
        print('{0.__name__} ({0})'.format(cls))
        cls.height = 170

    @staticmethod
    def static_method():
        print(Person.height)

Person.classs_method()
Person.static_method()
print(Person.__dict__)