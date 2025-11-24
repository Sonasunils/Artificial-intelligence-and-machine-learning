# a = [1,2,3]
# b = a
# b.append(4)
# print(a)

# print(id(a))
# print(id(b))


# for i in range(3):
#     print(i)
# else:
#     print("Done")



a =[3,4,2,7,5,3]
a.sort()
s=a

k = []
for i in s:
    if i not in k :
        k.append(i)
print(k)
print(k[-2])