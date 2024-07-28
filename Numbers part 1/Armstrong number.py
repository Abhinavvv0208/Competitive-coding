n=int(input("Enter a number:"))
num=n
sum=0
length=len(str(n))
for i in range(length):
    k=n % 10
    sum+=pow(k,length)
    n//=10
if (sum==num):
    print("It's an Armstrong Number")
else:
    print("No....")
