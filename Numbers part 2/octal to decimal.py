def octal_ti_decimal(Oct_num):
    i=decimal=0
    while(Oct_num!=0):
        rem=Oct_num%10
        decimal+=rem*pow(8,i)
        Oct_num//=10
        i+=1
    return decimal   

Oct_num=int(input("Enter the number in Octal form:")) 
print("The Octal Number is {}\n And the corresponding Decimal Number is {}".format(Oct_num,octal_ti_decimal(Oct_num)))
