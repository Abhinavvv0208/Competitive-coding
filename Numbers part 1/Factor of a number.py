n=int(input("Enter a number, you want to find the factor:"))
for i in range(1,n+1):
    if(n%i==0):
        print("The factors:",i,)