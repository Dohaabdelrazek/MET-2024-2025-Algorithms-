arr = [2,7,6,4,9]
n = len(arr)
for i in range(n-1):
    for j in range (1,n):
        if(arr[j] < arr[j-1]):
            temp = arr[j]
            arr[j] = arr[j-1]
            arr[j-1] = temp
print(arr)