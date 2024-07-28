def lcm(n1,n2):
    for i in range(max(n1,n2), (n1*n2)+1):
        if(i%n1==0 and i%n2==0):
            LCM=i
            break
    return LCM

n1=int(input("Enter a number:"))
n2=int(input("Enter another number:"))
print(lcm(n1,n2))        