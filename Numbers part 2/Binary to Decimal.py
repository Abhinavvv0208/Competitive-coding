def binary_to_decimal(b_num):
    i=decimal=0
    while(b_num!=0):
        rem=b_num%10
        decimal=decimal+rem*pow(2,i)
        b_num//=10
        i+=1
    return decimal

b_num=int(input("Enter the number in binary form:"))
print("The Binary Number is {}\n And the corresponding Decimal Number is {}".format(b_num,binary_to_decimal(b_num)))