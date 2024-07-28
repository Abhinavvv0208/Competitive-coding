def hcf(n1,n2):
    for i in range(1,min(n1,n2)+1):
        if(n1%i==0 and n2%i==0):
            hcf=i
    return hcf      

n1=int(input("Enter a number:"))
n2=int(input("Enter another number:"))
print(f"The HCF of {n1} and {n2} is:{hcf(n1,n2):}")