#A Number that is smaller than the sum of all it's factors except the number itself is known as an Abundant number.

def Abundant_number(num):
    sum=0
    for i in range(1,num):
        if(num%i==0):
            sum+=i

    if (sum>num):
        return True
    else:
        return False
        
num=int(input("Enter a number:"))  
print(f"{num} is an Abundant Number:{Abundant_number(num)}")      