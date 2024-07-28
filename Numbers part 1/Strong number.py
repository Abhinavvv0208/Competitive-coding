def factorial(n):
    if (n==0 or n==1):
        return 1
    else:
        return n *factorial(n-1)
def strong_number(n):
     if n==0:
       return 0
     else:
       k=n%10
       fact=factorial(k)
       return fact + strong_number(n//10) 

n=int(input("Enter a number:"))
if (strong_number(n)==n):
    print("Yes",n,"is a strong Number.")
else:
    print("No",n,"is not a strong Number.")    


    