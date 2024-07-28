def dec_to_hex(num):
    dec_num=[]
    while num>0:
        rem=num%16
        if(rem<10):
            dec_num.append(rem)
        else:
            dec_num.append(chr(rem+55))
        num//=16
    for i in range(len(dec_num)-1,-1,-1):
        print(dec_num[i],end='')

num=int(input("Enter a number:"))
print("The Octal form is:",end='')
dec_to_hex(num)