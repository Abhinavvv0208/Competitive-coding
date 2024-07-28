def sort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if(arr[j]>arr[j+1]):
                 arr[j],arr[j+1]=arr[j+1],arr[j]

    return arr

arr=eval(input("Enter an array of numbers:"))
print("The Sorted array:",sort(arr))
