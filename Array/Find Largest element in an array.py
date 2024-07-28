def largest(arr):
    max=arr[0]
    for i in range(len(arr)):
        if arr[i]>max:
            max=arr[i]
    return max

arr=eval(input("Enter an array of numbers:"))
print(" Largest element in an array:", largest(arr))