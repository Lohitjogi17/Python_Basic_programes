# Find the Factorial of a Number using for loop
fact=1
num=int(input("enter a number"))
if num<0:
    print("factorial doesnot exist")
if num==0:
    print("factorail of 0 is",1)
if num>0:
    for i in range(1,num+1):
        fact=fact*i
    print("factorial of number is",fact)
