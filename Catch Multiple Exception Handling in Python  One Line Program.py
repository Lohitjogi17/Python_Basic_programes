# Catch Multiple Exception Handling in Python - One Line Program
string=input("Enter a something here:")

try:
    num=int(input("Enter a number here:"))
    print(string+num)
except(ValueError,TypeError) as a:
    print(a)
print("Hello word")
