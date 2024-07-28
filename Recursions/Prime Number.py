def prime(num,i=2):
    if num==i:
        return True
    elif num%i==0:
        return False
    return prime(num,i+1)

num=int(input("Enter a number:"))
if prime(num):
    print(f"Yes {num} is a Prime Number")
else:
    print(f"{num} is not a Prime Number")