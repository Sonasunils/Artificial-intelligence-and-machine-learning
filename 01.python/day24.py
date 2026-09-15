# class InvaidAgeErrror:
#  def __init__(self ,age ,msg = " age must be between 0 and 120"):
#     self .age  = age 
#     self.msg = msg 
#     super().__init__(self.msg)
#  def __str__ (self):
#     return f"{self.age} {self.msg}"
# def set_age(age):
#         if age < 0 or age > 120 :
#           raise InvaidAgeErrror (age)
#         else :
#              print(f"age set to {age}")
# try :
#     set_age ("j")
# except InvaidAgeErrror as e :
#      print(e)
# a = "Hello, how are you?" 
# b = a.split()   
# c = " ".join(b)   
# print(b) 
# print(c) 
# a = "Hello, how are you?" 
# j = " ".join(a.split()[::-1])
# print(j)
# a = "Hello, how are you?" 
# j = a.split()
# print(j[::-1])
# def string_k(k,input_string):
# #  result  = []
#  words  = input_string.split(" ")  
#  for word in words :
#   if len(word)>k:
#    result.append(word) 
#  return result    

# k = 3 
# input_string  = "new world"
# print(string_k(k,input_string ))
# a  = [1,2,3,4,5,6,7,8,90]
# a.reverse()
# print(a)
# 
# remove = [2, 4, 6] 
# res = [] 
# for val in a: 
#     if val not in remove: 
#         res.append(val) 
# print(res) 
# a  = [1,2,3,4,5,6,7,8,90]
# s = set()
# dup  = []
# for  n in a :
#     if n in s :
#         dup.append(n)
#     else:
#         s.add(n)
#         print(dup)
# a =  {'a ': 100,"d ": 200}
# rs  = sum(a.values())
# print(rs)
# s = "nnnnneeeeewwwwwwwwwooooorrrrrllllddddd"
# fer = {}
# for  c in s:
#     if c in fer:
         
#      fer[c] += 1
#     else :
#        fer[c] = 1

# print(fer)
# d1 = {'x': 1, 'y': 2} 
# d2 = {'y': 3, 'z': 4} 
# d1.update(d2)
# print(d1)
# s = "new world "
# s2  = s.split()
# s3 = list(set(s2))
# s4 = " ".join(s3)
# print(s4)
# class ATM:
#     def __init__(self,balance =0):
#         self.balance = balance
#     def check_balance(self):
#         return self.balance 
#     def deposit(self,amount):
#         if amount> 0 :
#             self.balance+= amount
#             return  f"Deposited :${amount}.New Balance :${self.balance}"
#         else :
#             return "Invaild withdrawal amount"
#     def withdrawal (self,amount):
#         if 0 < amount <= self.balance:
#             self.balance -= amount 
#             return f"withdrew :${amount}.New amount :$(sel.balance )"
#         elif amount > self.balance :
#          return ' insuffiecient funds '
#         else :
#              return " invalid withdrawal"   
#     def atm_menu():
#         while True :
#              print("\nATM Menu")
#     print("1. Check Balance")    
#     print("2. Deposit ")
#     print("3. Withdraw")
#     print("4. Exit")
#     choice  = int (input('enter your choice (1 - 4)'))
#     if choice  == "1 ":
#         print(f"Current Balance:$ {atm.check_balance()}") 
#     elif choice  == "2":
#         amount = float(input("enter deposit amount"))
#                 print(atm.deposit(amount))
#     elif choice == "3 ":
#         amount = float (input("enter withdrawal amount"))
#         print(atm.withdrawal(amount))
#     elif choice  == "4":
#         print("Thank you for using the ATM  ")
#                 break
#     else :
#                  print( "invalid choice , please try again")
# if __name__ == "__main__":
#     my_atm = ATM(1000)  # Initial balance of $1000
#     atm_menu(my_atm)