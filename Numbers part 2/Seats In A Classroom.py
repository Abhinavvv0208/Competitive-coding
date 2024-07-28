#Python Program for Permutations In Which N People Can Occupy R Seats In A Classroomif


def factorial(x):
    if(x==0 or x==1):
        return 1
    else:
        return x* factorial(x-1)
    
def seat_permutation(N,R):
    result= factorial(N)/factorial(N-R)
    print(result)

N=int(input("No. of people:"))
R=int(input("No. of Seats available:"))
print("Permutations In Which N People Can Occupy R Seats In A Classroom:", end='')
seat_permutation(N,R)