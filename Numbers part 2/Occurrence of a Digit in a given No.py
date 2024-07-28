#Program to count the Occurrence of a Digit in a given Number in Python

def countOccurences(n,d):
    count=0
    while n>0:
        if(n%10==d):
            count+=1
        n//=10
    return count

n=int(input("Enter a number:"))
d=int(input("Enter the digit you want to find the occurrence of:"))
print("No of occurrences:",countOccurences(n,d))    