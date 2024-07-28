def Perfect_number(n):
    sum=0
    for i in range (1,n):
         if (n%i==0):
            sum+=i
    if(sum==n):
         return True
    else:   
         return False


n=int(input("Enter a number:")) 
print(Perfect_number(n))    
