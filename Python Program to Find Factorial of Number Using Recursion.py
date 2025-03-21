# Python Program to Find Factorial of Number Using Recursion - Complete Guide
def fact(n):
    if n==1:
        return n
    else:
        return (n* fact(n-1))
n=int(input("Enter a number here:"))
if n<=0:
    print("Factorial of number less than 1 doesnot exist")
else:
    print("Factorial of a number is",fact(n))
    
