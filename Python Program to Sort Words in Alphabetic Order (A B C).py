# Python Program to Sort Words in Alphabetic Order (A B C)
# Solution 1:Using string functions and for loop
a=input("Enter a string here:")
w=a.split()
for i in range(len(w)):
    w[i]=w[i].lower()
w.sort()
for i in w:
    print(i)
