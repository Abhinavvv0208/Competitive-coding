def smallest(arr):
    min=arr[0]
    for i in range(len(arr)):
        if(arr[i]<min):
            min=arr[i]
    return min

arr=eval(input("Enter an array of numbers:"))
print("Smallest element in an array:", smallest(arr))
