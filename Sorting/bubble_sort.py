arr=[64, 34, 25, 12, 22, 11, 90, 5]
print(arr)
for i in range(len(arr)-1):
    swap=False
    for j in range(len(arr)-1):
        if arr[j]>arr[j+1]:
            t=arr[j]
            arr[j]=arr[j+1]
            arr[j+1]=t
        swap=True
    if not swap:
        break

print(arr)


