# class parent :
#     v1 = "value 1"
#     v  = " value 2"
# class child(parent)
# pass
#     p = parent ()
#     print("using parent object")
#     print (p.v1,p.v)
# c = child()
# print("using child object")
# print(c.v1,c.v)
# class father :
#     def __init__(self):
#         self.property = 8000000000000000000000
#     def display (self):
#         print("father property = ",self.property)
# class son (father ):
#     pass
# s = son()
# s.display()
# class student :
#     def get_no(self,no):
#         self.no = no
#     def put_no(self):
#         print(self.no)
# class test(student):
#     def get_marks(self,sub1,sub2) :
#         self.sub1 = sub1
#         self.sub2 = sub2
#     def put_marks(self):
#         print("sub1 marks =",self.sub1)
#         print("sub2 marks = ",self.sub2)
# class result(test):
#     total = 0
#     def display (self):
#         result.total = self.sub1 + self.sub2
#         self.put_no()
#         self.put_marks()
#         print("total marks = ",result.total) 
# r = result ()
# r.get_no(2)
# r.get_marks(90,99)
# r.display()
# class father :
#     def height (self):
#         print("height:",6)
# class mother :
#      def nature (self):
#          print("nature :""kind")
# class child (father,mother ):
#     pass 
# c = child()
# c.height()
# c.nature()
# def add(x,y):
#     return x + y
# def subtract(x,y):
#     return x - y 
# def multiply(x,y):
#     return x * y
# def divide (x,y):
#     return x / y
# while True :
#     num1 = int(input("enter first number "))
#     num2 = int(input("enter  second number "))
    
#     # if choice in ('1','2','3','4'):
      
#     if choice == 1:
#         print(num1 ,'+', num2 ,'=', add(num1,num2))
#     elif choice == 2:
#         print(num1 ,'-',num2,'=',subtract(num1,num2))
#     elif choice == 3:
#         print(num1 ,'*', num2 ,'=', multiply(num1,num2))
#     elif choice == 4:
#         print(num1 ,'/', num2 ,'=', divide(num1,num2))
#     next_calculation = str(input("let's do an another a calculation (yes / no):"))
#     if next_calculation == "no":
#         break
#     else :
#         print("invalid input")
         
# # class car :
#     def __init__(self,brand ,model):
#         self.brand = brand
#         self.model = model
#     def move(self):
#         print("Drive")
# class boat :
#     def __init__(self,brand ,model):
#          self.brand = brand
#          self.model = model
#     def move (self):
#         print("sail")
# class plane :
#     def __init__(self,brand ,model):
#         self.brand = brand
#         self.model = model
#     def move (self):
#         print("fly")
# car1 =car("ford","mustang ")
# boat1 = boat("Ibiza","touring 20") 
# plane1 = plane("boeing","747")
# for i in (car1,boat1,plane1):
#     i.move()        
        