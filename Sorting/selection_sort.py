arr=[64, 34, 25, 12, 22, 11, 90, 5]
print(arr)
for i in range(len(arr)):
    m=i
    for j in range(i+1,len(arr)):
        if arr[j]<arr[m]:
            m=j
    t=arr[m]
    arr[m]=arr[i]
    arr[i]=t
print(arr)