import math as m

def Perfectsquare(num):
    x=m.sqrt(num)
    if (x*x==num):
        return True
    else:
        return False
    
num=int(input("Enter a number:"))    
print(f"Is {num} is the Perfect Square: { Perfectsquare(num)}")