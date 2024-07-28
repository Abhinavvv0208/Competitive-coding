def hexa_to_decimal(hex_num):
    l=len(hex_num)
    size=l-1
    decimal=0

    for i in range(l):
        if '0'<=hex_num[i]<='9':
            digit=int(hex_num[i])

        elif 'A'<=hex_num[i]<='F':
             digit=ord(hex_num[i])-55

        elif 'a'<=hex_num[i]<='f':
            digit=ord(hex_num[i])-87
        else:
            break
        decimal+=(digit*pow(16,size-i))
        '''size-=1
        i+=1'''

    return decimal

hex_num=input("Enter a Hexadecimal number:")
print("The Decimal Form is:",hexa_to_decimal(hex_num))

#with while loop

def hexa_to_decimal(hex_num):
    l=len(hex_num)
    size=l-1
    decimal=i=0

    while i<l:
        if '0'<=hex_num[i]<='9':
            digit=int(hex_num[i])

        elif 'A'<=hex_num[i]<='F':
            digit=ord(hex_num[i])-55

        elif 'a'<=hex_num[i]<='f':
            digit=ord(hex_num[i])-87

        else:
            break
        decimal+=(digit*pow(16,size-i)) 
        i+=1

    return decimal

