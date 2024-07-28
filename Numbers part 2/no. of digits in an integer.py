#Calculate the number of digits in an integer

def no_of_digit(num):
    count=0
    while num>0:
        rem=num%10
        count+=1
        num//=10
    return count

num=int(input("Enter a number:"))
print("No of digits:",no_of_digit(num))