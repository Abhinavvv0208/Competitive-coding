#Addition of two fractions

def hcf(den1,den2):
    for i in range(1,min(den1,den2)+1):
        if(den1%i==0 and den2%i==0):
            HCF=i
    return HCF

num1,den1=map(int, list(input("Enter numerator and denominator of first number : ").split(" ")))
num2,den2=map(int, list(input("Enter numerator and denominator of second number: ").split(" ")))

lcm= (den1*den2)//hcf(den1,den2) 

sum= ((num1*lcm)//den1)+ ((num2*lcm)//den2)
num3= sum//hcf(sum,lcm)
LCM= lcm//hcf(sum,lcm)

print(f"The sum of:{num1}/{den1}+{num2}/{den2}={num3}/{LCM} ")
