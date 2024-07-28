def printOrder(arr):
    new_arr=[]
    arr.sort()
    for i in range((len(arr)//2)):
        new_arr.append(arr[i])

    for j in range(len(arr)-1,len(arr)//2-1,-1):
        new_arr.append(arr[j])

    return new_arr

arr=eval(input("Enter an array of numbers:"))
print("The resultant array",printOrder(arr))

    



