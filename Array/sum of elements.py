def sum(arr):
    x=0
    for i in range(len(arr)):
        x+=arr[i]
    return x

arr=eval(input("Enter an array of numbers:"))
print("Sum of the elements:",sum(arr))    
