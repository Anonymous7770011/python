a=[7,1,5,3,6,4]
minprice=float('inf')
maxprofit=0
for i in range(len(a)):
    if a[i]<minprice:
        minprice=a[i]

if a[i]-minprice>maxprofit:
    maxprofit=a[i]
print("minprice =  ",minprice)
print("maxprofit = ",maxprofit)
