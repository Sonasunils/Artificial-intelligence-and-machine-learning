# class student :
#     student_count = 0
#     def __init__(self,rollno, name, course):
#         self.rollno = rollno
#         self.name = name 
#         self.course = course
#         student.student_count += 1
#     def display_count(self):
#         print("total students",student.student_count)
#     def display_student(self):
#         print("roll no :",self.rollno)
#         print('name:',self.name)
#         print("course:",self.course)
# st1 = student(1,"arjun","cs")
# st2 = student(2,'ashwin',"cs")
# st1.display_student()
# st2.display_student()
# st2.display_count()
# class product:
#     count = 1 
#     def __init__(self,name,price):
#         self.name= name
#         self.price = price 
#         self.count = product.count

#     def display (self):
#         print(self.name) 
#         print(self.price)
#         print(self.count) 
# p1 = product('computer ',20000)
# p2 = product ("table ",2000)
# p1.display()   
# p1.display()
# p2.display()
# del p1
# # print("deleting p1")  
# # del p2
# # print("deleting p2")  
# class text :
#     def __init__(self):
#         self.__price = "private member"
#         self._prot = "protected member "
#         self.pub = "public member"
#     def display (self):
#         print('inside class')
#         print(self.__price) 
#         print(self._prot)
#         print(self.pub)
# t = text ()
# t.display()
# print("outside class") 
# # print(t.pub)
# # print(t._prot)
# print(t.__price)      
# class greeter :
#     def greet (self,name):
#         print(f"hello {name}")
# g = greeter()
# g.greet("anu")
# class calculator :
#     def calculate (self,a,b):
#         return a + b
#     def sub (self,a,b):
#         return a - b
# cal = calculator()
# print("sum :",cal.calculate(5,6))
# print("difference :",cal.sub(10,1))
# class employee :
#     def __init__(self,name,id,department ):
#         self.name = name
#         self.id = id
#         self.department = department
#     def display(self):
#         print(f"name :{self.name}") 
#         print(f"Id :{self.id}")   
#         print(f"department :{self.department}")
# emp = employee("Arya Stark",25336,"data analytics")
# emp1 = employee("Samwell Tarly",734634676,"manager")
# emp2 = employee("Jon Snow",1,"CEO")
# emp.display()
# emp1.display()
# emp2.display()