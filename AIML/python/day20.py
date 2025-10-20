# a =int(input("enter a number "))
# b =int(input("enter a number"))
# f = a+b,a-b,a*b,a/b
# print(f)
# a = 2 
# d = 6
# temp = a
# a  =d 
# d = temp
# print(a ) 
# print(d)
# f ="hello world "
# print(f[2:5])
# def rev (n):
#     rev  = 0
#     while n != 0 :
#         digit = n % 10
#         rev =  rev * 10 + digit 
#         n =  n // 10
#     return rev  
# n = int(input("enter  a number")) 
# p = rev (n)
# print(p) 
# def prime (n):
#     count = 0
#     for i in range (1 ,n + 1 ):
#         if n % i == 0:
#             count += 1
#             if count == 2 :
#                 print("prime")
#             else :
#                print("not prime ")
# n =int(input("enter a number "))
# sum = 0 
# temp = n 
# while n > 0 :
#     digit =  n % 10 
#     sum += digit ** 3 
#     n = n // 10 
# print(sum )
# if sum == temp :
#     print("amstrong")
# else :
#     print("not amstrong")
# def factorial (n):
#     if n ==0 :
#         return 1 
#     else :
#         return n * factorial (n - 1)
# print(factorial(5))
# def fibinocci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else :
#         return fibinocci (n - 1) + fibinocci (n - 2) 
# f =fibinocci(4)
# print(f)
# n =int(input("enter a number "))
# if n > 0 :
#     print("positive")
# elif  n < 0:
#     print("negtive")
# else :
#     print(0)
# class Bank_account:
#     def __init__(self,account_number,account_holder,balance = 0):
#         self.account_number = account_number
#         self.account_holder = account_holder
#         self.balance =balance
#     def deposit(self,amount):
#         if amount> 0:
#             self.balance += amount
#             print(f"deposited:{amount},New balance = {self.balance}") 
#         else :
#             print("insufficient fund or invalid deposit")
#     def withdraw(self,amount):
#         if amount > 0 :
#             self.balance -= amount
#             print(F"withdrawal amount:{amount},New balance ={self.balance} ")

#     def get_balance(self):
#         return self.balance
#     def get_account_info(self):
#         return f"Account number:{self.account_number },Account holder:{self.account_holder},balance : {self.balance}"
# account_1 = Bank_account(123456789,"John Snow",99999999999999999999)
# print(account_1)
# account_1.deposit(5000)
# account_1.withdraw(500)
# print(f"Current balance{account_1.get_balance()}")
