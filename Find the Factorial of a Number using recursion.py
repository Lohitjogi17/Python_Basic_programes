#Find the Factorial of a Number using recursion
def fact(a):
    if a==0:
        return 1;
    else:
        return ((a)*fact(a-1))

num=int(input("enter a number"))
result=fact(num)
print("The factorial of a given number is:",result)
