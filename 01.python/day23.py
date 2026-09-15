# try:
# print(x)
# except:
#     print("An exception has occured")
# try:
#     print(x)
# except NameError:
#     print("variable x is not defined") 
# except :
#     print("something went wrong ")
# try :
#     print("hello world")
# except:
#     print("something went wrong")
# else :
#     print("nothing went wrong") 
# try:
#     print(x)
# except :
#     print("something went wrong ")   
# finally :
#     print("the try execpt is finished")
# n =10 
# try :
#   res =  n / 0 
# except ZeroDivisionError:
#     print("can't be divided by zero")
# try:
#     n = 0
#     res = n /100
# except ZeroDivisionError:
#     print("You can't be divided by zero ")
# except ValueError:
#     print("enter a valid number ")
# else :
#     print("result is ",res)
# finally :
#     print("execution is complete") 

class InvalidAgeError(Exception):
    def __init__(self, age, msg="Age must be between 0 and 120"):
        self.age = age
        self.msg = msg
        super().__init__(self.msg)

    def __str__(self):
        return f'{self.age} -> {self.msg}'

# Step 2: Use the custom exception in your code
def set_age(age):
    if age < 0 or age > 120:
        raise InvalidAgeError(age)
    else:
        print(f"Age set to: {age}")

# Step 3: Handling the custom exception
try:
    set_age("j")  # This will raise the custom exception
except InvalidAgeError as e:
    print(e)