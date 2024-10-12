def fun():
    arr = [3, 1, 2, 4, 5, 9, 13, 14, 12]
    odd=[]
    even=[]
    for i in range(len(arr)):
        if i%2==0:
            even.append(arr[i])
        else:
            odd.append(arr[i])
    odd.sort(reverse=True)
    even.sort()
    return even+odd
s=fun()
print(s)