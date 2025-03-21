# Python Program to Display Powers of 2 Using Anonymous Function
nterms=int(input("Enter the number of terms:"))
result=list(map(lambda x:2**x, range(nterms+1)))
#print(result)in list format
for i in range(nterms+1):
    print("The value of 2 raised to power",i,"is",result[i])
