# Python Program to Sort a Dictionary by Value 
marks={"john":21,"monu":78,"singh":67}

#Solution 1:Sort the dictionary based on values
sv=sorted(marks.items(),key=lambda x:x[1])
print(sv)

# Solution 2:Sort only the values
v=sorted(marks.values())
print(v)
