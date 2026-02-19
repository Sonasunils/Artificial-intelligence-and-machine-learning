# class human :
#     legs = 2
#     nose = 1
#     def walking(self):
#       print("can walk")
#     def talking(self) :
#       print("can talk")
# appu = human ()
# print(appu.legs)
# appu.walking()
# ammu = human ()
# print(ammu.nose)
# class room :
#     length = 0
#     breadth = 0 
#     height = 7 
#     def calculate (self ):
#         print(self. length * self. breadth * self.height) 
# studyroom = room ()
# studyroom.length = 42.5
# studyroom.breadth = 0.8
# studyroom.calculate()        
# class student:
#     sname = "arjun"
# si  = student ()
# si.rno = 56
# p2 = student ()
# p2.sname = "arun"
# p2.rno = 79
# print("student name:",si.sname) 
# print("student rno :",si.rno) 
# print("student name:",p2.sname)
# print("student rno :",p2.rno)
# class calculator :
#     def add (self,x,y):
#         return x+y
#     def sub (self,x,y ):
#         return x - y    
#     def  mul (self ,x,y):
#         return x * y
#     def div (self ,x,y):
#         if y ==0:
#             print("not possible")
#         else:    
#             return x // y
# my_calculator = calculator()
# print(my_calculator.add (5,3))
# print(my_calculator.sub (10,4))
# print(my_calculator.mul (2,6))    
# print(my_calculator.div (8,0))    
# class greet :
#     def greeter(self,name):
#         print("hiii" ,name)
# new = greet()
# new.greeter("sona")
# new.greeter("jack")
# class calculator:
#     def add (self,x,y):
#         return x + y
#     def sub (self,x,y):
#         return x - y
# my_cal = calculator()
# print(my_cal.add(7,7))
# print(my_cal.sub(7,7))
# class product :
#     def __init__(self,name,price):
#         self.name = name 
#         self.price = price
#     def display (self):
#         print(self.name)
#         print(self.price)
# p1 = product ("computer",20000)
# p2 = product ("table",2000)            
# p1.display()
# p2.display()       
# class BankAccount:
#     def __init__(self, account_number, account_holder_name, balance=0):
#         self.account_number = account_number
#         self.account_holder_name = account_holder_name
#         self.balance = balance

#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#             print(f"Deposited ${amount}. New balance: ${self.balance}")
#         else:
#             print("Invalid deposit amount.")

#     def withdraw(self, amount):
#         if 0 < amount <= self.balance:
#             self.balance -= amount
#             print(f"Withdrew ${amount}. New balance: ${self.balance}")
#         else:
#             print("Insufficient funds or invalid withdrawal amount.")

#     def get_balance(self):
#         return self.balance

#     def get_account_info(self):
#         return f"Account Number: {self.account_number}\nAccount Holder: {self.account_holder_name}\nBalance: ${self.balance}"


# # Example Usage
# account1 = BankAccount(1234567890, "John Doe", 1000)
# print(account1.get_account_info())

# account1.deposit(500)
# account1.withdraw(200)
# print("Current Balance:", account1.get_balance())

# account1.withdraw(1500)  # Test insufficient funds
# account1.deposit(-100)   # Test invalid deposit  