#Can A Number Be Expressed As A Sum Of Two Prime Numbers

def sum_two_PrimeNo(num):
    Pr_Array=[]
    
    for i in range(2,num+1):
        count=0
        for j in range(2,i+1):
            if(i%j==0):
                count+=1
        if(count==1):
            Pr_Array.append(i) 
    flag=0
    
    for k in range(len(Pr_Array)):
        for l in range(k+1,len(Pr_Array)):
            if Pr_Array[k]+Pr_Array[l]==num:
                flag=1  
          
                print(str(Pr_Array[k]),'+',str(Pr_Array[l]))
    if(flag==0):
        print("No result found")    

num=int(input("Enter a number:"))        
print("Numbers that can be Expressed As A Sum Of Two Prime Numbers")
sum_two_PrimeNo(num)


