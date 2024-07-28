#Python Program for Finding Maximum Number Of Handshakes

def Handshakes(N):
    if (N<1):
        return 1
   
    else:
        return (N*(N-1))/2
    
N = int(input("Enter number of People:"))
print("Maximum no. of Handshakes:",Handshakes(N))