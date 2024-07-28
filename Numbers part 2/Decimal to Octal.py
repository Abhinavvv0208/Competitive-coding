def dec_to_oct(num):
    dec_num=[]
    while num>0:
        rem=num%8
        dec_num.append(rem)
        num//=8
    for i in range(len(dec_num)-1,-1,-1):
        print(dec_num[i],end='')

num=int(input("Enter a number:"))
print("The Octal form is:",end='')
dec_to_oct(num)