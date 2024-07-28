def power(a,b):
    if(b!=0):
        return a*power(a,b-1)
    else:
        return 1
    
a=int(input("Enter the base:"))
b=int(input("Enter the power:"))
print("The result is:",power(a,b))
