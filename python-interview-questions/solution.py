l=[10, 5, 8, 10, 20, 15]

for i in range(len(l)-1):
    if l[i]>l[i+1]:
        l[i],l[i+1]=l[i+1],l[i]
print(l)
print(l[-2])