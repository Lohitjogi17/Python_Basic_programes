# Python Program to Check Prime Number
num=int(input("enter a number"))
if num==1:
    print(num,"is not a prime number")
if num>1:
    for i in range(2,num):
        if num%i==0:
            print(num,"It is not a prime number")
            break;
    else:
        print(num,"Its a prime number")
            
