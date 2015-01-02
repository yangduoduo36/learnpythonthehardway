## Animal is-a object (yes, sort of confusing) look at the extra credit
## Parent class
class Animal(object):
    pass

## Child class of Animal class
class Dog(Animal):

    def __init__(self, name):
        ## name of the dog
        self.name = name

## Child class of Animal
class Cat(Animal):

    def __init__(self, name):
        ## name passed to cat class
        self.name = name

## Parent class
class Person(object):

    def __init__(self, name):
        ## name passed to parent class
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

from pprint import pprint

## child class of person
class Employee(Person):

    def __init__(self, name, salary):
        ## ?? hmm what is this strange magic?
        # super returns proxy object that delegates method calls to a parent or sibling class. Useful for accessing inherited methods that have been overriden in a class
        # the init is referring to the parent's init
        super(Employee, self).__init__(name)
        ## sets variable
        self.salary = salary

## Parent object
class Fish(object):
    pass

## Inherits Fish class
class Salmon(Fish):
    pass

## Inherits Fish class
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## satan is-a cat
satan = Cat("Satan")

## mary is-a cat
mary = Person("Mary")

## mary has-a satan
mary.pet = satan

## frank is-a employee
frank = Employee("Frank", 120000)

## frank has-a pet rover
frank.pet = rover

## flipper is-a fish
flipper = Fish()

## crouse is-a salmon
crouse = Salmon()

## harry is-a halibut
harry = Halibut()

pprint(vars(frank))
