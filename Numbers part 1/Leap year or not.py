yr=int(input("Enter the year:"))
if(yr%400==0) or (yr%4==0 and yr%100!=0):
    print("It is a leap year")
else:
    print("It is not a leap year")    