#How to Concatenate Two List Using Python Codes
# Solution 1:Using + operator
l1=[1,2,3,"a","b"]
l2=[2,3,"k","f","j"]
l12=l1+l2
print(l12)

#Solution2:With unique values

l1=[1,2,3,"a","b"]
l2=[2,3,"k","f","j"]
l12=list(set(l1+l2))
print(l12)

# Solution3:Using extend() function

l1=[1,2,3,"a","b"]
l2=[2,3,"k","f","j"]
l1.extend(l2)
print(l12)
