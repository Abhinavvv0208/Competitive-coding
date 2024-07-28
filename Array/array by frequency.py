arr=eval(input("Enter an array of numbers:"))
freq={}
for x in arr:
    if x in freq:
        freq[x]+=1
    else:
        freq[x]=1

freq.sort()
print(freq)