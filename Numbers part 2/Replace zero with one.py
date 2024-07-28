#Replace all 0’s with 1 in a given integer 

num=int(input("Enter a number:"))
num2=0
if num==0:
    num2=1

while(num>0):
    rem=num%10
    if rem==0:
        rem=1
    num2=num2*10+rem
    num//=10

num=0
while num2>0:
    rem=num2%10
    num=num*10+rem
    num2//=10

print("The result:", num)


