def bin_to_oct(num):
    OctalArray=[]
    i=0
    Oct_digit=0
    count=0

    while(num!=0):
        rem=num%10
        Oct_digit+=rem*pow(2,i)
        num//=10
        i+=1
        count+=1   
        
        if(count==3):
            OctalArray.append(Oct_digit)
            Oct_digit=0
            i=0
            count=0
            
    if(count!=0):
        OctalArray.append(Oct_digit)  

    for j in range(len(OctalArray)-1,-1,-1):
        print(OctalArray[j],end='')     

num=int(input("Enter the number in binary form:"))
print("The Octal form is:",end='')
bin_to_oct(num)