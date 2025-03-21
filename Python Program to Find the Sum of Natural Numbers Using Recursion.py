#Python Program to Find the Sum of Natural Numbers Using Recursion
def NNS(n):
    if n<=1:
        return 1
    else:
        return n+ NNS(n-1)
n=int(input("Enter a number here:"))
if n<=1:
    print("Enter a positive number")
else:
    print("Sum of the natural numbers",NNS(n))
    
