#Python Program to Check If the Number is Armstrong or Not
num=int(input("Enter a number here:"))
order=len(str(num))
sum=0
temp=num
while temp>0:
    digit=temp%10
    cube=digit**3
    sum=sum+cube
    temp //=10
if sum==num:
    print("It is Armstrong number")
else:
    print("It is not an Armstrong number")
