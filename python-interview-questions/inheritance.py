## Q1. Write a Python program to demonstrate basic single inheritance.
class Animal:
    def speak(self):
        print("Animals make sounds")
class Dog(Animal):
    def bark(self):
        print("Dog barks: Woof! Woof!")
d = Dog()
d.speak()
d.bark()
 # Output:
 # Animals make sounds
 # Dog barks: Woof! Woof!
 #Explanation: Dog inherits from Animal and can use its methods; Dog also defines its own bark method.
 
 
##Q2. Demonstrate constructor inheritance using super().

class Person:
    def __init__(self, name):
        self.name = name
class Student(Person):
    def __init__(self, name, roll):
        super().__init__(name)
        self.roll = roll
    def display(self):
        print(f"Name: {self.name}, Roll: {self.roll}")
s = Student("Sona", 101)
s.display()
 # Output:
 # Name: Sona, Roll: 101
 #Explanation: Student calls the Person constructor using super() to initialize inherited attributes.

##Q3. Demonstrate method overriding in single inheritance.

class Vehicle:
    def info(self):
        print("This is a vehicle")
class Car(Vehicle):
    def info(self):
        print("This is a car")
c = Car()
c.info()
# Output:
 # This is a car
#Explanation: Car overrides the info() method of Vehicle; the child's method is called.
 
 
##Q4. Demonstrate accessing parent method using super().

class Parent:
    def greet(self):
        print("Hello from Parent")
class Child(Parent):
    def greet(self):
        super().greet()
        print("Hello from Child")
c = Child()
c.greet()
 # Output:
 # Hello from Parent
 # Hello from Child
#Explanation: super().greet() invokes the Parent implementation before the Child's message.
 
 
##Q5. Demonstrate inheritance with attributes and methods.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department
    def show(self):
        print(f"Name: {self.name}, Salary: {self.salary}, Department: {self.department}")
m = Manager("Sona", 50000, "IT")
m.show()

 # Output:
 # Name: Sona, Salary: 50000, Department: IT
#Explanation: Manager extends Employee and adds a department attribute and show() method.
 
 
##Q6. Demonstrate basic multiple inheritance.
class A:
    def feature1(self):
        print("Feature 1 from A")
class B:
    def feature2(self):
        print("Feature 2 from B")
class C(A, B):
    def feature3(self):
        print("Feature 3 from C")
obj = C()
obj.feature1()
obj.feature2()
obj.feature3()
 # Output:
 # Feature 1 from A
 # Feature 2 from B
 # Feature 3 from C
#Explanation: Class C inherits from both A and B and can access methods from both parents.
##Q7. Show method resolution order (MRO) in multiple inheritance.

class A:
    def show(self):
        print("A show")
class B(A):
    def show(self):
        print("B show")
class C(A):
    def show(self):
        print("C show")
class D(B, C):
    pass
d = D()
d.show()
print(D.mro())
 # Output:
 # B show
 # [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
#Explanation: Python follows C3 linearization (MRO); D searches B before C because of the inheritance order.
 
 
##Q8. Demonstrate combining functionality from multiple parents.
class Father:
    def skills(self):
        print("Gardening, Programming")
class Mother:
    def skills(self):
        print("Cooking, Art")
class Child(Father, Mother):
    def skills(self):
        Father.skills(self)
        Mother.skills(self)
        print("Sports")
c = Child()
c.skills()
 # Output:
 # Gardening, Programming
 # Cooking, Art
 # Sports
#Explanation: Child explicitly calls each parent's method to combine functionalities.
 
##Q9. Demonstrate multiple inheritance with constructors.
class A:
    def __init__(self):
        print("A initialized")
class B:
    def __init__(self):
        print("B initialized")
class C(A, B):
    def __init__(self):
        super().__init__()
        print("C initialized")
obj = C()
 # Output:
 # A initialized
 # C initialized
 
 
#Explanation: super() with multiple inheritance follows MRO; only A's __init__ runs before C's in this layout.
 
##Q10. Demonstrate diamond problem in multiple inheritance.
class A:
    def show(self):
        print("A show")
class B(A):
    def show(self):
        print("B show")
class C(A):
    def show(self):
        print("C show")
class D(B, C):
    pass
d = D()
d.show()
 # Output:
 # B show

#Explanation: Diamond shape causes potential ambiguity but Python's MRO resolves it, calling B.show() first.
 
##Q11. Demonstrate basic multilevel inheritance.

class Grandparent:
    def feature1(self):
        print("Feature 1 from Grandparent")
class Parent(Grandparent):
    def feature2(self):
        print("Feature 2 from Parent")
class Child(Parent):
    def feature3(self):
        print("Feature 3 from Child")
obj = Child()
obj.feature1()
obj.feature2()
obj.feature3()

 # Output:
 # Feature 1 from Grandparent
 # Feature 2 from Parent
 # Feature 3 from Child
#Explanation: Child inherits features from Parent and Grandparent in a chain.
 
##Q12. Demonstrate constructor chaining in multilevel inheritance.
 
class A:
    def __init__(self):
        print("A init")
class B(A):
    def __init__(self):
        super().__init__()
        print("B init")
class C(B):
    def __init__(self):
        super().__init__()
        print("C init")
obj = C()
 # Output:
 # A init
 # B init
 # C init
#Explanation: Each constructor calls super().__init__(), chaining initializations up the hierarchy.
 
##Q13. Demonstrate data flow in multilevel inheritance.

class A:
    def __init__(self, a):
        self.a = a
class B(A):
    def __init__(self, a, b):
        super().__init__(a)
        self.b = b
class C(B):
    def __init__(self, a, b, c):
        super().__init__(a, b)
        self.c = c
    def show(self):
        print(self.a, self.b, self.c)
obj = C(1, 2, 3)
obj.show()
 # Output:
 # 1 2 3
#Explanation: Values are passed through constructors from top to bottom; attributes persist.
 
##Q14. Demonstrate method overriding in multilevel inheritance.

class A:
    def show(self):
        print("Class A")
class B(A):
    def show(self):
        print("Class B")
class C(B):
    def show(self):
        print("Class C")
obj = C()
obj.show()
 # Output:
# Class C
#Explanation: The lowest-level class's method overrides parent methods in the chain.
 
 
##Q15. Demonstrate real-world multilevel inheritance example.

class Device:
    def power_on(self):
        print("Device powered on")
class Phone(Device):
    def call(self):
        print("Calling feature enabled")
class Smartphone(Phone):
    def browse(self):
        print("Internet browsing enabled")
s = Smartphone()
s.power_on()
s.call()
s.browse()
 # Output:
 # Device powered on
 # Calling feature enabled
 # Internet browsing enabled