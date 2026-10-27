# l=[10, 5, 8, 10, 20, 15]

# for i in range(len(l)-1):
#     if l[i]>l[i+1]:
#         l[i],l[i+1]=l[i+1],l[i]
# print(l)
# print(l[-2])d



k=[[1,3], [2,6], [8,10], [9,12]]
s=[]
m=len(k)
for i in range(m-1):
    if i%2==1:
        pass
    else:
      m=k[i][0]
      l=k[i+1][1]
      s.append([m,l])
    
      
print(s)