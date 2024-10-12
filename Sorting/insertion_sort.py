l=[7,12,9,11,3]
for i in range(1,len(l)):
    ins=i
    for j in range(i,-1,-1):
        if l[j]>l[i]:
            t=l[i]
            l[i]=l[j]
            l[j]=t
            i=j
print(l)
