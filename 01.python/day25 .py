# class ATM:
#     def __init__(self, balance=0):
#         self.balance = balance

#     def check_balance(self):
#         return self.balance

#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#             return f"Deposited ${amount}. New balance: ${self.balance}"
#         else:
#             return "Invalid deposit amount."

#     def withdraw(self, amount):
#         if 0 < amount <= self.balance:
#             self.balance -= amount
#             return f"Withdrew ${amount}. New balance: ${self.balance}"
#         elif amount > self.balance:
#              return "Insufficient funds."
#         else:
#             return "Invalid withdrawal amount."

# def atm_menu(atm):
#     while True:
#         print("\nATM Menu:")
#         print("1. Check Balance")
#         print("2. Deposit")
#         print("3. Withdraw")
#         print("4. Exit")

#         choice = input("Enter your choice (1-4): ")

#         if choice == '1':
#             print(f"Current balance: ${atm.check_balance()}")
#         elif choice == '2':
#             amount = float(input("Enter deposit amount: $"))
#             print(atm.deposit(amount))
#         elif choice == '3':
#             amount = float(input("Enter withdrawal amount: $"))
#             print(atm.withdraw(amount))
#         elif choice == '4':
#             print("Thank you for using the ATM.")
#             break
#         else:
#             print("Invalid choice. Please enter a number between 1 and 4.")

# if __name__ == "__main__":
#     atm = ATM(1000) #initial balance
#     atm_menu(atm)