#Python program to find number of integers which has exactly x divisors

num=int(input("Enter a number:"))
x=int(input("No. of Divisors:"))

count=0
for i in range(1,num+1):  
    count_fact=0        
    for j in range(1,i+1):
        if(i%j==0):
            count_fact+=1
        else:
            pass
    if(count_fact==x):
        count+=1 

print("Number of integers which has exactly x divisors:",count)        