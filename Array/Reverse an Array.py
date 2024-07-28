def Rev(arr):
    new_arr=[]
    for i in range(len(arr)-1,-1,-1):
        new_arr.append(arr[i])

    return new_arr

arr=eval(input("Enter an array of numbers:"))
print("Reverse of an integer:",Rev(arr))    