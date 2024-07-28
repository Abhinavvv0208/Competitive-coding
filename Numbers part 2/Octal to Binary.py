def oct_to_bin(num):
    binArray=[]
    while num>0:
        rem=num%10
        while rem>0:
            bin=rem%2
            binArray.append(bin)
            rem//=2
        num//=10    

    for i in range(len(binArray)-1,-1,-1):
        print(binArray[i],end='') 

num=int(input("Enter the number in Octal form:")) 
print("The binary form is:",end='')
oct_to_bin(num)
