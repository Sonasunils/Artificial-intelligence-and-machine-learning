#Exercise 1: Reverse each word of a string

# str = 'My Name is Jessa'
# m=""
# k = str.split()
# for i in k:
#     m=m+"".join(i[::-1])+' '
# print(m)


#Exercise 2: Remove items from a list while iterating
# In this question, you need to remove items from a list during iteration without creating a separate copy of the list.
# Remove numbers greater than 50

# number_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# k = [i for i in number_list if i <50]
# print(k)


#Exercise 3: Display all duplicate items from a list

# sample_list = [10, 20, 60, 30, 20, 40, 30, 60, 70, 80]

# s = []
# for i in sample_list:

#     if i in s:
#         continue
#     if sample_list.count(i)>1:
#         s.append(i)
# print(s)


#Exercise 5:/print the following number pattern

# 1 1 1 1 1 
# 2 2 2 2 
# 3 3 3 
# 4 4 
# 5


# rows = 5
# x = 0
# # reverse for loop from 5 to 0
# for i in range(rows, 0, -1):
#     x += 1
#     for j in range(1, i + 1):
#         print(x, end=' ')
#     print('\r')

#Exercise 6:Exercise 8: Create an inner function


# Question Description:
# Create an outer function that accepts two strings, x and y (where x = 'Emma' and y = 'Kelly').
# Create an inner function within the outer function that concatenates x and y.
# Finally, the outer function will join the word 'developer' to the result of the inner function's concatenation.

# def ss(s,k):
#     m = s
#     l = k
#     def con():
#         p = m + l
#         return p
#     pp = con()
#     print(pp + "developer")
# ss("sona",'ss')



#Excercise 7:Write a function that reverses a given string.

# def rev(s):
#     k = s[::-1]
#     print(k)
# m = input("enter a string")
# rev(m)


#excercise 8 : list filtering filter its only numeric

# def filter(s):
#     k =[]
#     for i in s:
#         if isinstance(i, int):
#             k.append(i)
#     print(k)
# m =(input("enter a list"))
# filter(m)


# def filter_numbers(lst):
#     k = []
#     for i in lst:
#         if isinstance(i, int):
#             k.append(i)
#     print(k)

# # Example input: [12, "a", 15, "b"]
# m = [12, "a", 15, "b"]
# filter_numbers(m)


#excercise 8 palindrome

# Palindrome Check
# Task: Write a function that checks if a given string is a palindrome (reads the
# same forwards and backwards), ignoring spaces, punctuation, and letter casing.

# def pall(s):
  
#     k = s[::-1]
#     if k == m:
#         print("palindrome")
#     else:
#         print('not palindrome')
# p = input("enter a string")
# m= " "
# for i in p:
#     if i.isalpha():
#         m.join(i)
# pall(m)

