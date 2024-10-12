arr = [7, 3, 9, 12, 11]
print("Before insertion  = ",arr)

def insertion(arr,value,key):
    for i in range(key,len(arr)):
        temp=arr[i]
        arr[i]=value
        value=temp
insertion(arr,16,3)
print("After inserton    = ",arr)
