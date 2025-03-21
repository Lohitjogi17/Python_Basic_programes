# Display Fibonacci Sequence Using Recursion
def fibo(n):
    if n<=1:
        return n
    else:
        return fibo(n-1)+fibo(n-2)
n=int(input("Enter a number:"))
if n<=0:
      print("Enter a positive number here")
else:
    print("Fibonaccy sequnce are:")
    for i in range(n):
        print(fibo(i))
