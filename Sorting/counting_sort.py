d=[0]
l=[0,4, 2, 2, 6, 3, 3, 1, 6, 5, 0,2, 3]
print("Input  : " ,l)
l1=[0,0,1, 2, 2, 2, 3, 3, 3, 4, 5, 6, 6]
print("Expec  : " ,l1)
d=d*(max(l)+1)
print("Base V : ",d)
for i in range(len(l)):
    d[l[i]]=d[l[i]]+1
l.clear()
print('Count V: ',d)
for i in range(len(d)):
    while d[i]>0:
        l.append(i)
        d[i]=d[i]-1
print("Result : ",l)