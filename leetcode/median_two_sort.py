#num3=[1,2,3]
num3=[1,2,3]
if len(num3)%2==0:
    s=len(num3)//2
    print(((num3[s]+num3[s-1]))/2)   
else:
    print(num3[len(num3)//2])
    