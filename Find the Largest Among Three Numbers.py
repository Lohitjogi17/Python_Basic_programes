# Find the Largest Among Three Numbers
num1=int(input("Enter the first number"))
num2=int(input("Enter the second number"))
num3=int(input("Enter the third number"))
if (num1>num2 and num1>num3):
    print(num1,"Is a largest")
elif(num2>num1 and num2>num3):
    print(num2,"Is a largest")
else:
    print(num3,"Is a largest")
