def Automorphic_number(num):
    x=num**2
    rem=x%10
    if (rem==num):
        return True
    else:
        return False
    
num= int(input("Enter a number:"))
print(f"Is {num} is an Automorphic Number: {Automorphic_number(num)}")    