a=0
b=1
l=[a,b]
for i in range(5):
    s=a+b
    l.append(s)
    a=b
    b=s
print(l)