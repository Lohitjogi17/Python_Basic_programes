# Python Program to Check Leap Year
year=int(input("Enter a year"))
if (year % 400==0 and year %100== 0):
    print(year,"Is a leap year")
elif(year%4==0 and year%100 !=0):
    print(year,"Is a leap year")
else:
    print(year,"Isnot a leap year")
