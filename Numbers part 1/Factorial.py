def factorial(n):
    if (n==1 or n==0):
        return n
    else:
        return n*factorial(n-1)
    
n = int(input("Enter a number:"))    
if n<1:
    print("Enter a Positive number")
else:
    print(factorial(n))