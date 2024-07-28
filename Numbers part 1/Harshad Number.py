# check if the sum of the digits can perfectly divide the number or not.

def Harshad_Number(num):
    lenth=len(str(num))
    count=0
    while(num>0):
        rem=num%10
        if (num%rem==0):
            count+=1
        num//=10

    if(count==lenth):
        return True
    else:
        return False

num= int(input("Enter a number:"))
'''print(f"Is {num} a Harshad Number:{Harshad_Number(num)}")'''
print(Harshad_Number(num))