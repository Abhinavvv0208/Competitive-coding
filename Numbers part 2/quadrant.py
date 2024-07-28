#Python program to find out the quadrant in which the given co-ordinate lie

def Quadrant(x,y):
    
    if (x>=0 and y>=0):
        print("1st Quadrant")
    elif(x<0 and y>=0):
        print("2nd Quadrant")
    elif(x<0 and y<0): 
        print("3rd Quadrant") 
    elif(x>=0 and y<0):
        print("4th Quadrant")  

x=int(input("Enter a number:"))
y=int(input("Enter another number:"))
print("The number lies in :", end='')
Quadrant(x,y)
