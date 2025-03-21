# Python Program to Find Numbers Divisible by Another Number
# solution 2:Using lambda function and filter
l=[39,45,52,65,78,90,118]
result=list(filter(lambda x : x%13==0,l))
print("The values divisible by 13 in the list are:",result)
