def fun():
    l=[2,-1,1]
    m=0
    for i in range(1,len(l)):
        if abs(l[i])<abs(l[m]):
            m=i
    if abs(l[m]) in l:
        return abs(l[m])
    else:
        return l[m]
print(fun())