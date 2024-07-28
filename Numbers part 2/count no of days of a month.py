year=int(input("Enter the year:"))
month=int(input("Enter the month in number:"))

if((month==2) and ((year%4==0) or ((year%100!=0) and (year%400==0)))):
    print("Total no. of days are 29")
     
elif(month==2):
    print("Total no. of days are 28")

elif((month==1)or(month==3)or(month==5)or(month==7)or(month==8)or(month==10)or(month==12)):
     print("Total no. of days are 31")

else:
    print("Total no. of days are 30")


year=int(input("Enter the year:"))
month=int(input("Enter the month in number:"))
