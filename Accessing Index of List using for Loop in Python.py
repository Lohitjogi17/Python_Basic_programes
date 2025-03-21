#Accessing Index of List using for Loop in Python
# Solution1:Using Enumerate method
#l=[34,5,62,37,77,89]
#for index, value in enumerate(l,start=1):
    #print(index,"-",value)

#l=[34,5,62,37,77,89]
#for index, value in enumerate(l):
 #   print(index,"-",value)

# Solution2:Not using enumearte method

l=[34,5,62,37,77,89]
for index in range(len(l)):
    value=l[index]
    print(index,"-",value)
