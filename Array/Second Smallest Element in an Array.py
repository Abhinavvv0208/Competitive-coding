import math as m
def Second_smallest(arr):
    first=m.inf
    second=m.inf
    for i in range(len(arr)):
        if(arr[i]<first):
            first=arr[i]
    
    for j in range(len(arr)):
        if(arr[j]!=first and arr[j]<second):
            second=arr[j]

    return second

arr=eval(input("Enter an array of numbers:"))
print("The second smallest element is:",Second_smallest(arr))

