arr = [47, 89, 12, 56, 23, 9, 72, 35]

print(arr)
for i in range(1,len(arr)):
    for j in range(i,-1,-1):
        if arr[i]<arr[j]:
            t=arr[i]
            arr[i]=arr[j]
            arr[j]=t
            i=j
print(arr)