'''num=int(input("Enter the no. of terms:"))
n1=0
n2=1
print("Fibonacci Series:", n1, n2, end=" ")
for i in range(2,num):
    n3=n1+n2
    n1=n2
    n2=n3
    print(n3,end=" ")
print()    '''

#with function
def fibo(n):
    if n<=1:
        return n
    else:
        return fibo(n-1)+fibo(n-2)
    
n= int(input("Enter the no. of terms:"))

if n<=0:
    print("Enter a valid positive number")
else:
    print("The Fibonacci Series:")
    for i in range(n):
        print(fibo(i))