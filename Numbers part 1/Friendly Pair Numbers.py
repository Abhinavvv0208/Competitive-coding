def friendly_pair(n1,n2):
    sum1=sum2=0
    for i in range(1,n1):
        if(n1%i==0):
            sum1+=i
    for j in range(1,n2):
        if(n2%j==0):
            sum2+=j
    if (sum1==n1 and sum2==n2):
        return True
    else:
        return False
    
n1=int(input("Enter a number:"))    
n2=int(input("Enter another number:")) 
print("The numbers are Friendly pair:",friendly_pair(n1,n2))